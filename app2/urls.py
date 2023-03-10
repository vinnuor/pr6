from app2.views import *
from django.urls import path
app_name='hero'
urlpatterns=[
    path('vikram/',vikram,name='vikram')
]