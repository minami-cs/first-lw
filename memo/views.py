from django.shortcuts import render, redirect
from .models import Memo
from .forms import MemoForm, NewForm, CommentForm
from django.contrib.auth.decorators import login_required


# Create your views here.


def index(request):
    context = dict()
    # print(request.POST.get('mydata'),"@"*50)
    request.POST.get('mydata')
    all_memo = Memo.objects.all()
    context['all_memo'] = all_memo
    return render(request, 'index.html', context)


def second(request):
    return render(request, 'second.html')


@login_required
def create(request):
    context = dict()
    context['memoform'] = MemoForm()
    if request.method == "POST":
        myform = MemoForm(request.POST, request.FILES)
        if myform.is_valid():
            myform.save()
            return redirect('index')
        else:
            context['memoform'] = myform
        pass
        # print(request.POST.get('title'))
        # Memo.object.create(title=request.POST.get("title"),
        #                    desc=request.POST.get("desc"),
        #                    pic=request.POST.get("pic"))

    return render(request, 'create.html', context)


def new(request):
    context = {}
    context['newform'] = NewForm()
    if request.method == "POST":
        tempform = NewForm(request.POST, request.FILES)
        if tempform.is_valid():
            tempform.save()
            return redirect('index')
        else:
            context['newform'] = tempform
    return render(request, 'new.html', context)


def detail(request, detail_id):
    context = {}
    one_memo = Memo.objects.get(id=detail_id)  # 예를 들어 5번 id글을 가져오겠다는 뜻
    # get_objects_or_404 참고
    context['one_memo'] = one_memo
    context['comment_form'] = CommentForm

    return render(request, 'detail.html', context)


def update(request, update_id):
    context = {}
    context['newform'] = NewForm(instance=Memo.objects.get(id=update_id))

    if request.method == "POST":
        tempform = NewForm(request.POST, request.FILES,
                           instance=Memo.objects.get(id=update_id),)
        if tempform.is_valid():
            tempform.save()
            return redirect('detail', update_id)
        else:
            context['newform'] = tempform
    return render(request, 'new.html', context)


def delete(request, delete_id):
    one_memo = Memo.objects.get(id=delete_id)
    one_memo.delete()
    return redirect('index')


def create_comment(request, memo_id):
    context = dict()

    if request.method == "POST":
        tmp_comment = CommentForm(request.POST)
        if tmp_comment.is_valid():
            save_comment = tmp_comment.save(commit=False)
            save_comment.memo = Memo.objects.get(id=memo_id)
            save_comment.save()
            return redirect('detail', memo_id)
    return redirect('index')