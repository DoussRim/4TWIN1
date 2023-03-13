from django.shortcuts import render,HttpResponse,redirect
from .models import Event,participation_event,Person
from django.views.generic import *
from django.contrib import messages
from .forms import FormEvent
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import F
from django.urls import reverse_lazy
from .Serializers import EventSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
def index(request):
    return HttpResponse("Bonjour")
def index_param(request,param):
    return HttpResponse(f"Bonjour {param}")
@login_required
def Affiche(request):
    evt=Event.objects.all()
    # resultat="-----".join(e.title for e in evt)
    # #Affichage via HttpResponse
    # return HttpResponse(resultat)
    # context={'ee':evt}
    return render(request,'Event/Affiche.html',
                  {'ee':evt})
    
class AfficheGeneric(LoginRequiredMixin,ListView):
    model=Event
    template_name="Event/Affiche.html"
    context_object_name="ee"
    # fields="__all__"
    ordering=['description']
    # queryset=Event.objects.filter(state=True)
    # def filterState(self):
    #     return Event.objects.filter(state=True)
def Detail(request,title):
    event=Event.objects.get(title=title)
    return render(request,'Event/Detail.html',
                  {'ee':event})
class DetailGeneric(DetailView):
    model=Event
    template_name="Event/Detail.html"
    context_object_name="ee"
def Add(request) :
    #Form
    #Method 
    if request.method=="GET":
        #Afficher le formulaire
        form=FormEvent()
        return render(request,'Event/Ajout.html',
                      {'form':form})
    #Method POST
    if request.method=="POST":
        form=FormEvent(request.POST,request.FILES)
        #form valid()
        if form.is_valid():
            form.save()
            # new_evt.save()
            return redirect('Aff')
        #Ajout
        #retour vers Affiche
        #erreur
        else:
            return render(request,'Event/Ajout.html',
                          {'form':form, "msg_erreur":"Erreur lors de l'ajout d'un evt"})
class Ajout(CreateView):
    model=Event
    # fields="__all__"
    form_class=FormEvent
    success_url=reverse_lazy('Aff')
def Participate(request,event_id):
    object=participation_event()
    object.person=Person.objects.get(cin=request.user.cin)
    object.event=Event.objects.get(pk=event_id)
    if participation_event.objects.filter(
        person=object.person, event=object.event).count()==0:
        object.save()
        Event.objects.filter(pk=event_id).update(
            nbe_participant=F('nbe_participant')+1
        )
    else:
        return HttpResponse(
            f"You're already participating in the event {object.event.title}"
        )
    return redirect("Aff")
def Cancel(request,id):
    evt=Event.objects.get(id=id)
    person=Person.objects.get(cin=123)
    if participation_event.objects.filter(
        person=person, event=evt).count()!=0:
        participation_event.objects.filter(
        person=person, event=evt).delete()
        evt.nbe_participant-=1
        evt.save()
    return redirect("Aff")
@api_view(['GET'])
def get_Events(request):
    events=Event.objects.all()
    serializer=EventSerializer(events,many=True)
    return Response(serializer.data,
                    status=status.HTTP_200_OK)
