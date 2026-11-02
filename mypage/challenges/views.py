from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse 
from django.template.loader import render_to_string
# Create your views here.

#python3 manage.py runserver
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
    
    months = list(monthly_challenges.keys())
    
    return render(request,"challenges/index.html",{
        "months":months
    })



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
        return render(request,"challenges/challenge.html",{
            "text": challenge_text,
            "month_name":month
        })
    except:
        HttpResponseNotFound("<h1>This month is not supported ! ! ! !</h1>")
    
    

