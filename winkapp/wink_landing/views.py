from django.shortcuts import render
from django.views.generic import ListView, CreateView
from . import models
# Create your views here.


def index(request):
    feeds = getUserFeed(request)    
    comments = getComments(request)
    return render(request, 'wink_landing/base.html', {'feeds':feeds,'comments':comments})



class FeedList(ListView):
    template_name = "wink_landing/base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #TODO: Need to add a filter based on loged in user 
        context["feeds"] = models.UserFeed.all()        
        return context

class CreatePost(CreateView):
    template_name='wink_landing/base.html'
    redirect_field_name ='wink_landing/base.html'
    model = models.UserFeed
    fields = ('feed_text',)
    def form_valid(self, form):
        form.instance.user = self.request.user
        print('loggedin user',self.request.user)
        return super().form_valid(form)
    
    def form_invalid(self, form):
        print("Form is invalid")
        values = form.cleaned_data.get("symptoms")
        print(form.errors)
        return super().form_invalid(form)

def getUserFeed(request):
    return models.UserFeed.objects.filter(user = request.user)

def getComments(request):
    return models.Comment.objects.filter(user = request.user)