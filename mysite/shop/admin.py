from django.contrib import admin

from .models import Item, Review

admin.site.register(Item)
admin.site.register(Review)