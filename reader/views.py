from django.shortcuts import render
from models import Profile

# Create your views here.
def get_profile(request):
    current_profile = Profile.objects.get(user=request.user)
    context = {'profile':current_profile}
    return

def edit_profile(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')

        if name != profile.name:
            profile.name = name
        if email != profile.email:
            profile.email = email
        profile.save()
    return