from django.contrib import admin
from . import models


admin.site.register(models.Animal)
admin.site.register(models.Owner)
