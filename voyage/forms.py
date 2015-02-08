from django.forms import ModelForm, Textarea
from django import forms

from .models import Place, Comment

class PlaceForm(ModelForm):
    name = forms.CharField(
        label='Place name',
        widget=forms.TextInput(attrs={'class':'form-control'}),
    )
    text = forms.CharField( #TextField
        required=False,
        label='Description',
        widget=forms.Textarea(attrs={'class':'form-control'}),
    )

    class Meta:
        model = Place
        fields = ['name', 'text']

class CommentForm(ModelForm):
    text = forms.CharField(#TextField
        label='Content',
        widget=forms.Textarea(attrs={
            'class':'form-control',
            'cols': 50,
            'rows': 10
            }
        ),
    )
    class Meta:
        model = Comment
        fields = ['text']
