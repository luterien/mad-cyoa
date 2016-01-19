"""madcyoa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin

from apps.stories.views import ChapterDetail


urlpatterns = [

    url(r'^admin/', admin.site.urls),

    url(r'^test/$', 'apps.main.views.test'),

    url(r'^chapter/(?P<slug>[\w-]+)/$', ChapterDetail.as_view(), name="chapter-detail"),
    url(r'^snippet/(?P<slug>[\w-]+)/edit/$', 'apps.stories.ajax.edit_snippet', name="edit-snippet"),
    
    url(r'^snippet/update/$', 'apps.stories.ajax.update_snippet', name="update-snippet"),
    url(r'^snippet/add_target_choice/$', 'apps.stories.ajax.add_target_choice', name="add-target-choice"),
    url(r'^snippet/add_source_choice/$', 'apps.stories.ajax.add_source_choice', name="add-source-choice"),
    url(r'^snippet/delete_choice/$', 'apps.stories.ajax.delete_choice', name="delete-choice"),
    url(r'^snippet/update_source_choice/$', 'apps.stories.ajax.update_source_choice', name="update-source-choice"),
    url(r'^snippet/update_target_choice/$', 'apps.stories.ajax.update_target_choice', name="update-target-choice"),
    
]
