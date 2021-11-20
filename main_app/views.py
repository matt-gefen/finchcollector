from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
  return HttpResponse('finch finch finch')
def about(request):
  return HttpResponse('<h1>About the Finch Collector<h1>')