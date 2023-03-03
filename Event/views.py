from django.shortcuts import render,HttpResponse,redirect
from .models import Event,participation_event,Person
from django.views.generic import *
from django.contrib import messages
from .forms import FormEvent
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
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
    