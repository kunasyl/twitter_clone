from django import forms

from .models import Tweet


class AddTweetForm(forms.ModelForm):
    tweet = forms.CharField(required=True,
                            widget=forms.widgets.Textarea(attrs={
                                'placeholder': 'Write your Tweet here in 140 characters',
                                'class': 'form-control',
                                'maxlength': '140'
                            }))

    class Meta:
        model = Tweet
        exclude = ('user', 'created_at')
