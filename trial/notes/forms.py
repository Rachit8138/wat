from django import forms

from django.core.exceptions import ValidationError
from .models import Notes

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title','text')
        # labels = {'title':'Title', 'text':'Add your description here!'}
        # widgets = {'title':forms.TextInput(attrs={'class':'form-control'}),
        #            'text':forms.Textarea(attrs={'class':'form-control'}),}

    def clean_title(self):
        title = self.cleaned_data['title'].strip().lower()
        if 'django'.lower() not in title:
            raise ValidationError('We only accept notes about Django!!')
        return title
