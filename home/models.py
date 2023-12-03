from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length = 500)
    rank = models.IntegerField()
    image = models.ImageField(upload_to='media' , default="")
    def __str__(self):
        return self.name

class Featured(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to= 'media')


    def __str__(self):
        return self.name

LABELS = (('' , 'default') , ('trending' , 'trending') , ('most played' , 'most played'))
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    discounted_price = models.IntegerField(default = 0)
    image = models.ImageField(upload_to='media')
    description = models.TextField(blank = True)
    game_id = models.CharField(max_length = 100)
    category = models.ManyToManyField(Category)

    tags = models.CharField(max_length = 200)
    labels = models.CharField(choices = LABELS , max_length=50 , blank = True)

    def __str__(self):
        return self.name








