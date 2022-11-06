from django.db import models


class Contact(models.Model):
    email_date = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50, null=False, blank=False)
    surname = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    subject = models.CharField(max_length=254, null=True, blank=True)
    query = models.TextField(null=True, blank=True)
    hearfrom = models.CharField(max_length=254, null=True, blank=True)
