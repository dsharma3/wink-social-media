from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('new/', views.CreatePost.as_view(), name='createfeed'),
    path('search/',views.SearchFriends.as_view(), name='searchfriends'),
]
