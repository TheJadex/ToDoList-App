from django.shortcuts import render
# from django.http import HttpResponse, HttpResponseRedirect
from django import forms
# from django.urls import reverse

# Create your views here.

tasks = []

class TaskForms(forms.Form):
    task = forms.CharField(label="Task", max_length=225)

def name(request):
    if request.method == "POST":
        form = TaskForms(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            tasks.append(task)
        else:
            return render(request, 'index.html', {
                "form": form,
            })
        
    return render(request, 'index.html',{
        "task": tasks,
        "form": TaskForms(),
    })