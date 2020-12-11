from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm  # 유저생성모델폼
from django.contrib.auth import authenticate, login

# Create your views here.

def signup(request):
    context = dict()
    if request.method == "POST":
        save_form = UserCreationForm(request.POST)
        if save_form.is_valid():
            save_form.save()

            # 회원가입과 동시에 로그인 가능
            user = authenticate(username = save_form.cleaned_data['username'],
                                password = save_form.cleaned_data['password1'])

            login(request, user)

            return redirect('index')
        else:  # 사용자가 입력한 데이터가 유효성 검사에서 통과 실패
            context['userform'] = save_form  # 사용자가 입력한 데이터와 실패한 이유가 담긴 form
            return render(request, 'registration/signup.html', context)
    context['userform'] = UserCreationForm()
    return render(request, 'registration/signup.html', context)