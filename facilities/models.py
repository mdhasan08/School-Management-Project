from django.db import models

# Create your models here.
class Facilities(models.Model):
    background_image = models.ImageField(upload_to='facilities/background_image')
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=200)

    def __str__(self):
        return '( '+self.title+' ) - '+self.description