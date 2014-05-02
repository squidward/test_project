import lemon

from django.contrib import admin
from .models import Document, RedactorText
from redactor.widgets import RedactorEditor
from django import forms

class DocumentAdmin(lemon.ModelAdmin):
    class Meta:
        model = Document

class RedactorTextAdminForm(forms.ModelForm):
    class Meta:
        model = RedactorText
        widgets = {
            'content': RedactorEditor(),
        }

class RedactorTextAdmin(lemon.ModelAdmin):
    form = RedactorTextAdminForm
#admin.site.register(Document)
#admin.site.register(RedactorText,RedactorTextAdmin )
lemon.site.register(Document,DocumentAdmin)
lemon.site.register(RedactorText,RedactorTextAdmin)
