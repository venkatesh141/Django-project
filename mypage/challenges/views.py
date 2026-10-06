from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse 
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

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("monthly-challenge",args=[month])
        list_items += f"<li> <a href=\"{month_path}\">{capitalized_month}</a></li>"
    response_data = f"<ul> {list_items} </ul>"
    return HttpResponse(response_data)


def monthly_challenge_by_number(request,month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month ")
    redirect_month = months[month-1]    
    redirect_path = reverse("monthly-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request,month):
    try:
        challenge_text = monthly_challenges[month] 
        response_data = f"<h1> {challenge_text} </h1>"
        return HttpResponse(response_data)
    except:
        HttpResponseNotFound("<h1>This month is not supported ! ! ! !</h1>")
    
    

