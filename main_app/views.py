from django.shortcuts import render, redirect
from .models import Critter
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def critters_index(request):
  critters = Critter.objects.all()
  return render(request, 'critters/index.html', { 'critters': critters })

def critters_detail(request, critter_id):
  critter = Critter.objects.get(id=critter_id)
  return render(request, 'critters/detail.html', { 'critter': critter })

class CritterCreate(CreateView):
  model = Critter
  fields = '__all__'

class CritterUpdate(UpdateView):
  model = Critter
  fields = ['species', 'description', 'age']

class CritterDelete(DeleteView):
  model = Critter
  success_url = '/critters/'