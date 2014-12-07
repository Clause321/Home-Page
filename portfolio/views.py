from django.shortcuts import render_to_response
from models import Project, Tree

# Create your views here.

def portfolio(request):
    web_projects = Project.objects.filter(type = "web").order_by("-end_date")
    android_projects = Project.objects.filter(type = "android").order_by("-end_date")
    embedded_projects = Project.objects.filter(type = "embedded").order_by("-end_date")
    trees13 = Tree.objects.all()[0:5]
    trees14 = Tree.objects.all()[5:17]
    w_sides = (Tree.objects.all().count() - 13 + 1) * 76
    w_full = 1000 + w_sides
    w_more = 1000 + 2 * w_sides
    return render_to_response('portfolio.html', locals())

def show(request, i):
    project = Project.objects.get(id=i)
    return render_to_response('detail.html', locals())