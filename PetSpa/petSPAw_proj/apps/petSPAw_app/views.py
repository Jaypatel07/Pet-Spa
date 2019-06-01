from django.shortcuts import render, HttpResponse, redirect
from .models import Pet
from ..LogRegApp.models import User
from django.contrib import messages
def add(request):
    return render(request, "petSPAw_app/addPets.html")

def add_process(request):
    if request.session['userid']:
        valid = Pet.objects.pet_validator(request.POST)
        if valid['status'] == False:
            for error in valid['errors']:
                messages.error(request, error)
            return redirect('/dashboard/add', messages)
        else:
            return redirect('/dashboard')
    return redirect('/')

def home(request):
    return render(request, "petSPAw_app/home.html")

def aboutus(request):
    return render(request, "petSPAw_app/aboutus.html")

def dashboard(request):
    if request.session['userid']:
        context= {
            'pets': Pet.objects.filter(pet_members=request.session['userid']),
            'mypets': Pet.objects.filter(created_by =request.session['userid']),
            'userid': request.session['userid'],
        }
        return render(request, "petSPAw_app/dashboard.html", context)
    return redirect('/')

def appointment(request,id):
    if request.session['userid']:        
        context = {
            'pet': Pet.objects.get(id=id),
        }
        return render(request, "petSPAw_app/appointment.html", context)
    return redirect('/')


def edit(request, id):
    if request.session['userid']:
        context = {
            'pet': Pet.objects.get(id=id),
            'owner': User.objects.get(id=(Pet.objects.get(id=id).created_by_id)).name,
        }
        return render(request, "petSPAw_app/edit.html", context)
    return redirect('/')

def profile(request, id):
    if request.session['userid']:
        context = {
            'pet': Pet.objects.get(id=id),
            'owner': User.objects.get(id=(Pet.objects.get(id=id).created_by_id)).name,
        }
        return render(request, "petSPAw_app/profile.html", context)
    return redirect('/')

def process_edit(request,id):
   if request.session['userid']:
        context = {
            'pet': Pet.objects.get(id=id),
            'owner': User.objects.get(id=(Pet.objects.get(id=id).created_by_id)).name,
        }
        valid = Pet.objects.edit(request.POST)
        context= {
            'pet': Pet.objects.get(id=id),
        }
        if valid['status'] == False:
            for error in valid['errors']:
                messages.error(request, error)
            return render(request, "petSPAw_app/edit.html")
        else:
            updatedPet= Pet.objects.get(id=id)
            updatedPet.name= request.POST['name']
            updatedPet.age= request.POST['age']
            updatedPet.breed= request.POST['breed']
            updatedPet.comments= request.POST['comments']
            updatedPet.save()
            return redirect('/dashboard', context)
        return redirect('/')


