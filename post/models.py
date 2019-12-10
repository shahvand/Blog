from django.db import models
from django.urls import reverse
# Create your models here.
class post(models.Model):
    name = models.CharField(max_length=150)
    tel = models.CharField(max_length=150)
    department = models.CharField(max_length=150)
    sakhteman = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("post:detail",kwargs={'id':self.id})
    
    def get_update_url(self):
        return reverse("post:update",kwargs={'id':self.id})    

    def get_delete_url(self):
        return reverse("post:delete",kwargs={'id':self.id})
   