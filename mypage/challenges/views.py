from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
# Create your views here.


monthly_challenges = {
    
    "january": "You are in Jan",
    "february": "You are in feb",
    "march": "You are in march",
    "april": "You are in april",
    "may": "You are in may",
    "june": "You are in june",
    "july": "You are in july",
    "august": "You are in august",
    "september": "You are in september",
    "october": "You are in october",
    "november": "You are in november",
    "december": "You are in december"
    
}

def monthly_challenge_by_number(request,month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month ")
    redirect_month = months[month-1]    
    return HttpResponseRedirect("/challenges/"+redirect_month)

def monthly_challenge(request,month):
    try:
        challenge_text = monthly_challenges[month] 
    except:
        HttpResponseNotFound("This month is not supported ! ! ! !")
    
    return HttpResponse(challenge_text)

