from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request,"generator/home.html")

def about(request):
    return render(request,"generator/about.html")


def password(request):
    the_password = "test"
    characters=list("abcdefghijklmnopqrstuvwxyz")
    the_password=""
    if request.GET.get("uppercase"):
        characters.extend("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    if request.GET.get("special"):
        characters.extend(list("~!#$%^&*()"))
    if request.GET.get("numbers"):
        characters.extend("1234567890")


    length = int(request.GET.get("length",15))
    for x in range(length):
        the_password+= random.choice(characters)

    return render(request,"generator/password.html",{"password":the_password})
