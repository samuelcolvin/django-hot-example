from django.db import models

class BasicModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        abstract = True

class Shop(BasicModel):
    post_code = models.CharField(max_length=200)

class Farm(BasicModel):
    area = models.FloatField()

class Field(BasicModel):
    farm = models.ForeignKey(Farm)
    area = models.FloatField()

class Product(BasicModel):
    colors = (('R', 'Red'), 
              ('G', 'Green'), 
              ('B', 'Blue'), 
              ('O', 'Orange'), 
              ('X', 'Other'))
    color = models.CharField(max_length=1, choices=colors)
    farms = models.ManyToManyField(Farm)
    types = ((1, 'Fruit'), (2, 'Veg'), (3, 'Other'))
    type = models.IntegerField(choices=types, default=1)
    weight = models.FloatField(null=True, blank=True)
    luxury = models.BooleanField()

class Basket(models.Model):
    product = models.ForeignKey(Product)
    shop = models.ForeignKey(Shop)
    items = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    sell_by = models.DateField()
    dropped = models.BooleanField()