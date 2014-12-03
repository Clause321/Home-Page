from django.contrib import admin
from models import Project, Team, Tech, Lang, Tree

# Register your models here.

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    filter_horizontal = ("langs", "tech", "team",)
    
@admin.register(Team, Tech, Lang, Tree)
class LabelAdmin(admin.ModelAdmin):
    pass
