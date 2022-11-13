import uuid
from django.db import models


class Contact(models.Model):

    class Meta:
        verbose_name_plural = 'Queries'

    query_number = models.CharField(max_length=32, null=False,
                                    editable=False, default='')
    email_date = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50, null=False, blank=False)
    surname = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    subject = models.CharField(max_length=254, null=True, blank=True)
    query = models.TextField(null=True, blank=True)
    hearfrom = models.CharField(max_length=254, null=True, blank=True)

    def _generate_query_number(self):
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        if not self.query_number:
            self.query_number = self._generate_query_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.query_number
