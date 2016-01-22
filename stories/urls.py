from django.conf.urls import *
from django.core.urlresolvers import reverse_lazy

from .views import ChapterDetail


urlpatterns = patterns('',

    # chapters
    url(r'^chapter/(?P<slug>[\w-]+)/$', ChapterDetail.as_view(), name="chapter-detail"),
    url(r'^story/(?P<slug>[\w-]+)/chapter/create/$', 'stories.views.create_chapter', name="create-chapter"),

    # snippets
    url(r'^snippet/(?P<slug>[\w-]+)/edit/$', 'stories.ajax.edit_snippet', name="edit-snippet"),
    url(r'^snippet/(?P<slug>[\w-]+)/update/$', 'stories.ajax.update_snippet', name="update-snippet"),
    url(r'^snippet/create/$', 'stories.ajax.create_snippet', name="create-snippet"),

    # choices
    url(r'^snippet/(?P<slug>[\w-]+)/choices/add/$', 'stories.ajax.add_choice', name="add-choice"),
    url(r'^snippet/(?P<slug>[\w-]+)/choices/delete/$', 'stories.ajax.delete_choice', name="delete-choice"),
    url(r'^snippet/(?P<slug>[\w-]+)/choices/update/$', 'stories.ajax.update_choice', name="update-choice"),

    # stories
    url(r'^story/create/$', 'stories.views.create_story', name="create-story"),
    url(r'^story/(?P<slug>[\w-]+)/$', 'stories.views.story_detail', name="story-detail"),

    # game
    url(r'^story/(?P<slug>[\w-]+)/play/$', 'stories.views.play', name="play"),
    url(r'^story/(?P<slug>[\w-]+)/play/move$', 'stories.ajax.make_play', name="make-play"),

)