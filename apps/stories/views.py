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

    base_s = Snippet.objects.get(id=int(snippet_id))

    choice = Choice(source=base_s)
    choice.save()

    return render(request, "include/target_choices.html", {
        "targets": base_s.targets.all(),
        "snippets": Snippet.objects.all(),
        })


def add_source_choice(request):
    
    snippet_id = request.POST.get("snippet_id")
    choice_name = request.POST.get("choice_name")

    base_s = Snippet.objects.get(id=int(snippet_id))

    choice = Choice(target=base_s)
    choice.save()

    return render(request, "include/source_choices.html", {
        "sources": base_s.sources.all(),
        "snippets": Snippet.objects.all(),
        })


def update_source_choice(request):

    choice_id = request.POST.get("choice_id")
    source_id = request.POST.get("source_id")
    choice_text = request.POST.get("choice_text")

    choice = Choice.objects.get(id=int(choice_id))

    choice.source_id = int(source_id)
    choice.text = choice_text
    choice.save()

    return HttpResponse("OK")


def update_target_choice(request):

    choice_id = request.POST.get("choice_id")
    target_id = request.POST.get("target_id")
    choice_text = request.POST.get("choice_text")

    choice = Choice.objects.get(id=int(choice_id))

    choice.target_id = int(target_id)
    choice.text = choice_text
    choice.save()

    return HttpResponse("OK")


def delete_choice(request):

    choice_id = request.POST.get("choice_id")

    Choice.objects.get(id=int(choice_id)).delete()

    return HttpResponse("OK")

