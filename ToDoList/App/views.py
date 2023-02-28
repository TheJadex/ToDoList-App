from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

title = {"title":"ToDOList",}

def name(request):
    return render(request, "index.html", title)