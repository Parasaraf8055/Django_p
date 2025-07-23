from django.db import models

# Create your models here.


class Blogs(models.Model):
    date=models.DateField(auto_now=False, auto_now_add=False)
    time=models.TimeField(auto_now=False, auto_now_add=False)
    content=models.CharField(max_length=5000)
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.content
    



