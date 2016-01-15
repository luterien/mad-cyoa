from __future__ import unicode_literals

from django.db import models


class Displayable(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    slug = models.SlugField(max_length=100, null=True, blank=True)
    text = models.TextField()
    sort_order = models.IntegerField(default=1)

    class Meta:
    	abstract = True
    	ordering = ("sort_order",)

    def __unicode__(self):
    	return u"%s" % self.name


class Story(Displayable):
	pass


class Chapter(Displayable):
	story = models.ForeignKey(Story, related_name="related_chapters")


class Snippet(Displayable):
	chapter = models.ForeignKey(Chapter, related_name="related_snippets")

	is_completed = models.BooleanField(default=False)
	is_failed = models.BooleanField(default=False)

	starting_point = models.BooleanField(default=False)
	checkpoint = models.BooleanField(default=False)


class Choice(Displayable):
	source = models.ForeignKey(Snippet, related_name="sources", null=True, blank=True)
	target = models.ForeignKey(Snippet, related_name="targets", null=True, blank=True)

