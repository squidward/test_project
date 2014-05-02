# -*- coding: utf-8 -*-
import json
import logging
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from myproject.myapp.models import Document, DocAndAttr2, MyText, RedactorText
from myproject.myapp.forms import DocumentForm, DocAndAttrForm, MyTextForm, RedactorTextForm

def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()
            dict = {'names':newdoc.docfile.name,
                    'urls': newdoc.docfile.url}
            return  HttpResponse(json.dumps(dict), mimetype="application/json")

    else:
        form = DocumentForm() # A empty, unbound form

    documents = Document.objects.all()

    return render_to_response(
        'myapp/list.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )

def show(request):
    if request.method == 'POST':
        form = DocAndAttrForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = DocAndAttr2(name = request.POST['name'] ,document = request.FILES['document'])
            newdoc.save()
            dict = {'names':newdoc.name,
                    'urls': newdoc.document.url}
            return  HttpResponse(json.dumps(dict), mimetype="application/json")

    else:
        form = DocAndAttrForm() # A empty, unbound form

    documents = DocAndAttr2.objects.all()

    return render_to_response(
        'myapp/list2.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )

def mytext(request):
    if request.method == 'POST':
        form = MyTextForm(request.POST)
        if form.is_valid():
            newdoc = MyText(content = request.POST['content'])
            newdoc.save()
            return  redirect('/myapp/mytext/')

    else:
        form = MyTextForm() # A empty, unbound form

    documents = MyText.objects.all()

    return render_to_response(
        'myapp/mytext.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )

def redactortext(request):
    if request.method == 'POST':
        form = RedactorTextForm(request.POST)
        if form.is_valid():
            newdoc = RedactorText(content = request.POST['content'])
            newdoc.save()
            return  redirect('/myapp/redtext/')

    else:
        form = RedactorTextForm() # A empty, unbound form

    documents = RedactorText.objects.all()

    return render_to_response(
        'myapp/redtext.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )