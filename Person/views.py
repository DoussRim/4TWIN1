from django.shortcuts import redirect,render
from .forms import FormRegistrationUser
from django.contrib.auth import login
def SignUp(request):
    if request.user.is_authenticated:
        return redirect('Aff')
    #form
    form= FormRegistrationUser()
    if request.method=="POST":
        form= FormRegistrationUser(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('Aff')
    return render(request,'person/login.html',{'f':form})   