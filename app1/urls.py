from app1.views import *
from django.urls import path
app_name='danger'
urlpatterns=[
    path('rolex/',rolex,name='rolex'),
    path('santaanam/',santaanam,name='santaanam')
]