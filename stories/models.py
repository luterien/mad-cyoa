from __future__ import unicode_literals

from django.db import models
from django.conf import settings

from autoslug import AutoSlugField


class Displayable(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    slug = AutoSlugField(populate_from="name", unique=True, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    sort_order = models.IntegerField(default=1)

    class Meta:
        abstract = True
        ordering = ("sort_order",)

    def __unicode__(self):
        return u"%s" % self.name


class Story(Displayable):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)

    @property
    def first_chapter(self):
        return self.related_chapters.all()[0]


class Chapter(Displayable):
    story = models.ForeignKey(Story, related_name="related_chapters")

    @property
    def first_snippet(self):
        try:
            return self.related_snippets.get(starting_point=True)
        except:
            return self.related_snippets.order_by("-id")[0]


class Snippet(Displayable):
    chapter = models.ForeignKey(Chapter, related_name="related_snippets")

    is_completed = models.BooleanField(default=False)
    is_failed = models.BooleanField(default=False)

    starting_point = models.BooleanField(default=False)
    checkpoint = models.BooleanField(default=False)


class Choice(Displayable):
    source = models.ForeignKey(Snippet, related_name="targets", null=True, blank=True)
    target = models.ForeignKey(Snippet, related_name="sources", null=True, blank=True)

