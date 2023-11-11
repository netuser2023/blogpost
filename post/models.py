from django.db import models

# Create your models here.

class Post(models.Model):
      title = models.CharField(max_length=60, null=False, blank=False)
      postid = models.IntegerField(primary_key=True)
      createdate = models.DateField(null=True)