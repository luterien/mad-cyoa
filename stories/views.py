import json

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from .models import Chapter, Snippet, Choice, Story
from .forms import CreateChapterForm, CreateStoryForm


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


def create_chapter(request, story_id):

	if request.method == "POST":
		story = get_object_or_404(Story, id=story_id)
		form = CreateChapterForm(request.POST)

		if form.is_valid():
			name = form.cleaned_data["name"]
			chapter = Chapter.objects.create(story=story, name=name)
			return redirect(reverse("my-stories"))
	else:
		form = CreateChapterForm()

	return render(request, "stories/create_chapter.html", {"form": form})


def create_story(request):

	if request.method == "POST":
		form = CreateStoryForm(request.POST)

		if form.is_valid():
			name = form.cleaned_data["name"]
			story = Story.objects.create(name=name, owner=request.user)
			return redirect(reverse("my-stories"))
	else:
		form = CreateStoryForm()

	return render(request, "stories/create_story.html", {"form": form})


def play(request, story_id):
	""" initialize a new game """
	from .game import Game

	story = get_object_or_404(Story, id=story_id)

	game = Game(request, story)

	if request.GET.get("reset"):
		game.reset()
		return redirect(reverse("play", kwargs={"story_id": story_id}))
	
	game.resume()

	snippet = Snippet.objects.get(
		id=int(game.get_current_snippet_id())
		)

	return render(request, "stories/game.html", {"snippet": snippet})
