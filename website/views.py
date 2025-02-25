from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Home page
def home(request):

    return render(request, 'base.html')

# Login view
@login_required
def profile_view(request):
    return render(request, 'profile.html')
