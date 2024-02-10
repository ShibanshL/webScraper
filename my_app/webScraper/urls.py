from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.myGetReq),
    path('symbols/',views.test_List),
    path('test/<key_id>/',views.paramsSent),
    path('symbols/',views.getArray)
]
