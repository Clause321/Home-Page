from django.shortcuts import render_to_response
from models import Slide

# Create your views here.

def home(request):
    slides = Slide.objects.filter(active=True)[0:4]
    return render_to_response('home.html', locals())

def about(request):
    return render_to_response('about.html')

def blog(request):
    return render_to_response('blog.html', locals())