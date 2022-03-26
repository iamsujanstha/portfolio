from unicodedata import name
from django.urls import path
from webapp import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about-me/', views.about, name = 'about'),
    path('portfolio/', views.portfolio, name = 'portfolio'),
    path('contact-me/', views.contact, name = 'contact'),
]