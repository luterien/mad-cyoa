from django import forms

from .models import Story, Chapter


class CreateStoryForm(forms.ModelForm):

	class Meta:
		model = Story
		fields = ("name",)


class CreateChapterForm(forms.ModelForm):

	class Meta:
		model = Chapter
		fields = ("name",)

