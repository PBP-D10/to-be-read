from reader.models import Profile
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.
def view_profile(request):
    current_profile = Profile.objects.get(user=request.user)
    context = {'profile':current_profile}
    return render(request, "view_profile.html", context)

def edit_profile(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        date_of_birth = request.POST.get('date_of_birth')
        
        if name != profile.name:
            profile.name = name
        if email != profile.email:
            profile.email = email
        if address != profile.address:
            profile.address = address
        if date_of_birth != profile.date_of_birth:
            profile.date_of_birth = date_of_birth
        
        profile.save()
        return HttpResponseRedirect(reverse('reader:view_profile'))

    context = {'profile': profile}
    return render(request, "edit_profile.html", context)
