from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.

def app_page(request):
    return render (request,"bookcab.html")