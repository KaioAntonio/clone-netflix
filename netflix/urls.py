
from django.urls import path

from netflix import views

urlpatterns = [
    path('',views.index, name='index'),
    path('login/',views.login,name='login')
]
