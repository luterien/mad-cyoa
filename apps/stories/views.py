import json

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic.detail import DetailView

from .models import Chapter, Snippet, Choice


class ChapterDetail(DetailView):
	model = Chapter
	template_name = "chapter_detail.html"



def edit_snippet(request, slug):

	snippets = Snippet.objects.all()

	snippet = get_object_or_404(Snippet, slug=slug)

	ctx = {
		"snippet" : snippet,
		"snippets" : snippets
	}

	return render(request, "edit_snippet.html", ctx)


def update_snippet(request):

	s_id = request.POST.get("snippet_id")
	s_content = request.POST.get("content")

	s = Snippet.objects.get(id=int(s_id))
	s.text = s_content
	s.save()

	return HttpResponse(json.dumps({}))


def add_target_choice(request):
	
	snippet_id = request.POST.get("snippet_id")
	choice_name = request.POST.get("choice_name")
	target_s_id = request.POST.get("target_s_id")

	base_s = Snippet.objects.get(id=int(snippet_id))
	#target_s = Snippet.objects.get(id=int(target_s_id))

	choice = Choice(source=base_s)
	choice.save()

	return render(request, "include/target_choices.html", {
		"sources": base_s.sources.all(),
		"snippets": Snippet.objects.all(),
		})



def update_choice(request):
	pass

