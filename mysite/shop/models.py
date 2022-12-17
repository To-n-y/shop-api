from django.db import models


class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=200)
    item_date = models.DateTimeField('date published')
    item_price = models.IntegerField(default=0)
    item_description = models.CharField(max_length=200)
    item_image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.item_name
