from django.contrib import admin
from django.urls import path,include
from . import views
from django.urls import path


urlpatterns = [

   path("api/swapi/get",views.get_request,name="get_request"),
    path("api/swapi/post",views.post_request,name="post_request"),
    path("api/swapi/put/",views.put_request,name="put_request"),
    path("api/swapi/delete/<int:id>/",views.delete_request,name="delete_request"),
]
