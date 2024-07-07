from django.urls import path
from . import views

urlpatterns = [
    path('workshops', views.view_workshops, name='view_workshops'),
    path('workshopapply', views.workshopapply, name='workshopapply'),
    path('', views.thankyou, name='thankyou'),
]
