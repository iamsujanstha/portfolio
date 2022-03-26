from django.db import models
import uuid

# Create your models here.
class tag(models.Model):
    tag = models.CharField(max_length=100)
    created_time = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.tag

class skill(models.Model):
    skill = models.CharField(max_length=50)
    created_time = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.skill
    
    
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    thumbnail = models.ImageField(null = True, blank = True,  default = 'default.png')
    skill  = models.ManyToManyField(skill,blank=True, related_name='projects')
    tag = models.ManyToManyField(tag,blank=True, related_name='tagname')
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    source_link = models.CharField(max_length=1000, null=True, blank = True)


    def __str__(self):
        return self.title
    
