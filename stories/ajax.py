import json

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Snippet, Choice, Chapter
from .game import Game


def make_play(request):

    s_id = request.POST.get("selected_id")
    c_id = request.POST.get("chapter_id")

    chapter = Chapter.objects.get(id=int(c_id))
    snippet = Snippet.objects.get(id=int(s_id))

    game = Game(request, chapter=chapter)
    game.move(int(s_id))

    return render(request, "stories/inc/game_content.html", {"snippet": snippet})


def edit_snippet(request, slug):

    snippets = Snippet.objects.filter()

    snippet = get_object_or_404(Snippet, slug=slug)

    ctx = {
        "snippet" : snippet,
        "snippets" : Snippet.objects.filter(chapter=snippet.chapter)
    }

    return render(request, "stories/edit_snippet.html", ctx)


def update_snippet(request):

    s_id = request.POST.get("snippet_id")
    s_content = request.POST.get("content")
    s_name = request.POST.get("snippet_name")

    s = Snippet.objects.get(id=int(s_id))
    s.text = s_content or s.text
    s.name = s_name or s.name
    s.save()

    return HttpResponse("OK")


def add_target_choice(request):
    
    snippet_id = request.POST.get("snippet_id")
    choice_name = request.POST.get("choice_name")

    base_s = Snippet.objects.get(id=int(snippet_id))

    choice = Choice(source=base_s)
    choice.save()

    return render(request, "include/target_choices.html", {
        "targets": base_s.targets.all(),
        "snippets": Snippet.objects.filter(chapter=base_s.chapter),
        })


def add_source_choice(request):
    
    snippet_id = request.POST.get("snippet_id")
    choice_name = request.POST.get("choice_name")

    base_s = Snippet.objects.get(id=int(snippet_id))

    choice = Choice(target=base_s)
    choice.save()

    return render(request, "include/source_choices.html", {
        "sources": base_s.sources.all(),
        "snippets": Snippet.objects.filter(chapter=base_s.chapter),
        })


def update_source_choice(request):

    choice_id = request.POST.get("choice_id")
    source_id = request.POST.get("source_id")
    choice_text = request.POST.get("choice_text")

    source = Snippet.objects.get(id=int(source_id))
    choice = Choice.objects.get(id=int(choice_id))

    choice.source_id = int(source_id)
    choice.text = choice_text
    choice.save()

    return render(request, "include/source_choices.html", {
        "sources": choice.target.sources.all(),
        "snippets": Snippet.objects.filter(chapter=source.chapter),
        })


def update_target_choice(request):

    choice_id = request.POST.get("choice_id")
    target_id = request.POST.get("target_id")
    choice_text = request.POST.get("choice_text")

    target = Snippet.objects.get(id=int(target_id))
    choice = Choice.objects.get(id=int(choice_id))

    choice.target_id = int(target_id)
    choice.text = choice_text
    choice.save()

    return render(request, "include/target_choices.html", {
        "targets": choice.source.targets.all(),
        "snippets": Snippet.objects.filter(chapter=target.chapter),
        })


def delete_choice(request):

    choice_id = request.POST.get("choice_id")

    Choice.objects.get(id=int(choice_id)).delete()

    return HttpResponse("OK")


def create_snippet(request):

    chapter_id = request.POST.get("chapter_id")

    chapter = Chapter.objects.get(id=int(chapter_id))

    snippet = Snippet.objects.create(chapter=chapter)
    snippet.name = "Empty Snippet " + str(snippet.pk)
    snippet.save()

    return HttpResponse("OK")


