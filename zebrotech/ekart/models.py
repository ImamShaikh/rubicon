from django.db import models

# Create your models here.
class product(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    price = models.IntegerField()
    quantity = models.IntegerField()
    image = models.ImageField(upload_to="post_images/", null=True)

    def __str__(self):
        return self.name
        

    