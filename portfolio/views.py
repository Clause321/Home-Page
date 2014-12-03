from django.shortcuts import render_to_response
from models import Project, Tree

# Create your views here.

def portfolio(request):
    web_projects = Project.objects.filter(type = "web")
    android_projects = Project.objects.filter(type = "android")
    embedded_projects = Project.objects.filter(type = "embedded")
    trees13 = Tree.objects.all()[0:5]
    trees14 = Tree.objects.all()[5:17]
    return render_to_response('portfolio.html', locals())