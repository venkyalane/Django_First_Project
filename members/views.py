from django.shortcuts import render
from django.http import HttpResponse
from members.models import Member

# Create your views here.

# def members(request):
#     return HttpResponse("<h1 align='center'>Hello world!</h1>")

def home(request):
    return render(request, "Home_Page.html")

#data from models (Member)
def all_members(request):
    mymembers = Member.objects.all().values()
    context={
        'mymembers' : mymembers,
    }
    return render(request, "all_members.html", context)

def about_us(request):
    return render(request, "about_us.html")

def contact_us(request):
    return render(request, "contact_us.html")

def details(request, id):
    mymembers = Member.objects.get(id=id)
    context = {
        'mymembers' : mymembers
    }
    return render(request, "details.html", context)

def main(request):
    return render(request, "main.html")

def testing(request):
    context = {
        'fruits' : ['Apple', 'Banana', 'Cherry'],
    }
    return render(request, "template.html", context)


