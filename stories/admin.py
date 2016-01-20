from django.contrib import admin

from .models import Story, Chapter, Snippet, Choice


admin.site.register(Story)
admin.site.register(Chapter)
admin.site.register(Snippet)
admin.site.register(Choice)
