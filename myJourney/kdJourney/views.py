from django.shortcuts import render
from .models import Profile, LearningEntry

def index(request):
    entries = LearningEntry.objects.all().order_by('-date')
    return render(request, 'index.html', {'entries': entries})

def aboutMe(request):
    profile = Profile.objects.first()  # Fetch the first (and probably only) profile
    return render(request, 'aboutMe.html', {'profile': profile})
