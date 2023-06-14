from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.files import ImageField

# Create your models here.
""" creamos un modelo para mi portfolio """

""" asi que guardamos datos de mis proyectos """

class Project(models.Model):
    title = CharField(max_length=100)
    description = CharField(max_length=250)
    image = ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)