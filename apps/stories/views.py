import json

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic.detail import DetailView

from .models import Chapter, Snippet, Choice


class ChapterDetail(DetailView):
    model = Chapter
    template_name = "chapter_detail.html"


