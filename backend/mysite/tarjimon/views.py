from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1 style='color:red;'>Salom</h1>")

def welcome(request):
    return HttpResponse("""
    <h1>Salom Do'stlar saytimizga xush kelibsizlar!!!</h2>
    <p>Bu mening yangi loyiham</p>
    """)
