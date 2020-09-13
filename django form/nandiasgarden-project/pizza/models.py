from django.db import models

# Create your models here.
class Size (models.Model):
   title = models.CharField(max_length=100)

   def __str__(self):
       return self.title

class Pizza (models.Model):
   toping1 = models.CharField(max_length=100)
   toping2 = models.CharField(max_length=100)
   size=models.ForeignKey(Size,on_delete=models.CASCADE)
