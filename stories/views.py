import json

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic.detail import DetailView

from .models import Chapter, Snippet, Choice, Story


class ChapterDetail(DetailView):
    model = Chapter
    template_name = "chapter_detail.html"


def story_detail(request, slug):

	"""
		display story details
		todo: add permission checks & redesign the template
	"""

	story = get_object_or_404(Story, slug=slug)

	return render(request, "stories/story_detail.html", {"story": story})



