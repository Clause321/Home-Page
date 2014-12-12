from django.db import models
from DjangoUeditor.models import UEditorField
from model_template import ProjectLabel
# 
# # Create your models here.
# 
class Tech(ProjectLabel, models.Model):
    pass
 
class Lang(ProjectLabel, models.Model):
    pass
 
class Team(ProjectLabel, models.Model):
    pass

class Tree(models.Model):
    date = models.DateField(max_length=127)
    
    def __str__(self):
        return self.date.strftime('%Y-%m')

class Project(models.Model):
    type = models.CharField(max_length=127)
    title = models.CharField(max_length=127)
    start_date = models.DateField()
    end_date = models.DateField(blank=True)
    inprogress = models.BooleanField(default=False)
    abstract = UEditorField(u'abstract', toolbars="full",
                 imagePath="image/abstract/", filePath="file/abstract/", width=667,
                 upload_settings={"imageMaxSize":1024000},
                 settings={},command=None,
                 blank=True)
    ifdetail = models.BooleanField(default=False)
    detail = UEditorField(u'detail', toolbars="full",
                 imagePath="image/detail/", filePath="file/detail/", width=1200,
                 upload_settings={"imageMaxSize":1024000},
                 settings={},command=None,
                 blank=True)
    tech = models.ManyToManyField(Tech, blank=True)
    langs = models.ManyToManyField(Lang, blank=True)
    team = models.ManyToManyField(Team, blank=True)
    tree = models.ForeignKey(Tree, blank=True, null=True)
    side_image = models.ImageField(upload_to='image/side/', blank=True, null=True)
#     front_image = models.ImageField(upload_to='image/front/', blank=True, null=True)
 
    def __str__(self):
        return self.title
     
    def save(self, force_insert=False, force_update=False, using=None, 
        update_fields=None):
        if not self.inprogress:
            self.tree = Tree.objects.get(date=self.end_date)
        return models.Model.save(self, force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)
