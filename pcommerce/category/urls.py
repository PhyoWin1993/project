from django.urls import path
from .views import *

urlpatterns = {
    path('',home,name="cat-home"),
    path('about/',about,name="about-cat")
}