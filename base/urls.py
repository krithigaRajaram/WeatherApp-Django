from django.urls import path
from . import views
urlpatterns=[
    path('delete_city/', views.delete_city, name='delete_city'),
    path('',views.index,name='home'),
]