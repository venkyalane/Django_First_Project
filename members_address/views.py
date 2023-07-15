from django.shortcuts import render
from members_address.models import MemberAddress

# Create your views here.

def all_member(request):
    mymembers = MemberAddress.objects.all().values()
    context = {
        'mymembers' : mymembers
    }

    return render(request, 'all_member_address.html', context)