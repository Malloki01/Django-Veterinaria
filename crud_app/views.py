# Create your views here.
# views.py

from django.shortcuts import render

def mi_vista(request):
    return render(request, 'index.html')