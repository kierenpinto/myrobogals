from django.db import models
from django.utils import timezone
from myrobogals.rgchapter.models import Chapter
# Create your models here.
class Request(models.Model):
    '''
        ENQUIRY_TYPES = (('TSE','Tech Support Enquiry'), ('RSE','Regional Support Enquiry'), ('CSE','Chapter Support Enquiry')
    ,('BUG','Bug Report'),('MWC','Marketing Website Changes'),('GEN','General Enquiry (choose this option if unsure)'))
    enquiry_type = models.CharField(
        choices= ENQUIRY_TYPES,
    max_length = 100
    )
    '''
    enquiry_type = models.ForeignKey('Department',
                                      on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    chapter = models.ForeignKey(Chapter,on_delete=models.CASCADE)# Add validation for Correct Chapter Options
    message = models.TextField(max_length=100)
    date = models.DateTimeField(default=timezone.now)
    date_resolved = models.DateTimeField(null=True)
    resolved = models.BooleanField(default=False)
    def __str__(self):
        return self.name
    def resolve_enquiry(self):
        self.resolved = True
        self.date_resolved = timezone.now()

class Department(models.Model):
    name = models.CharField(max_length=100)
    destination_email = models.ManyToManyField('Department_Emails')
    send_to_chapters = models.BooleanField(default=False)
    def __str__(self):  # need to add this for when a string method is called on the object
        return self.name

class Department_Emails(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    def __str__(self):  # need to add this for when a string method is called on the object
        return self.name