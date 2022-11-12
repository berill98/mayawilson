from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('first_name', 'surname', 'email', 'subject',
                  'query', 'hearfrom',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'first_name': 'First name',
            'surname': 'Last name',
            'email': 'Your email address',
            'subject': "Wedding/Family session",
            'query': "Share your vision for your photoshoot, any ideas you have and tell me a little bit about you",
            'hearfrom': "Instagram, Facebook",
        }
        self.fields['first_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'rate_us':
                if self.fields[field].required:
                    placeholder = placeholders[field]
                    self.fields[field].widget.attrs['required'] = True
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
