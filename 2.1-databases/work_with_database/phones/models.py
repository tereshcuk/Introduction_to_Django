from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    id = models.IntegerField(primary_key=True, serialize=False)
    name = models.CharField(max_length=75)
    price = models.FloatField()
    image = models.CharField(max_length=1000)
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField()
    
