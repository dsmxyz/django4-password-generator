# Create your views here

from django.shortcuts import render
from django.http import HttpResponse
import random

# Home page
def home(request):
    return render(request, 'generator/home.html')

# Password generation page/function
def password(request):
    # Intialize password variable
    thepassword=''
    # Add whole alphabet (lowercase) to characters list 
    characters=list('abcdefghijklmnopqrstuvwxyz')
    # If uppercase is toggled on form, uppercase alphabet will be added to characters list
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    # If special characters are toggles on form, special characters will be added to characters list
        characters.extend(list('!@#$%^&*()-_=+?.>,<'))
    # If numbers is toggled on form, numbers will be added to characters list
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    # Sets the length of the generated password based on form input
    length=int(request.GET.get('length'))
    # For loop that stop when i is greater than the length variable
    for i in range(length):
        # Each pass of the loop will choose a random character from the character list and place it in the password variable
        thepassword+=random.choice(characters)
    # Renders html page
    return render(request, 'generator/password.html', {'password': thepassword})

# About us page
def about(request):
    return render(request, 'generator/about.html')