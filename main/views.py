from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse


def test(request):
	return render(request, "test.html", {"data": "unknown!"})


def index(request):

	if request.user.is_authenticated():
		return redirect(reverse("my-stories"))

	return render(request, "main/index.html", {})

