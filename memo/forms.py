from django.forms import ModelForm  # Django의 modelform을 쓰기 위해서 import 해주었다.
from .models import Memo, Comment  # Modelform을 만들 재료인 Model도 가져온다.
from django_summernote.widgets import SummernoteWidget


class MemoForm(ModelForm):

    class Meta:
        model = Memo
        fields = ("title", "desc", "pic")

        widgets = {
            'desc' : SummernoteWidget(),
        }


class NewForm(ModelForm):

    class Meta:
        model = Memo
        fields = ('title', 'desc', 'pic',)  # 하나만 있어도 , 작성


class CommentForm(ModelForm):
    
    class Meta:
        model = Comment
        fields = ('desc',)