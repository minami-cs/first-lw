from django.db import models

# Create your models here.

# memo 데이터베이스 만들기
class Memo(models.Model):
    title = models.CharField("제목", max_length=1000)
    desc = models.TextField("본문", blank=True)
    pic = models.ImageField("사진", blank=True, null=True)

    created_date = models.DateTimeField("생성날짜", auto_now_add=True)    # 생성할 떄 정해짐
    modified_date = models.DateTimeField("수정날짜", auto_now=True)    # 수정할 때 바뀜
    
    
    def __str__(self):    # "제목"을 memo페이지에서 표시하게 해줌
        return self.title

class Comment(models.Model):
    # ForeignKey: 참조하는 대상값을 의미하는데 여기서는 글을 의미
    memo = models.ForeignKey('Memo', on_delete=models.CASCADE, related_name='comment_set')
    # PrimaryKey: 우리가 어떤 대상을 식별할 수 있는 고유한 key값
    # related_name속성을 주면 _set을 다른 이름으로 설정할 수 있음
    # ManyToManyField: ForeignKey와 동일하게 동작함
    desc = models.CharField('댓글내용', max_length=100)
    created_date = models.DateTimeField('생성날짜', auto_now_add=True)

    def __str__(self):
        return self.desc

