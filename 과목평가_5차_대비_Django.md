# Table of Contents
### 💻 Django Web Framework
- [Table of Contents](#table-of-contents)
    - [💻 Django Web Framework](#-django-web-framework)
    - [💻 Django Model](#-django-model)
- [Django Web Framework](#django-web-framework)
  - [🥕 MTV](#-mtv)
  - [🥕 URL](#-url)
  - [🥕 Django template path](#-django-template-path)
  - [🥕 한국어로 번역하기](#-한국어로-번역하기)
  - [🥕 경로 설정하기](#-경로-설정하기)
  - [🥕 Django Template Language](#-django-template-language)
  - [🥕 Form tag with Django](#-form-tag-with-django)
- [Django Model](#django-model)
  - [🍋 Model 반영하기](#-model-반영하기)
  - [🍋 Model 변경사항 저장하기](#-model-변경사항-저장하기)
  - [🍋 Python Shell](#-python-shell)
  - [🍋 Django Model Field](#-django-model-field)
  - [🍋 Django Model](#-django-model-1)

<br>

### 💻 Django Model
- [Model 반영하기](#-model-반영하기)
- [Model 변경사항 저장하기](#-model-변경사항-저장하기)
- [Python Shell](#-python-shell)
- [Django Model Field](#-django-model-field)
- [Django Model](#-django-model)


<br><br>

---
# Django Web Framework

## 🥕 MTV
Django는 MTV 디자인 패턴으로 이루어진 Web Framework이다.

<br>
- Model(데이터베이스 관리) - Model
- Template(인터페이스, 화면) - View
- View(중심 컨트롤러) - Controller

<br>

🔹 Model
- 응용프로그램의 데이터 구조를 정의하고 데이터베이스의 기록을 관리(추가, 수정, 삭제)

<br>

🔹 Template
- 파일의 구조나 레이아웃을 정의
- 실제 내용을 보여주는 데 사용(presentation)

<br>

🔹 View
- HTTP 요청을 수신하고 HTTP 응답을 반환
- Model을 통해 요청을 충족시키는데 필요한 데이터에 접근
- 그리고 탬플릿에게 응답의 서식 설정을 맡김

<br><br>

---

## 🥕 URL
💙 Variable Routing : Django에서 URL 자체를 변수처럼 사용해서 동적으로 주소를 만드는 것

- 템플릿의 많은 부분이 중복되고, 일부분만 변경되는 상황에서 비슷한 URL과 템플릿을 계속해서 만들지 않기 위해
- URL 주소를 변수로 사용
- URL의 일부를 변수로 지정하여 views 함수의 인자로 넘길 수 있음
- 즉, 변수 값에 따라 하나의 path()에 여러 페이지를 연결 시킬 수 있음

<br><br>

---

## 🥕 Django template path
Django 프로젝트는 render할 template 파일들을 찾을 때, 기본적으로 settings.py에 등록된 각 앱 폴더 안의 templates 폴더 내부를 탐색한다.


<br><br>

---

## 🥕 한국어로 번역하기
Django 프로젝트를 한국어로 제공하기 위해 번역 설정

1️⃣ settings.py에 어떤 변수를 어떤 값으로 할당해야 하는가?  <br>
`LANGUAGE_CODE = 'ko-kr'`
2️⃣ settings.py에 어떤 변수가 활성화 되어 있어야 위의 변수를 설정할 수 있는가? <br>
`USE_I18N`

<br/>

- LANGUAGE_CODE : 번역 <br/>
  USE_I18N = True 여야만 사용 가능

- TIME_ZON : 시간대 <br/>
  USE_TZ = True 여야만 사용 가능

``` python
LANGUAGE_CODE = 'ko-kr'
TIME_ZONE = 'Asia/Seoul'
```


<br><br>

---

## 🥕 경로 설정하기
```python
from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
  path('ssafy/', views.ssafy),
  path('admin/', admin.site.urls),
]
```
- url의 끝 주소에는 / 적어주기
- 트레일링 콤마( , ) 적어주기 (확장성)

<br><br>

---

## 🥕 Django Template Language

1. menus 리스트를 반복문으로 출력
``` html
{% for menu in menus %}
  <p>{{ menu }}</p>
{% endfor %}
```

<br>

2. posts 리스트를 반복문을 활용하여 0번 글부터 출력
``` html 
{% for post in posts %}
  <p>{{ forloop.counter0 }}번 글 : {{ post }}</p>
{% endfor %}
```

<br>

3. users 리스트가 비어있다면 "현재 가입한 유저가 없습니다." 텍스트 출력
``` html
{% for user in users %}
  <p>{{ user }}</p>
{% empty %}
  <p>현재 가입한 유저가 없습니다.</p>
{% endfor %}
```

<br>

4. 첫 번째 반복문일 때와 아닐 때를 조건문으로 분기 처리
``` html
{% if forloop.first %}
  <p>첫 번째 반복문 입니다.</p>
{% else %}
  <p>첫 번째 반복문이 아닙니다.</p>
{% endif %}
```

<br>

5. 출력된 결과가 주석과 같도록
``` html
<!-- 글자 길이 : 5 -->
<p>글자 길이 : {{ 'hello'| length }}</p>
<!-- My Name Is Tom -->
<p>{{ 'my name is tom' | title }}</p>
```

<br>

6. 변수 today에 datetime 객체가 들어있을 때, 출력된 결과가 주석과 같도록
[공식문서](https://docs.djangoproject.com/en/4.1/ref/templates/builtins/)

``` html
<!-- 2022년 08월 8일 (Mon) AM 10:02 -->
<p>{{ today | date:"Y년 m월 j일 (D) A h:i" }}</p>
```
> 참고! `{{ today|date: "Y년 m월 j일 (D) A h:i"}}`과 같이 콜론(:) 뒤 공백시 아래 에러 발생
Could not parse the remainder: ': "Y년 m월 j일 (D) A h:i"' from 'today | date: "Y년 m월 j일 (D) A h:i"'

<br><br>

---

## 🥕 Form tag with Django
``` html
<form action="/create/" method="">
  <label for="title">Title : </label>
  <input type="text" name="title" id="title">
  <label for="content">Content : </label>
  <input type="text" name="content" id="content">
  <label for="my-site">My-Site : </label>
  <input type="text" name="my-site" id="my-site">
  <input type="submit">
</form>
```
<br>

1️⃣ form 태그의 속성인 action의 역할 <br>
: form이 제출될 떄 데이터를 보낼 경로 지정

<br>

2️⃣ method가 가질 수 있는 속성 값 <br>
: GET, POST

<br>

3️⃣ input 태그에 각각 '안녕하세여', '반갑습니다', '파이팅' 문자열을 넣고 submit 버튼을 눌렀을 때 이동하는 url 경로 <br>
: `http://127.0.0.1:8000/create/?title=안녕하세요&content=반갑습니다&my-site=파이팅`


<br><br>

---
# Django Model

## 🍋 Model 반영하기
Django가 Model에 생긴 변화는 DB에 반영하는 방법 <br>
➡ Migrate (Migration)

<br><br>

---

## 🍋 Model 변경사항 저장하기
``` python
class Article(models.Model):
  title = models.CharField(max_length=10)
  content = models.TextField()
```
<br>

1️⃣ Model의 변경사항을 저장하기 위한 명령어  <br>
: `$ python manage.py makemigrations`

<br>

2️⃣ 생성된 마이그레이션 파일에 대응되는 SQL문을 확인하기 위한 명령어와 출력결과 (app_name = articles) <br>
: `$ python manage.py sqlmigrate app_name 0001`

``` sh
CREATE TABLE "articles_article"
	 ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
   "title" varchar(100) NOT NULL, "content" text NOT NULL);
```

<br><br>

---

## 🍋 Python Shell
Django에서 사용 가능한 모듈 및 메서드를 대화식 Python Shell에서 사용하려고 할 때, 사용해야 하는 명령어 <br>

➡ 기본 Shell : `$ python manage.py shell` <br>

➡ django_extensions : `$ python manage.py shell_plus` 

<br><br>

---

## 🍋 Django Model Field
Django에서 Model을 정의할 때 사용할 수 있는 필드 타입
- models.CharField
- models.TextField
- models.IntegerField
- models.DateField
- models.FileField
- 등등

<br><br>

---

## 🍋 Django Model
``` python
# posts/models.py
from django.db import models

class Post(models.Model):
  title = models.CharField(max_length=100)
  content = models.TextField()
```
<br>

1️⃣ models.py를 작성한 후 마이그레이션 작업을 위해 터미널에 작성해야 하는 핵심 명령어

`$ python manage.py makemigrations`

`$ python manage.py migrate`

<br>

2️⃣ 새로운 POST를 저장하기 위한 코드 3가지
``` python
# 1
post = Post()
post.title = 'a'
post.content = 'b'
post.save()

# 2 ✔
post = Post(title='가', content='나')
post.save()

# 3
Post.objects.create(title='1', content='2')
```

> 인스턴트 생성 시, 필드 명을 함께 적어야 한다.

<br>

3️⃣ Post가 10개 저장되어 있고 id의 값이 1부터 10까지라고 가정할 때, 가장 첫 번째 Post를 가져오는 코드

``` python
# 1
post1 = Post.objects.all()[0]

#2 
post2 = Post.objects.all().first()

# 3
post3 = Post.objects.all().get(id=1)
```
> Negative indexing(음수 인덱싱) 지원하지 않음


<br>

4️⃣ my_post 변수에 post 객체 하나가 저장되어 있을 때, title을 '안녕하세요', content를 '반갑습니다'로 수정하기 위한 코드

```python
my_post.title = '안녕하세요'
my_post.content = '반갑습니다'
my_post.save()
```

<br>

5️⃣ 만들어진 모든 Post 데이터를 QuerySet 형태로 반환해주기 위한 코드

`posts = Post.objects.all()`