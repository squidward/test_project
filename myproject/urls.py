# -*- coding: utf-8 -*-
import lemon
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^myapp/', include('myproject.myapp.urls')),
	(r'^$', RedirectView.as_view(url='/myapp/list/')),
	(r'^ckeditor/', include('ckeditor.urls')),
	(r'^redactor/', include('redactor.urls')),# Just for ease of use.
    (r'^admin/', include(lemon.site.urls)),
)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

