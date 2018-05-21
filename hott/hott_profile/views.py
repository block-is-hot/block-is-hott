from django.shortcuts import render, redirect, get_object_or_404
from .models import HottProfile
from .forms import ProfileEditForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from django.urls import reverse_lazy


def profile_view(request, username=None):
    owner = False

    import pdb; pdb.set_trace()
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


class ProfileEditView(LoginRequiredMixin, UpdateView):
    template_name = 'hott_profile/profile_edit.html'
    model = HottProfile
    form_class = ProfileEditForm
    login_url = reverse_lazy('auth_login')
    success_url = reverse_lazy('profile')
    slug_url_kwarg = 'username'
    slug_field = 'user__username'

    def get(self, *args, **kwargs):
        self.kwargs['username'] = self.request.user.get_username()
        return super().get(*args, **kwargs)

    def post(self, *args, **kwargs):
        self.kwargs['username'] = self.request.user.get_username()
        return super().post(*args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'username': self.request.user.get_username()})
        return kwargs

    def form_valid(self, form):
        form.instance.user.email = form.data['email']
        form.instance.user.first_name = form.data['first_name']
        form.instance.user.last_name = form.data['last_name']
        form.instance.user.save()
        return super().form_valid(form)
