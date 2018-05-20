from django.shortcuts import render, redirect
from .models import HottProfile
from .forms import ProfileEditForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from django.urls import reverse_lazy


def profile_view(request, username=None):
    if not username:
        username = request.user.get_username()
        if username == '':
            return redirect('home')

    return render(request, 'hott_profile/profile.html')


class ProfileEditView(LoginRequiredMixin, UpdateView):
    template_name = 'shopper_profile/profile_edit.html'
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
        # import pdb; pdb.set_trace()
        form.instance.user.email = form.data['email']
        form.instance.user.first_name = form.data['first_name']
        form.instance.user.last_name = form.data['last_name']
        form.instance.user.save()
        return super().form_valid(form)
