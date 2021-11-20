from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

class Finch:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, species, description):
    self.name = name
    self.species = species
    self.description = description

finches = [
  Finch('Dorkus', 'House Finch', 'wee little scamp')
] 

def home(request):
  return HttpResponse('finch finch finch')
def about(request):
  return render(request, 'about.html')
def finches_index(request):
  return render(request, 'finches/index.html', {'finches': finches})