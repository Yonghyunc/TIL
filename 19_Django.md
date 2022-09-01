# Today I Learned
- [Django Intro](#django)
- [Django 구조 (MTV Design Pattern)](#django-구조-mtv-design-pattern)
- [Django 설치](#django-설치)
- [Django Template](#django-template)
- [Django URLs](#django-urls)


<br/><br/>

---

# Django
'웹 서비스 개발'


## Django Framework
> 밀키트 같음🍲
- 누군가 만들어 놓은 코드 재사용
- 서비스 개발에 필요한 기능들을 미리 구현해서 모아 놓은 것 = 프레임워크
- 내가 만들고자 하는 본질에 집중해 개발 O
- 소프트웨어의 생산성 + 품질 높임

> 파이썬으로 작성된 프레임워크 -> Flask, Django, FastAPI

<br/>

## 🌏 Web 이해하기
- WWW (World Wide Web) : 전 세계에 퍼져 있는 거미줄 같은 연결망
- 우리가 인터넷을 이용한다는 건, 전세계의 컴퓨터가 연결되어 있는 하나의 인프라를 이용하는 것
- 가장 많이 사용하는 구조 : 클라이언트-서버 구조

### 🧑‍💻 클라이언트-서버 구조
- 클라이언트 - 요청 (크롬 브라우저, 나)
- 서버 - 응답 (구글 서버)


➡️ django는 서버를 구현하는 웹 프레임워크

### 웹 브라우저
- 웹에서 페이지를 찾아 보여주고, 사용하가 하이퍼링크를 통해 다른 페이지로 이동할 수 있도록 하는 프로그램
- 렌더링 프로그램
- 웹 페이지 코드를 받으면 우리가 보는 화면처럼 바꿔주는 것

### 웹 페이지
- 웹에 있는 문서 (우리가 보는 화면 각각)
1. 정적 웹 페이지
- 한 번 작성된 HTML 파일의 내용이 변하지 않음
- 같은 상황에서 모든 사용자에게 동일한 정보 표시
> 서버가 없어도 됨 (HTML 파일만 있으면 됨)


2. 동적 웹 페이지
- 사용자의 요청에 따라 웹 페이지에 추가적인 수정이 되어 클라이언트에게 전달
- 웹 페이지의 내용을 바꿔주는 주체 == **서버**
- ex) 로그인, 장바구니 등

<br/><br/>

--- 
# Django 구조 (MTV Design Pattern)

자주 사용되는 구조 ➡️ 일반화해서 하나의 공법으로

### 소프트웨어 디자인 패턴
- 자주 사용되는 소프트웨어 구조를 일반적인 구조화 해둔 것
- 목적 : 재사용 가능한 해결책
- 장점 : 디자인 패턴을 알고 있다면 서로 복잡한 커뮤니케이션이 매우 간단해짐

**➡️ 다수의 엔지니어들이 일반화된 패턴으로 소프트웨어 개발을 할 수 있도록 한 규칙, 커뮤니케이션의 효율성을 높이는 기법**

<br/><br/>

## **Django ➡️ MTV 패턴**
### MVC 소프트웨어 디자인 패턴
Model - View - Controller
1. Model : 데이터와 관련된 로직 관리
2. View : 레이아웃, 화면 처리
3. Controller : 명령을 model과 view 부분으로 연결

|    MVC     |   MTV    |
| :--------: | :------: |
|   Model    |  Model   |
|    View    | Template |
| Controller |   View   |

➡️ 용어만 바뀐 것

<br/><br/>

### **MTV 디자인 패턴**
1. Model
- 데이터와 관련된 로직 관리
- 데이터 구조 정의, 데이터베이스 기록 관리
  > MVC 패턴에서 Model 역할 

<br/>

2. Template
- 레이아웃, 화면 처리
- 화면상의 사용자 인터페이스 구조, 레이아웃 정의
  > MVC 패턴에서 View 역할

<br/>

3. View
- Model & Template와 관련된 로직 처리, 응답 반환 <br/>
ex) 데이터가 필요하다면 model에 접근해서 데이터를 가져오고 <br/>
가져온 데이터를 template로 보내 화면을 구성하고  <br/>
구성된 화면을 응답으로 만들어 클라이언트에게 반환
  > MVC 패턴에서 Controller 역할

<br/><br/>

---

# Django 설치

1. 가상환경 설치 <br/>
`$ python -m venv venv`

<br/>

2. 가상환경 활성화 <br/>
`$ source venv/Scripts/activate`

<br/>

3. 가상환경 비활성화 <br/>
`$ deactivate`

<br/>

4. django 설치 <br/>
`$ pip install django==3.2.13`

<br/>

5. 패키지 목록 조회 (가상환경 켜면 그 내부 패키지만, 끄면 글로벌 패키지) <br/>
`$ pip list`

<br/>

6. requirements.txt 생성 <br/>
`$ pip freeze > requirements.txt`
- venv는 로컬에서만 작업 (용량 大) ➡️ 깃허브 업로드 X
- 가상환경 패키지 목록 기록 ➡️ 각 로컬에서 작업
- 코드 한번 더 입력하면 덮어씌우기 (패키지 추가 시)

<br/>

7. requirements.txt 목록 설치 <br/>
`pip install -r requirements.txt`
- requirements 파일을 읽으며 그 패키지들을 설치함

<br/>

8. django 프로젝트 생성 <br/>
`$ django-admin startproject firstpjt .`
- **. (현재 폴더)**을 빼먹지 않도록 주의

<br/>

9. django 서버 실행 <br/>
`$ python manage.py runserver`
- http://127.0.0.1:8000/

<br/>

> 애플리케이션 -- 하나의 기능 <br/>
> 여러 개의 애플리케이션 -> 프로젝트

<br/>

10. django 애플리케이션 생성 <br/>
`$ python manage.py startapp articles`
- articles : 애플리케이션 이름
- 애플리케이션 생성 시 -s 복수형으로 생성 (관례)

<br/>

11. INSTALLED_APPS에 앱을 등록
- firstpjt/settings.py 파일 내 INSTALLED_APPS에 'articles' 추가
- 사용자 앱을 맨 위에 넣는 것을 권장
- **반드시 생성 후 등록!!!**

<br/>

12. urls.py에 path 등록
> 메뉴판에 메뉴 등록^^

- urls.py 파일 내 urlpatterns의 path <br/>
`path('index/', views.index),` <br/>
`from articles import views`
- url의 끝 주소에는 / 적어주기
- 트레일링 콤마( , ) 적어주기 (확장성)

<br/>
 
13. views.py에 함수 생성 <br/>
- view 함수들이 정의 되는 곳
- MTV 패턴의 V에 해당
  ``` python
  def index(request):
      return render(request, 'index.html')
  ```
  ❗ request : views 내부의 함수의 첫번째 인자로 무조건 와야 함!!!!! 

<br/>

14.  template 생성 <br/>
- index.html 파일 생성

<br/>

15.  크롬에서 해당 URL로 요청 <br/>
`python manage.py runserver` 후 나오는 url에 주소창에서 /index 추가 시 해당 html로 이동

<br/>

## 🟡 코드 작성 순서 : URL ➡️ View ➡️ Template🟡

<br/><br/> 

### ➕ 추가 설정

- LANGUAGE_CODE : 번역 <br/>
  USE_I18N = True 여야만 사용 가능


- TIME_ZON : 시간대 <br/>
  USE_TZ = True 여야만 사용 가능

``` python
LANGUAGE_CODE = 'ko-kr'
TIME_ZONE = 'Asia/Seoul'
```

<br/><br/>

---

# Django Template
- 데이터 표현을 제어하는 도구이자 표현에 관련된 로직
- HTML 정적 부분과 동적 컨텐츠 삽입

<br/>

## Django Template Language (DTL)
- 조건, 반복, 변수 치환, 필터 등 기능 제공
- 프로그래밍적 로직 X // 단순 프리젠테이션 표현

<br/><br/>

## DTL Syntax
### 1. Variable
`{{ variable }}`
- 변수명 : 영어, 숫자, 언더바의 조합 But 언더바로는 시작할 수 없음
- dot(.)을 사용하여 변수 속성 접근 O
- render()의 세번째 인자로 딕셔너리 형태로 넘겨주며, key가 변수명이 됨
`return render(request, 'greeting.html', {'name':'alex'})`
`return render(request, 'greeting.html', context)`

``` python
def greeting(request):
    # context 데이터가 많아질 경우, 다음과 같이 작성하는 것이 바람직
    foods = ['apple', 'banana', 'coconut', 'mango', 'grape']
    info = {
        'name' : 'Alice',
    }

    # 다른 이름으로 사용 가능하지만, 관행적으로 context 사용 
    context = {
        'info' : info,
        'foods' : foods,
    }
    return render(request, 'articles/greeting.html', context)
```

<br/>

### 2. Filters
- 표시할 변수 수정
`{{ name|length }}` 
`{{ foods|join:" & " }}`
🔗 [Built-in filter reference](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#built-in-filter-reference)

<br/>

### 3. Tags
- 출력 텍스트를 만들거나, 반복 또는 논리를 수행하여 제어 흐름을 만드는 등 변수보다 복잡한 일들을 수행
- for문, if문 등
``` html
{% for food in foods %}
  {% if food|length > 6 %}
    <p>{{ food }}</p>
  {% endif %}
{% endfor %}
```
🔗 [Built-in tag reference](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#built-in-tag-reference)

<br/>

### 4. Comments
- 주석
- 한 줄 주석
`{# <p>이것은 주석입니다.</p> #}`

- 여러 줄 주석
``` html
{% comment %}
  <p>이것은 여러줄 주석입니다.</p>
  <p>이것은 여러줄 주석입니다.</p>
  <p>이것은 여러줄 주석입니다.</p>
{% endcomment %}
```

<br/><br/>

---
# Template inheritance (템플릿 상속)
- 코드의 재사용성에 초점 <br/>
### base.html

``` html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css">
  <title>firstpjt</title>
</head>
<body>
  {% block content %}
  {% endblock content %}
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css"></script>
</body>
</html>
```

- block 
`{% block content %}{% endblock  %}`
- extends - 반드시 탬플릿 최상단 위치!!!!
`{% extends 'base.html' %}`

<br/>

### 추가 템플릿 경로 추가하기
`'DIRS': [BASE_DIR / 'templates',],`

<br/><br/>

---
# Sending and Retrieving form data
form 데이터를 통해서 데이터를 보내고 가져오기

- 클라이언트-서버 구조

<br/>

## Sending form data (Client)
- HTML `<form>` element
  - 사용자로부터 할당된 데이터를 서버로 전송
  - 데이터를 담아서 요청
  - "데이터를 어디(action)로 어떤 방식(method)으로 보낼지"

    - action : 어디에? - URL
    - method : 어떻게? - HTTP request methods (GET, POST)
      - GET : 조회
      - POST : 생성

- HTML `<input>` element
  - 사용자로부터 데이터를 입력 받기 위해 사용
  - type 속성에 따라 동작 방식이 달라짐 (기본값 : text)
    - name : form을 통해 데이터를 제출했을 때 name 속성에 설정된 값을 서버로 전송 + 서버는 name 속성에 설정된 값을 통해 사용자가 입력한 데이터 값에 접근O


- HTML request method
GET, POST, PUT, DELETE

``` html
{% extends 'base.html' %}

{% block content %}
  <h1>Throw</h1>
  <form action="" method="GET">
    <label for="message">던져</label>
    <input type="text" id="message" name="message">
    <input type="submit">
  </form>
{% endblock %}
```

<br/>

## Retrieving form data (Server)
데이터 가져오기(검색하기)

``` html
{% extends 'base.html' %}

{% block content %}
  <h1>Catch</h1>
  <h2>여기서 데이터를 받았다</h2>
  <a href="/throw/">다시 던져라</a>
{% endblock %}
```

throw.html ➡️ `action="/catch/"`

- throw 페이지의 form이 보낸 데이터는 URL에 포함되어 서버로 보내짐

- "모든 요청 데이터는 view 함수의 첫번째 인자 request에 들어있다"


<br/><br/>

---

# Django URLs
- "Dispatcher로서의 URL 이해하기"
- 웹 어플리케이션은 URL을 통한 클라이언트의 요청에서부터 시작

## Trailing URL Slashes

- 모든 주소가 /로 끝나도록 구성

## Variable routing
- 템플릿의 많은 부분이 중복되고, 일부분만 변경되는 상황에서 비슷한 URL과 템플릿을 계속해서 만들지 않기 위해
- URL 주소를 변수로 사용
- URL의 일부를 변수로 지정하여 views 함수의 인자로 넘길 수 있음
- 즉, 변수 값에 따라 하나의 path()에 여러 페이지를 연결 시킬 수 있음
`path('hello/<name>/', views.hello),`
- 변수는 <>에 정의하며 views 함수의 인자로 할당됨
- 5가지 타입
  - str (기본값)
  - int `path('hello/<int:number>/', views.hello),`
  - slug
  - uuid
  - path

## App URL mapping
- 앱이 많아졌을 때 urls.py를 각 app에 매핑하는 방법

## Naming URL patterns

> DRY 원칙 (Don't Repeat Yourself)

---
### Django의 설계 철학
1. 표현과 로직을 분리
2. 중복을 배제

### Framework의 성격
- 독선적
- 관용적

### Django Framework의 성격
- 다소 독선적 : 양쪽 모두에게 최선의 결과를 준다고 강조

<br/><br/>

--- 

# Error
## 1. 폴더명은 정확하게
templates!!!!
template로 폴더명을 만들면, 그 내부에 있는 html 파일이 작동하지 않는다.
폴더명을 꼭 주의하자

## 2. base_html 사용 시에는 경로 추가 필수
프로젝트 폴더 내의 settings.py에서 'DIRS': [BASE_DIR / 'templates',], 를 해줘야 정상적으로 작동

## 3. Git 업로드 시
.gitignore 작성 필수
가상환경, 데이터베이스는 local에서만 사용 (용량 大)