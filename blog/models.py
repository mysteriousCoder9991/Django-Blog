from django.db import models

# Create your models here.
class Blog(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    content=models.TextField()
    short_desc=models.CharField(max_length=150)
    slug=models.CharField(max_length=50)
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    