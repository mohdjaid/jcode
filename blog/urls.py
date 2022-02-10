import imp
from unicodedata import name
from xml.dom.minidom import Document
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="blog"),
    path("about",views.about,name="about"),
    path("contact",views.contact,name="contact"),
    path("post/<int:id>",views.post,name="post"),

] 
