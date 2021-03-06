# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from stories import views

from django.conf.urls import url

urlpatterns = [

        url(r'^addstory/$', views.addstory),
        url(r'^story/(?P<story>\d+)/$', views.Source),
        url(r'^edit_story/(?P<edit_id>\d+)/$', views.edit_story,
            name="editstory"
            ),
        url(r'^delete_story/(?P<delete_id>\d+)/$', views.delete_story),
        url(r'^search/$', views.search),
        url(r'^delete_company/(?P<delete_id>\d+)/(?P<company_name>\w+)/$',
            views.delete_company),
]