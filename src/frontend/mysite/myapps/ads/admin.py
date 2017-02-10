from django.contrib import admin

# Register your models here.
from myapps.ads.models import Category, Food, Meal

admin.site.register(Meal)
admin.site.register(Food)
admin.site.register(Category)
