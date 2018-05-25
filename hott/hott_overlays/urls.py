# from django.shortcuts import render
from django.urls import path
# from .views import CrimeView, EntertainmentView, EventView, ArtView, DirtinessView
from django.views.generic import TemplateView


urlpatterns = [
    # path('crime/', CrimeView.as_view(), name='crimemap'),
    # path('entertainment/', EntertainmentView.as_view(), name='entertainmentmap'),
    # path('events/', EventView.as_view(), name='eventsmap'),
    # path('art/', ArtView.as_view(), name='artmap'),
    # path('complaints/', DirtinessView.as_view(), name='dirtinessmap'),
    path('crime/', TemplateView.as_view(template_name="crime.html"), name='crimemap'),
    path('entertainment/', TemplateView.as_view(template_name="entertainment.html"), name='entertainmentmap'),
    path('events/', TemplateView.as_view(template_name="events.html"), name='eventsmap'),
    path('art/', TemplateView.as_view(template_name="art.html"), name='artmap'),
    path('complaints/', TemplateView.as_view(template_name="dirtiness.html"), name='dirtinessmap'),
]