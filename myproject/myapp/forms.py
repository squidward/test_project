# -*- coding: utf-8 -*-
from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Document, DocAndAttr2, RedactorText
from ckeditor.fields import RichTextFormField
from redactor.widgets import RedactorEditor
class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file'

    )

class DocAndAttrForm(forms.ModelForm):

    class Meta:
        model = DocAndAttr2


class MyTextForm(forms.Form):
    content = RichTextFormField()

class RedactorTextForm(forms.ModelForm):

    class Meta:
        model = RedactorText
        widgets = {
            'content': RedactorEditor(redactor_options={'buttons': ['html', '|', 'formatting', '|', 'bold', 'italic']}),
        }


