from django.shortcuts import render_to_response

# Create your views here.

def home(request):
    return render_to_response('home.html')

def about(request):
    return render_to_response('about.html')

def blog(request):
    # blogs = Blog.objects.all()
    return render_to_response('blog.html', locals())