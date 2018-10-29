from django.forms import ModelForm, Textarea
from .models import Review


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['Rating', 'Comment']
        widgets = {
            'Comment': Textarea(attrs={'cols': 20, 'rows': 10}),
        }