from django.shortcuts import render
from django.views.generic import ListView, CreateView, View
from . import models
import datetime
from django.urls import reverse
# Create your views here.


def index(request):
    feeds = getUserFeed(request)    
    return render(request, 'wink_landing/base.html', {'feeds':feeds})


class CreatePost(CreateView):
    template_name='wink_landing/base.html'
    model = models.UserFeed

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
