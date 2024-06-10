from django import forms
from .forms import ConversationMessage

class ConversationForm(forms.ModelForm):
    class Meta:
        model = ConversationMessage
        fields = ('content',)
        widgets = {
            'content':forms.Textarea(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'
            })
        }