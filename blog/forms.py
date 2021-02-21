from django import forms

from .models import Comment, QuestionAnswer


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text',)


class QuestionForm(forms.ModelForm):
    class Meta:
        model = QuestionAnswer
        fields = ('author', 'question',)
