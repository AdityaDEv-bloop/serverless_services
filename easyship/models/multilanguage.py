from django.db import models
from django.contrib.postgres.fields import ArrayField


class MultiLanguages(models.Model):
    language = models.CharField(max_length=100)
    tag = models.CharField(max_length=100, default="0.01")
    navcontent = ArrayField(base_field=ArrayField(models.CharField()))
    homecontent = ArrayField(base_field=ArrayField(models.CharField()))
    aboutcontent = ArrayField(base_field=ArrayField(models.CharField()))