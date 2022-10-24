from django.shortcuts import render
from django.http import HttpResponse

class Critter:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, species, description, age):
    self.name = name
    self.species = species
    self.description = description
    self.age = age

critters = [
  Critter('Lolo', 'Prarie Dog', 'has the bubonic plague', 3),
  Critter('Sachi', 'California Condor', 'Super fast. Crazy endangered tho', 0),
  Critter('Raven', 'Mountain Lion', 'Almost hunted me down as I was hiking the rim before I tamed him', 4)
]
# Create your views here.
def home(request):
    return HttpResponse('<h1>AYYYE</h1>')

def about(request):
    return render(request, 'about.html')

def critters_index(request):
    return render(request, 'critters/index.html', { 'critters': critters })