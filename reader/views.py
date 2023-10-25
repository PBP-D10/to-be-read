from django.shortcuts import render
from models import Profile

# Create your views here.
def get_profile(request):
    current_profile = Profile.objects.get(request.user)
    context = {'profile':current_profile}
    return

def edit_profile(request):
    current_profile = Profile.objects.get(request.user)