from django.shortcuts import render
from django.contrib.auth.models import User
from members.models import Employee
from members.serializer import EmployeeSer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

def home(request):
    return render(request, "Home_Page.html")

#data from models (Member)
def all_members(request):
    mymembers = Employee.objects.all().values()
    context={
        'mymembers' : mymembers,
    }
    return render(request, "all_members.html", context)

def about_us(request):
    return render(request, "about_us.html")

def contact_us(request):
    return render(request, "contact_us.html")

def details(request, employee_id):
    mymembers = Employee.objects.get(employee_id=employee_id)
    context = {
        'mymembers' : mymembers
    }
    return render(request, "details.html", context)

def news(request):
    return render(request, 'news.html')

def entertainment(request):
    return render(request, 'movies.html')

def blog(request):
    return render(request, 'blog_page.html')

def register(request):
    if request.method == 'POST':
        fn = request.POST.get('firstName')
        ln = request.POST.get('lastName')
        e = request.POST.get('email')
        c = request.POST.get('city')
        d = request.POST.get('department')
        p = request.POST.get('password')
        p = request.POST.get('ContactNo')

        #add employee in model
        member = Employee(firstname = fn, lastname = ln, phone = p, city = c, department = d)
        member.save()

        #create user in user model
        user = User.objects.create_user(username=e, email='', password=p)
        user.save()
    return render(request, 'register.html')


class EmployeeViews(APIView):
    def get(self, r):
        accountobj = Employee.objects.all()
        serobj = EmployeeSer(accountobj, many=True)
        return Response(serobj.data, status=status.HTTP_200_OK)

    def post(self, r):
        ser = EmployeeSer(data = r.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)