from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    return HttpResponse("<p>Hello about world !</p>")

def home(request):
    return render(request,'home.html',{'greeting':"Hello User !"})


def default_page(request):
    return render(request,"default.html",{'content':'Another content'})


def text_page(request):
    return render(request,'text.html',{'rev':'Reverse!','text':"Vice Versa"})
