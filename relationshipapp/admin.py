from django.contrib import admin
from relationshipapp import models
# Register your models here.
admin.site.register([
    models.Article,
    models.Author,
    models.Publications,
])