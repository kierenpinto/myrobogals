from django.shortcuts import render
from django.utils import timezone
# Create your views here.
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView
from .models import Request, Department, Department_Emails
from .forms import RequestForm, RequestForm_Edit
from django.shortcuts import get_object_or_404, redirect
from myrobogals.rgmessages.models import EmailMessage, EmailRecipient
from myrobogals.rgchapter.models import Chapter
from myrobogals.rgprofile.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
#Dependant Email Function
def email_message(http_request_obj,request_pk):
    '''
    if(obj.send_to_chapters):
        chapters = Chapter.objects.all()
        chapter_email = []
        for chapter in chapters:
            chapt_email.append(chapter.)
            '''
    request_object = Request.objects.get(pk = request_pk)
    dept = Department.objects.get(name=request_object.enquiry_type)
    email_recipients = Department_Emails.objects.filter(department__pk=dept.pk)
    email_body = request_object.message
    email_subject = request_object.name + " " + str(request_object.date) + " " + str(request_object.enquiry_type)
    message = EmailMessage()
    message.subject = email_subject
    #message.subject = "test subject"
    html_body = render(http_request_obj,'rgsupport/email_message_template.html', {'email_body':email_body,'email_subject':email_subject})
    message.body = html_body.content
    message.from_name = "myRobogals"
    message.from_address = "my@robogals.org"
    message.reply_address = "my@robogals.org"
    message.sender = User.objects.get(username='edit')
    message.html = True
    message.email_type = 0

    # Message is set to WAIT mode
    message.status = -1
    message.save()

    # Creates a list of all email addresses to notify
    if email_recipients != None:
        # Email to all addresses that need to be notified
        for email_recipient in email_recipients:
            recipient = EmailRecipient()
            recipient.message = message
            recipient.user = User.objects.get(username='edit')
            '''set recipient as user object
                edit which '''
            recipient.to_name = request_object.name
            recipient.to_address = email_recipient.email
            recipient.save()
            message.status = 0
            message.save()

#      SEND MESSAGE FUNCTION


def get_requestform(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            reqform = form.save(commit=False)
            reqform.date = timezone.now()
            reqform.resolved = False
            reqform.save()
            print reqform.pk
            email_message(request, reqform.pk)
            return redirect('rgsupport:thanks')
    else:
        form = RequestForm()

    return render(request, 'rgsupport/support_form.html', {'form':form})

@login_required
def get_editform(request, pk):
    if (request.user.is_superuser):
        query = get_object_or_404(Request, pk=pk)
        if request.method == "POST":
            form = RequestForm(request.POST, instance=query)
            if form.is_valid():
                reqform = form.save(commit=False)
                reqform.date = timezone.now()
                reqform.resolved = False
                reqform.save()
                return redirect('rgsupport:admin_view', pk=query.pk)
        else:
            form = RequestForm_Edit(instance=query)
        return render(request, 'rgsupport/admin_edit.html', {'form': form, 'query':query})
    else:
        return render(request, 'rgsupport/admin_reject.html')
@login_required
def set_resolved(request, pk):
    if (request.user.is_superuser):
        query = get_object_or_404(Request, pk=pk)
        query.resolve_enquiry()
        query.save()
        return redirect('rgsupport:admin_view', pk=query.pk)
    else:
        return render(request, 'rgsupport/admin_reject.html')

def get_thanks(request):
    return render(request,'rgsupport/thanks.html')

class IssuesList(ListView):
    model = Request
    template_name = 'rgsupport/admin.html'
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(IssuesList, self).dispatch(*args, **kwargs)

    @method_decorator(login_required)
    def get(self, *args, **kwargs):
        if (self.request.user.is_superuser):
            return super(IssuesList, self).get(*args, **kwargs)
        else:
            return render(self.request,'rgsupport/admin_reject.html')

class IssueDetail(DetailView):
    model = Request
    template_name = 'rgsupport/admin_detail.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(IssueDetail, self).dispatch(*args, **kwargs)

    @method_decorator(login_required)
    def get(self, *args, **kwargs):
        if (self.request.user.is_superuser):
            return super(IssueDetail, self).get(*args, **kwargs)
        else:
            return render(self.request,'rgsupport/admin_reject.html')
