from django.shortcuts import render
from django.views.generic import ListView, CreateView, View
from . import models
import datetime
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.

@login_required
def index(request):
    feeds = getUserFeed(request)    
    return render(request, 'wink_landing/landing.html', {'feeds':feeds})


class CreatePost(CreateView, LoginRequiredMixin):
    template_name='wink_landing/base.html'
    model = models.UserFeed
    login_url = '/login/'
    fields = ('feed_text',) 

    def form_valid(self, form):        
        form.instance.user = self.request.user
        form.instance.createddate = datetime.datetime.now()
        print('loggedin user',self.request.user)
        return super().form_valid(form)
    
    def form_invalid(self, form):
        print("Form is invalid")
        values = form.cleaned_data.get("symptoms")
        print(form.errors)
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse("home")

def getUserFeed(request):    
    return models.UserFeed.objects.prefetch_related("comments").filter(user = request.user).order_by('-createddate')


class SearchFriends(View):
    fields = ('search')
    model = User
    template_name = 'wink_landing/friend_search.html'
    def get(self, request, *args, **kwargs):
        return HttpResponse('GET request!')

    def post(self, request, *args, **kwargs):
        friend = request.POST.get('search')
        search_users = User.objects.filter(username__icontains = friend)    
        print('length',len(search_users) )
        return render(request,'wink_landing/friend_search.html',context={'search_users':search_users})

    