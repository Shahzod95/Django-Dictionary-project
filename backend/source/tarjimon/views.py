from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html', {'ism':'Kimdir'})

def welcome(request):
    return HttpResponse("""
    <h1>Salom Do'stlar saytimizga xush kelibsizlar!!!</h2>
    <hr>
    <p>Bu mening yangi loyiham</p>
    """)
