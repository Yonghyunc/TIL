Authentication (인증)

두 번째 app (accounts) 생성


User Model

admin
Django는 내장된 유저모델이 이미 사용되고 있다
-> Custom User Model로 대체

AUTH_USER_MODEL

auth.User : auth앱의 User 클래스
django.contrib.auth
(첫 번째 마이그레이션 이후 변경 불가)


1. 대체할 커스텀 유저모델 작성
``` python
# accounts/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass
```

2. AUTH_USER_MODEL의 값 변경

crud/settings.py
`AUTH_USER_MODEL = 'accounts.User'`
- 프로그램 중간에 X, 시작 단계에 O

3. admin.py에 커스텀 User 모델 등록

``` python
# accounts/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
admin.site.register(User, UserAdmin)
```

> AbstactUser
> 관리자 권한과 함께 완전한 기능을 가지고 있는 User model을 구현하는 추상 기본클래스

커스텀 유저 모델 --> 강력 권장!!!

---

HTTP Cookies
요청 - 응답

쿠키 : 상태 유지
- 서버가 사용자의 웹 브라우저에 전송하는 작은 데이터 조각

1. 브라우저는 쿠키를 로컬에 KEY-VALUE 데이터 형식으로 저장
2. 쿠키를 저장해 놓았다가, 동일한 서버에 재요청 시 저장된 쿠키를 함께 전송

- 쿠키는 두 요청이 동일한 브라우저에서 들어왔는지 아닌지 판단할 때 주로 사용
  - -> 사용자의 로그인 상태 유지 O
  > 쿠키 - 나 로그인된 사용자다 / 매 요청마다 보냄

쿠키 사용 목적
1. 세션 관리 : 로그인, 아이디 자동완성, 장바구니 등
2. 개인화
3. 트래킹


세션
- 사이트와 특정 브라우저 사이의 상태를 유지시키는 것
- 클라이언트가 서버에 접속하면 서버가 특정 session id를 발급하고, 클라이언트는 session id를 쿠키에 저장
- 다시 동일한 서버에 접속하면 요청과 함꼐 session id가 저장된 쿠키를 서버에 전달


쿠키는 session id만 저장
핵심 정보는 서버가

쿠키 Lifetime (수명)
1. session cookie
2. ...


Session in Django
장고가 세션 관리 해줄거야~
- session 정보는 django_session 테이블에 저장



Login 
: session을 create하는 과정

- AuthenticationForm


1. 로그인할 페이지를 보여줄 view함수 먼저
- accounts/urls.py
`path('login/', views.login, name='login')`
- accounts/views.py
``` python
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def login(request):
    if request.method == "POST":
        pass
    else:
        form = AuthenticationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/login.html', context)
```

- templates/accounts/login.html
``` html
{% extends 'base.html' %}

{% block content %}
  <h1>LOGIN</h1>
  <form action="{% url 'accounts:login' %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
  </form>
{% endblock content %}
```

![image](https://user-images.githubusercontent.com/93974908/188770136-642ffaed-e43e-40a6-9f81-0a0f68cba7f5.png)


> `form = AuthenticationForm(request, request.POST)`
> 첫 번째 인자 : request


문제 1 : 함수 이름과 모듈 이름이 겹침
-> 모듈 이름 수정
login -> auth_login

문제 2 : 분명 무슨 문제가 있다고 했는데,,,?

``` python
# accounts/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login


# Create your views here.
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_vaild():
            # 로그인
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)
```

login()
- login(request, user, backend=None)
- 입력된 데이터 판단 -> 현재 세션에 데이터 입력



Authentication with User
- 현재 로그인 되어있는 유저 정보 출력하기
- -> 기본 context가 있다는 뜻 -> 어디에? : settings.py context processors

``` python
'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
```
  
> ```
> context = {
        'form': form,
        'user' : user, 
    }
    ```
>    사용은 위험함!

---

Logout
- session을 delete하는 과정
