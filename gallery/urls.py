from django.urls import path
from . import views

urlpatterns = [
    path('caps/', views.caps, name='caps'),
    path('wavers/', views.wavers, name='wavers'),
    path('delikat/', views.delikat, name='delikat'),
    path('astro/', views.astro, name='astro'),
    path('art/', views.art, name='art'),
    path('site/', views.site, name='site'),
]