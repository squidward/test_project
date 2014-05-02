# -*- coding: utf-8 -*-
from django.db import models
from ckeditor.fields import RichTextField
from redactor.fields import RedactorField
class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')

    def __unicode__(self):
        return self.docfile.name

class DocAndAttr2(models.Model):
    name = models.CharField(max_length=150)
    document = models.FileField(upload_to='documents/%Y/%m/%d')

    def __unicode__(self):
        return self.name

class MyText(models.Model):
    content = RichTextField()

class RedactorText(models.Model):
    content = RedactorField(allow_file_upload=True)
