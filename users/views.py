from django.shortcuts import render, redirect, get_object_or_404
from users.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def profile_view(request, username):
    profile = User.objects.get(username=username)

    return render(request, 'profile_view.html', {"profile": profile})