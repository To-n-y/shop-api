from django.db import models


class Review(models.Model):
    r_id = models.AutoField(primary_key=True)
    r_item = models.ForeignKey('Item', on_delete=models.CASCADE)
    r_text = models.TextField(default='')
    r_rating = models.IntegerField(default=0)
    r_created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.r_text


class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=200)
    item_date = models.DateTimeField('date published')
    item_price = models.IntegerField(default=0)
    item_description = models.CharField(max_length=200)
    item_image = models.ImageField(upload_to='shop/static/shop/images/', default='images/None/no-img.jpg')
    item_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.item_name
