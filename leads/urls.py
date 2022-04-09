from django.urls import path
from .views import *

urlpatterns = [
    path('', Home),
    path('leads/', LeadsLists),
    path('leads/<int:pk>/', LeadsDetails),
    path('leads/create/', CreateLead)
]