from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from myrobogals.auth.models import Group

def home(request):
	return render_to_response('home.html', {}, context_instance=RequestContext(request))

def welcome(request, chapterurl):
	chapter = get_object_or_404(Group, myrobogals_url__exact=chapterurl)
	return render_to_response('welcome.html', {'chapter': chapter}, context_instance=RequestContext(request))

def credits(request):
	return render_to_response('credits.html', {}, context_instance=RequestContext(request))

def support(request):
	return render_to_response('support.html', {}, context_instance=RequestContext(request))

def files(request):
	return render_to_response('files.html', {}, context_instance=RequestContext(request))
