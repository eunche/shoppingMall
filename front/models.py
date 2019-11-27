from django.db import models

# Create your models here.

class Post(models.Model) :
    title = models.CharField(max_length = 200)
    price = models.IntegerField()
    image = models.ImageField(upload_to='images/')
    ctg= (
    (5, '외투'),

    (4, '상의'),

    (3, '하의'),

    (2, '신발'),

    (1, '모자'),
    )
    category = models.FloatField(
        choices=ctg,
        default= 5
    )

    def __str__(self) :
        return self.title