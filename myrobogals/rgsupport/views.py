from django.shortcuts import render
from django.utils import timezone
# Create your views here.
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import ListView
from .models import Request as issueRequest
from .forms import RequestForm

def get_requestform(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            reqform = form.save(commit=False)
            reqform.date = timezone.now()
            reqform.resolved = False
            reqform.save()
            return HttpResponseRedirect(reverse('rgsupport:thanks'))
    else:
        form = RequestForm()

    return render(request, 'support_form.html', {'form':form})

def get_thanks(request):
    return render(request,'thanks.html')

