# Today I Learned
- [Today I Learned](#today-i-learned)
- [The Django authentication system](#the-django-authentication-system)
  - [custom User model로 대체하기](#custom-user-model로-대체하기)
    - [💛 AUTH_USER_MODEL](#-auth_user_model)
- [HTTP Cookies](#http-cookies)
  - [HTTP](#http)
    - [❓ HOW 로그인 상태 유지 ❓](#-how-로그인-상태-유지-)
  - [쿠키 : 상태 유지](#쿠키--상태-유지)
  - [세션](#세션)
    - [쿠키 Lifetime (수명)](#쿠키-lifetime-수명)
    - [Session in Django](#session-in-django)
- [Authentication in Web requests](#authentication-in-web-requests)
  - [1. Login](#1-login)
    - [🔹 AuthenticationForm](#-authenticationform)
    - [로그인할 페이지를 보여줄 view함수 먼저](#로그인할-페이지를-보여줄-view함수-먼저)
    - [login()](#login)
  - [Authentication with User](#authentication-with-user)
    - [❓ HOW base.html에서 context 데이터 없이 user 변수 사용❓](#-how-basehtml에서-context-데이터-없이-user-변수-사용)
    - [⭐ context processors](#-context-processors)
  - [2. Logout](#2-logout)
    - [logout(request)](#logoutrequest)
- [Authentication with User](#authentication-with-user-1)
  - [1. 회원가입](#1-회원가입)
    - [🔹 UserCreationForm](#-usercreationform)
  - [Custom user & Built-in auth forms](#custom-user--built-in-auth-forms)
    - [🔸 AbstractBaseUser의 모든 subclass와 호환되는 form](#-abstractbaseuser의-모든-subclass와-호환되는-form)
    - [🔸 커스텀 유저 모델을 사용하려면 다시 작성하거나 확장해야 하는 form](#-커스텀-유저-모델을-사용하려면-다시-작성하거나-확장해야-하는-form)
  - [2. 회원탈퇴](#2-회원탈퇴)
  - [3. 회원정보 수정](#3-회원정보-수정)
    - [🔹 UserChangeForm](#-userchangeform)
    - [CustomUserChangeForm **fields** 재정의](#customuserchangeform-fields-재정의)
  - [4. 비밀번호 변경](#4-비밀번호-변경)
    - [🔹 PasswordChangeForm](#-passwordchangeform)
- [Limiting access to logged-in users](#limiting-access-to-logged-in-users)
  - [⭐ is_authenticated](#-is_authenticated)
    - [▪ login_required 데코레이터](#-login_required-데코레이터)

<br><br>

---

# The Django authentication system
인증 시스템은 인증과 권한 부여를 함께 제공(처리)함 <br>
django.contrib.auth (settings.py에 이미 포함 O)

<br>

- Authentication (인증)
  - 신원 확인
  - 사용자가 자신이 누구인지 확인하는 것
  
- Authorization (권한, 허가)
  - 권한 부여
  - 인증된 사용자가 수행할 수 있는 작업 결정


두 번째 app (accounts) 생성


## custom User model로 대체하기

Django는 내장된 유저모델이 이미 사용되고 있다
➡ Custom User Model로 대체


### 💛 AUTH_USER_MODEL
- 프로젝트에서 User를 나타낼 때 사용하는 모델
- auth.User : auth앱의 User 클래스
- django.contrib.auth
- 첫 번째 마이그레이션 이후 변경 불가

<br><br>

1. 대체할 커스텀 유저모델 작성
   - AbstractUser를 상속받는 커스텀 User 클래스 작성
    ▶ accounts/models.py
    ``` python
    from django.db import models
    from django.contrib.auth.models import AbstractUser

    # Create your models here.
    class User(AbstractUser):
        pass
    ```

<br>

2. AUTH_USER_MODEL의 값 변경
    ▶ crud/settings.py <br>
    `AUTH_USER_MODEL = 'accounts.User'`
    - 프로그램 중간에 X, 시작 단계에 O

<br>

3. admin.py에 커스텀 User 모델 등록

    ``` python
    # accounts/admin.py

    from django.contrib import admin
    from django.contrib.auth.admin import UserAdmin
    from .models import User

    # Register your models here.
    admin.site.register(User, UserAdmin)
    ```

<br>

> AbstactUser
> 
> 관리자 권한과 함께 완전한 기능을 가지고 있는 User model을 구현하는 추상 기본클래스
> 
>> Abstaract base classes (추상 기본 클래스)
>> 몇 가지 공통 정보를 여러 다른 모델에 넣을 때 사용하는 클래스

커스텀 유저 모델 --> 강력 권장!!! <br>
WHY? ➡ 커스텀 User 모델을 기본 User 모델과 동일하게 작동하면서도 필요한 경우 나중에 맞춤 설정할 수 있다 <br>
BUT 프로젝트 처음에 진행!!

<br><br>

---

# HTTP Cookies

## HTTP
- Hyper Text Transfer Protocol
- HTML 문서와 같은 리소스들을 가져올 수 있도록 해주는 프로토콜(규칙, 규약)
- 웹에서 이루어지는 모든 데이터 교환의 기초
- 클라이언트 - 서버 프로토콜

<br>

📢 **요청 - 응답** <br>
요청 (requests) : 클라이언트(브라우저)에 의해 전송되는 메시지 <br>
응답 (response) : 서버에서 응답으로 전송되는 메시지

<br>

- 특징 
  - 1. 비 연결 지향 : 서버는 요청에 대한 응답을 보낸 후 연결을 끊음
  - 2. 무상태 : 연결을 끊는 순간 클라이언트와 서버 간의 통신이 끝나며 상태 정보 유지 X


<br><br>

### ❓ HOW 로그인 상태 유지 ❓
➡ **"쿠키와 세션"**

<br>

## 쿠키 : 상태 유지
- 서버가 사용자의 웹 브라우저에 전송하는 작은 데이터 조각

1. 브라우저는 쿠키를 로컬에 KEY-VALUE 데이터 형식으로 저장
2. 쿠키를 저장해 놓았다가, 동일한 서버에 재요청 시 저장된 쿠키를 함께 전송

- 쿠키는 두 요청이 동일한 브라우저에서 들어왔는지 아닌지 판단할 때 주로 사용
  - ➡ 사용자의 로그인 상태 유지 O
  > 쿠키 - 나 로그인된 사용자다 / 매 요청마다 보냄

<br>

✅ 쿠키 사용 목적
1. **세션 관리** : 로그인, 아이디 자동완성, 장바구니 등
2. 개인화
3. 트래킹

<br><br>

## 세션
- 사이트와 특정 브라우저 사이의 "상태"를 유지시키는 것
- 클라이언트가 서버에 접속하면 서버가 특정 session id를 발급하고, 클라이언트는 session id를 쿠키에 저장
- 다시 동일한 서버에 접속하면 요청과 함꼐 session id가 저장된 쿠키를 서버에 전달


> 쿠키는 session id만 저장 <br>
> 핵심 정보는 서버가

<br><br>


### 쿠키 Lifetime (수명)
1. Session cookie
- 현재 세션이 종료되면 삭제됨
- 브라우저 종료와 함께 세션이 삭제됨

2. Persistent cookies
- Expires 속성에 지정된 날짜 / Max-Age 속성에 지정된 기간이 지나면 삭제됨

<br>

### Session in Django
장고가 세션 관리 해줄거야~
- session 정보는 django_session 테이블에 저장
- 설정을 통해 다른 저장방식으로 변경 가능
- Django는 특정 session id를 포함하는 쿠키를 사용해서 각각의 브라우저와 사이트가 연결된 session을 알아냄


<br><br>

---

# Authentication in Web requests

## 1. Login 
: session을 create하는 과정

<br>

### 🔹 AuthenticationForm
- 로그인을 위한 built-in form
  - 로그인 하고자 하는 사용자 정보를 입력받음
  - 기본적으로 username과 password를 받아 데이터가 유효한지 검증

<br>

### 로그인할 페이지를 보여줄 view함수 먼저
📍 accounts/urls.py <br>
`path('login/', views.login, name='login')`

<br>

📍 accounts/views.py
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
<br>

📍 accounts/templates/accounts/login.html
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

<br>
📍 출력 결과

![image](https://user-images.githubusercontent.com/93974908/188770136-642ffaed-e43e-40a6-9f81-0a0f68cba7f5.png)

<br>

### login()
- login(request, user, backend=None)
- 입력된 데이터 판단 -> 현재 세션에 데이터 입력

> `form = AuthenticationForm(request, request.POST)`
> 첫 번째 인자 : request

<br>

❌ 문제 : 함수 이름과 모듈 이름이 겹침 <br>
➡ 모듈 이름 수정 : login -> auth_login


<br>

📍 accounts/views.py
``` python
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
> get_user()
> - 유효성 검사를 통과했을 경우 로그인 한 사용자 객체 반환

<br><br>


## Authentication with User
- 현재 로그인 되어있는 유저 정보 출력하기

📍 base.html
``` html
<body>
  <div class="container">
    {% if request.user.is_authenticated %}
      <h3>{{ user }}</h3> 
    ...
    {% block content %}
    {% endblock content %}
  </div>
</body>
```

<br>

### ❓ HOW base.html에서 context 데이터 없이 user 변수 사용❓
➡ 기본 context가 있다는 뜻 ➡ 어디에? : settings.py의 context processors 설정 값

### ⭐ context processors
- 템플릿이 렌더링 될 때 호출 가능한 context 데이터 목록
- 즉, django에서 자주 사용하는 데이터 목록을 미리 템플릿에 로드 해 둔 것


``` python
'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
```
> 현재 user 변수는 `'django.contrib.auth.context_processors.auth'` 프로세서

<br><br>


```
context = {
        'form': form,
        'user' : user, 
    }
```
> 위와 같은 사용은 위험함!

<br><br>

---

## 2. Logout
- session을 delete하는 과정

### logout(request)

- HttpRequest 객체를 이나로 받고 반환 값이 없음
- 사용자가 로그인하지 않은 경우 오류 X

1. 현재 요청에 대한 session data를 DB에서 삭제
2. 클라이언트의 쿠키에서도 session id를 삭제

  - 다른 사람이 동일한 웹 브라우저를 사용하여 로그인하고, 이전 사용자의세션 데이터에 액세스하는 것을 방지하기 위함

<br>

📍 accounts/urls.py <br>
`path('logout/', views.logout, name='logout')`

<br>

📍 accounts/views.py
``` python
def logout(request):
    auth_logout(request)
    return redirect('articles:index')
```

<br><br>

---
# Authentication with User

## 1. 회원가입

### 🔹 UserCreationForm
- 주어진 username과 password로 권한이 없는 새 user를 생성하는 ModelForm (일반 유저)
  > user data에 저장이 되야 하므로 ModelForm
- 3개의 필드
  1. username
  2. password1
  3. password2

📍 url <br>
`path('signup/', views.signup, name='signup')`

<br>

📍 views <br>
``` python
# create (user)
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = UserCreationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/signup.html', context)
```
<br>

📍 template
``` html
{% extends 'base.html' %}

{% block content %}
  <h1>SIGNUP</h1>
  <form action="{% url 'accounts:signup' %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
  </form>
{% endblock content %}
```

<br>

📍 출력 결과
![image](https://user-images.githubusercontent.com/93974908/188791298-b0f222e7-f51a-49b9-a7b0-d9a500572d84.png)

<br>

❌ 에러 발생 

![image](https://user-images.githubusercontent.com/93974908/188792041-6496e620-c3b0-48ac-acc2-edc4d5ab9407.png)

해당 오류는 이상한게 아님! <br>
➡ UserCreationFrom은 모델폼, 즉 클래스 메타가 있음  <br>
➡ user가 자동으로 안 바뀜 (프로그램에서 다른 유저로 바꾸었다고 해도 과거의 유저를 모델로 등록해놓음)

UserCreationFrom이 기존 유저 모델로 인해 작성된 클래스이기 때문

<br>

상속의 관점에서 해결
-> 오버라이드


---

<br>

## Custom user & Built-in auth forms
### 🔸 AbstractBaseUser의 모든 subclass와 호환되는 form
- AuthenticationForm
- SetPasswordForm
- PasswordChangeForm
- AdminPasswordChangeForm
> 기존 user 모델을 참조하는 form이 아님

<br>

### 🔸 커스텀 유저 모델을 사용하려면 다시 작성하거나 확장해야 하는 form
- UserCreationForm : 회원가입
- UserChangeForm : 회원 정보 수정
> class Meta: model = User가 등록된 form 이기 때문에 반드시 커스텀해야 함

<br>

📍 accounts/forms.py 생성 후 작성

``` python
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = get_user_model()


class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = get_user_model()
```


> get_user_model()
> 
> : 현재 프로젝트에서 활성화된 사용자 모델을 반환

<br>

📍 accounts/views.py <br>
CustomUserCreationForm()으로 대체
``` python
from .forms import CustomUserCreationForm, CustomUserChangeForm


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/signup.html', context)
```

<br>

➕ 가입 후 자동로그인 <br>
저장한 정보를 가지고 있게 해줌
``` python
user = form.save()
auth_login(request, user)
```

<br><br>

## 2. 회원탈퇴
📍 url <br>
`path('delete/', views.delete, name='delete')`

<br>

📍 views
``` python
def delete(request):
    request.user.delete()
    return redirect('articles:index')
```
<br>

로그아웃 후 탈퇴
``` python
def delete(request):
    auth_logout(request)
    request.user.delete()
    return redirect('articles:index')
```
> 탈퇴 후 로그아웃 순서가 바뀌면 안됨
> 
> request 정보가 사라지므로 탈퇴에 필요한 정보를 얻을 수 없음

<br><br>

## 3. 회원정보 수정
### 🔹 UserChangeForm
- 사용자의 정보 및 권한을 변경하기 위해 admin 인터페이스에서 사용되는 ModelForm
- ModelForm이기 때문에 instance 인자로 기존 user 데이터 정보를 받음
- CustomUserChangeForm 사용

<br>

📍 url <br>
`path('update/', views.update, name='update'),`

<br>

📍 views
``` python
def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_vaild():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form' : form,
    }
    return render(request, 'accounts/update.html', context)
```
<br>

📍 template
``` html
{% extends 'base.html' %}

{% block content %}
  <h1>회원정보수정</h1>
  <form action="{% url 'accounts:update' %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
  </form>
{% endblock content %}
```

<br>

📍 출력 결과
![image](https://user-images.githubusercontent.com/93974908/188801489-819a425a-55d8-4ffd-8b60-f5125429774e.png)
> 일반사용자에게 너무 많은 권한을 오픈함
> 덜어낼 필요 O - 출력될 것을 선택

<br><br>

### CustomUserChangeForm **fields** 재정의

📍 accounts/forms.py
``` python
class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name',)
```
> user 모델의 fields명을 알기 위해서는,
> 1. UserChangeForm 클래스 구조 확인
> 2. User 클래스 구조 확인
> 3. AbstractUser 클래스 구조 확인
> 4. 공식문서의 User 모델의 Fields 확인

<br>
📍 재정의 후 출력 결과

![image](https://user-images.githubusercontent.com/93974908/188801961-9749040c-6fd0-4f99-a923-937b7849d4fe.png)



> 비밀번호 변경 폼 따로 (대부분의 사이트가 그러함)

<br><br>

## 4. 비밀번호 변경

### 🔹 PasswordChangeForm
- 이전 비밀번호를 입력하여 비밀번호를 변경할 수 있도록 함
- 이전 비밀번호를 입력하지 않고 비밀번호를 설정할 수 있는 SetPasswordForm을 상속받는 서브 클래스

<br>

📍 url <br>
`path('password/', views.change_password, name="change_password")`

<br>

📍 views
``` python
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm


def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form' : form,
    }
    return render(request, 'accounts/change_password.html', context)
```

<br>

📍 template
``` html
{% extends 'base.html' %}

{% block content %}
  <h1>비밀번호 변경</h1>
  <form action="{% url 'accounts:change_password' %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
  </form>
{% endblock content %}
```

<br>

- PasswordChangeForm은 SetPasswordForm의 하위인자, 상속으로 인해 첫번째 인자로 request.user 받아야함


- 비번 변경 후 로그아웃 - 정상 (기존 세션 만료)

<br>

> update_session_auth_hash(request, user)
> - 현재 요청과 새 session data가 파생될 업데이트된 사용자 객체를 가져오고, session data를 적절하게 업데이트해줌

``` python
from django.contrib.auth import update_session_auth_hash


def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form' : form,
    }
    return render(request, 'accounts/change_password.html', context)
```
<br><br>

---

# Limiting access to logged-in users
로그인 사용자에 대한 접근 제한
1. 속성 : is_authenticated
2. 데코레이터 : login_required

<br>

## ⭐ is_authenticated
- 사용자가 인증 되었는지 여부를 알 수 있는 방법
- 모든 User 인스턴스에 대해 항상 True인 읽기 전용 속성
- AnontmousUser에 대해서는 항상 False
- request.user에서 이 속성에 접근할 수 있음


> 권한과는 관련 X , 사용자가 활성 상태인지 확인 X, 유효한 세션인지 X
> 
> 로그인 / 비로그인 사용자 인지만 확인

``` html
{% if request.usr.is_authenticated %}
    <h3>{{ user }}</h3>
    <form action="{% url 'accounts:logout' %}" method="POST">
        {% csrf_token %}
        <input type="submit" value="Logout">
    </form>
    <a href="{% url 'accounts:update' %}">회원정보수정</a>
    <form action="{% url 'accounts:delete' %}" method="POST">
        {% csrf_token %}
        <input type="submit" value="회원탈퇴">
    </form>
{% else %}
    <a href="{% url 'accounts:login' %}">Login</a>
    <a href="{% url 'accounts:signup' %}">Signup</a>
{% endif %}
```
> 출력만 막음 <br>
> 주소 쳐서 들어가기 가능

<br>

⬇ <br>
인증된 사용자라면 로그인 로직을 수행할 수 없도록 처리 <br>
📍 view
``` python
def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
```

<br>

### ▪ login_required 데코레이터
- 사용자가 로그인 되어 있으면 정상적으로 view 함수 실행

> 데코레이터 내용 추후 추가