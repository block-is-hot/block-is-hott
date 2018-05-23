from django.shortcuts import render, redirect, get_object_or_404
from .models import HottProfile
from .forms import ProfileEditForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from django.urls import reverse_lazy


def profile_view(request, username=None):
    owner = False

    # import pdb; pdb.set_trace()
    if not username:
        username = request.user.get_username()
        owner = True
        if username == '':
            return redirect('/')

    profile = get_object_or_404(HottProfile, user__username=username)

    if not owner:
        return redirect('/')

    context = {
        'profile': profile,
    }
    return render(request, 'templates/profile.html', context)
