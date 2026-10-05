from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound
# Create your views here.

def january(request):
    return HttpResponse("Eat no meat for entire month")

def february(request):
    return HttpResponse("walk for atleast 20 minutes everyday")

def monthly_challenge(request,month):
    challenge_text = None 
    
    if month == "january":
        challenge_text = "You are in Jan"
    elif month == "febrauary":
        challenge_text = "You are in Feb"
    elif month == "march":
        challenge_text = "You are in March"
    else:
        return HttpResponseNotFound("Month is not supported")
    
    return HttpResponse(challenge_text)

