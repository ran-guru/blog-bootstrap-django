from django.contrib import admin

# Register your models here.
from blog import models


admin.site.register(models.Category)
admin.site.register(models.Autor)
admin.site.register(models.Post)
