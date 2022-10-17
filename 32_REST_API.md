# TIL 

[REST API](#rest-api)

[Response JSON](#response-json)

Django REST framework
- [Singel Model](#django-rest-framework---single-model)
- [N:1 Relation](#django-rest-framework---n1-relation)
- [N:1 역참조](#n1---역참조-데이터-조회)

<br><br>


---

## HTTP 
▫ HyperText Tranfer Protocol  
▫ HTML 문서와 같은 리소스들을 가져올 수 있도록 하는 프로토콜 (규약)  
▫ 웹 상에서 컨텐츠를 전송하기 위한 약속  
▫ 웹에서 이루어지는 모든 데이터 교환의 기초  

▫ "클라이언트 - 서버 프로토콜"  

▫ 클라이언트와 서버는 다음과 같은 개별적인 메시지 교환에 의해 통신  
- 요청 (request) : 클라이언트에 의해 전송되는 메시지  
- 응답 (response) : 서버에서 응답으로 전송되는 메시지

<br>

### ⭐ HTTP 특징  
▫ Stateless (무상태)  
- 동일한 연결에서 연속적으로 수행되는 두 요청 사이에 링크 X   
- 즉, 응답을 마치고 연결을 끊는 순간 클라이언트와 서버 간의 통신 종료 (상태 정보 유지 X)
  > 다음 요청 시, 이전 응답에 대한 내용 끌고갈 수 X 

So, 특정 페이지와 일관되게 상호작용 하고 싶으면  
➡ 쿠키 + 세션 사용하여 서버 상태를 요청과 연결  

<br>

### ⭐ HTTP Request Methods
= HTTP verbs  

▫ 리소스에 대해 수행할 원하는 작업을 나타내는 메서드 모음 정의  
➡ GET, POST, PUT, DELETE ...

> 📌 **리소스(resource)**  
> ▫ HTTP 요청의 대상

1️⃣ GET  
▫ 서버에 리소스의 표현 요청 (조회)  
▫ 데이터 검색에만 사용  

2️⃣ POST  
▫ 데이터를 지정된 리소스에 제출  
▫ 서버의 상태 변경 (생성, 수정 등)  

3️⃣ PUT   
▫ 요청한 주소의 리소스 수정  
 
4️⃣ DELETE   
▫ 지정된 리소스 삭제

<br>

### ⭐ HTTP response status codes 
▫ 특정 HTTP 요청이 성공적으로 완료되었는지 여부  

1️⃣ Informational responses (100-199)  

2️⃣ Succeccful responses (200-299)   

3️⃣ Redirection messages (300-399)  

4️⃣ Client error responses (400-499)  
▫ 400 : Bad Request (유효하지 않은 요청)  
▫ 401 : Unauthorized (인증되지 않은 사용자)  
▫ 403 : Forbidden (클라이언트 권한 없음)  
▫ 404 : Not found (요청한 경로 혹은 자원이 존재하지 않음)

5️⃣ Server error responses (500-599)  

> 요청에는 행동이 정의되어 있고, 응답에는 상태가 정의되어 있음

<br><br>

## 리소스 식별 
▫ 각 리소스는 식별을 위해 **URI**로 식별됨
- 자원의 **위치**로 자원을 식별 (URL)
- 고유한 **이름**으로 자원을 식별 (URN)

<br> 

### 🔹 URI
▫ Uniform Resource Identifier (통합 자원 식별자)  
▫ 인터넷에서 하나의 리소스를 가리키는 문자열  
▫ 가장 일반적인 URI는 URL (웹 주소)  
> 특정 이름공간에서 이름으로 리소스를 식별하는 URI는 URN  

<br>

### 🔹 URL 
▫ Uniform Resource Locator (통합 자원 위치)  
▫ 웹에서 주어진 리소스의 주소  

<br>

### 🔹 URL 구조

1️⃣ **Scheme** (or protocol)  
▫ 브라우저가 리소스를 요청하는 데 사용해야 하는 프로토콜  
▫ URL의 첫 부분은 브라우저가 어떤 규약을 사용하는지 나타냄  
▫ 기본적으로 웹은 HTTP(S)를 요구하며 메일을 열기위한 mailto:, 파일을 전송하기 위한 ftp: 등 다른 프로토콜도 존재  

2️⃣ **Authority** (권한)  
▫ Scheme 다음에 작성됨  
▫ :// 으로 구분  
▫ domain과 port를 모두 포함 (:으로 구분)  

1. Domain Name
    - 요청 중인 웹 서버 
    - 어떤 웹 서버가 요구되는지 
    - 직접 IP주소 사용도 가능, BUT 외우기 어려움 ➡ Domain Name 사용
2. Port
    - 웹 서버의 리소스에 접근하는데 사용되는 기술적인 문 
    - HTTP 프로토콜의 표준 포트 (생략 가능) 
      - HTTP - 80
      - HTTPS - 443
      > 나머지 포트는 생략 불가
    - Django의 경우 8000(80+00)이 기본 포트

3️⃣ **Path**  
▫ 웹 서버의 리소스 경로  
▫ 초기 : 실제 파일이 위치한 물리적 위치  
▫ 현재 : 추상화된 형태의 구조  


4️⃣ **Parameters**  
▫ 웹 서버에 제공하는 추가적인 데이터  
▫ '&' 기호로 구분되는 key-value 쌍 목록  
▫ 서버는 리소스 응답 이전 파라미터를 사용하여 추가 작업 수행 O

5️⃣ **Anchor**  
▫ 리소스의 다른 부분에 대한 앵커  
▫ "북마크" (브라우저에 해당 북마크 지점에 있는 콘텐츠 표시) 
> ex) 스크롤 이동  

▫ fragment identifier (부분 식별자)라고 부르는 '#' 이후 부분은 서버 전송 X  

> 하이퍼링크와 비슷한 기능을 하는 인터넷 사의 다른 문서와 연겨뢴 문자 혹은 그림  

<br>

> 📌 **URN**
> 
> ▫ Uniform Resource Name (통합 자원 이름)  
> ▫ URL과 달리 자원의 위치에 영향을 받지 않는 유일한 이름 역할 (독립적 이름)  
> ▫ URL의 단점 극복 위해 등장 ➡ 자원이 어디에 위치한지 여부와 관계없이 이름만으로 자원 식별  
> 
> **BUT**, 이름만으로 실제 리소스를 찾는 방법은 보편화 되어있지 않아 현재는 URL을 대부분 사용
> 
> ex)  
> ▫ ISBN (국제표준 도서번호)  
> ▫ ISAN (국제표준 시청각 자료번호)

<br><br>

# REST API 

## API
▫ Application Programming Interface  
▫ 애플리케이션과 프로그래밍으로 소통하는 방법  
> GUI으로 소통(그래픽)  ↔ CLI로 소통 (터미널창 등)  

▫ API를 제공하는 애플리케이션과 다른 소프트웨어 및 하드웨어 등의 것들 사이의 간단한 계약(인터페이스)이라고 볼 수 있음  
▫ API는 복잡한 코드를 추상화하여 대신 사용할 수 있는 몇 가지 더 쉬운 구문 제공  

<br>

### ⭐ Web API 
▫ 웹 서버 / 웹 브라우저를 위한 API  
▫ 현재 웹 개발은 여러 Open API를 활용하는 추세  
▫ 대표적인 Third Party Open API 서비스  
- Youtube API
- Naver Papago API
- Kakao Map API

▫ API는 다양한 타입의 데이터 응답 ➡  HTML, XML, JSON 등 

> 📌 **Open API**  
> 
> ▫ 누구나 사용할 수 있도록 공개된 API  
> ▫ 개발자에게 사유 응용 소프트웨어나 웹 서비스의 프로그래밍적 권한 제공 


<br>

## REST
▫ Representational State Transfer  
▫ API Server를 개발하기 위한 일종의 소프트웨어 설계 방법론  
▫ '소프트웨어 아키텍쳐 디자인 제약 모음'  
▫ REST 원리를 따르는 시스템 = **RESTful 한 API**  
▫ REST의 기본 아이디어는 **자원** ➡ 자원을 정의하고 자원에 대한 주소를 지정하는 전반적인 방법 서술  

<br>

### ⭐ REST에서 자원을 정의하고 주소를 지정하는 방법

1️⃣ 자원의 식별 ➡ URI

2️⃣ 자원의 행위 ➡ HTTP Method

3️⃣ 자원의 표현 ➡ JSON  
▫ 자원과 행위를 통해 궁극적으로 표현되는 추상화된 결과물  

> ctrl + p  
> settings.json

<br>

## JSON  
▫ lightweight data-interchange format  
▫ 자바스크립트의 표기법을 따른 단순 문자열  
▫ C 계열의 언어가 갖고 있는 자료구조로 쉽게 변환할 수 있는 key-value 형태의 구조  
> 파이썬 dictionary, 자바스크립트 object

▫ 사람이 읽고 쓰기 쉽고 기계가 파싱하고 만들어내기 쉬움 ➡ 현재 API에서 가장 많이 사용하는 데이터 타입  

<br><br>

---

# Response JSON
▫ JSON 형태로의 서버 응답 변화  

▫ JSON 데이터를 받아 화면을 구성하여 사용자에게 보여주는 것은 Front-end Framework가 담당  ➡ Vue.js

<br>

## Response

``` python
# my_api/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('articles.urls')),
]
```
``` python
# articles/urls.py

from django.urls import path
from . import views


urlpatterns = [
    path('html/', views.article_html),
    path('json-1/', views.article_json_1),
    path('json-2/', views.article_json_2),
    path('json-3/', views.article_json_3),
]
```

<br>



### 1️⃣ HTML 응답
▫ 지금까지 해오던 방식

``` python
from django.shortcuts import render
from .models import Article


def article_html(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/article.html', context)
```

``` html
<!DOCTYPE html>
<html lang="en">
<head>
  ...
</head>
<body>
  <h1>Article List</h1>
  <hr>
  <p>
    {% for article in articles %}
      <h2>{{ article.pk }}번 글. {{ article.title }}</h2>
      <p>{{ article.content }}</p>
      <hr>
    {% endfor %}
  </p>
</body>
</html>
```

<br>


### 2️⃣ JsonResponse()를 사용한 JSON 응답
▫ Django가 기본적으로 제공하는 JsonResponse 객체 활용하여 python 데이터 타입을 JSON으로 변환하여 응답  


``` python
from django.shortcuts import render
from django.http.response import JsonResponse
from .models import Article


def article_json_1(request):
    articles = Article.objects.all()
    articles_json = []

    for article in articles:
        articles_json.append(
            {
                'id': article.pk,
                'title': article.title,
                'content': article.content,
                'created_at': article.created_at,
                'updated_at': article.updated_at,
            }
        )
    return JsonResponse(articles_json, safe=False)
```
![image](https://user-images.githubusercontent.com/93974908/196095245-6e463661-1b49-4689-8e1e-aa126bdc1e3b.png)

<br>

#### 🚩 JsonResponse()  
▫ JSON-encoded response를 만드는 클래스  

▫ 'safe' parameter  
- 기본값 : True (dict 인스턴스만 serialization 가능)
- False : 모든 타입의 객체 serialization 가능

<br>

### 3️⃣ Django Serializer를 사용한 JSON 응답
▫ Django의 내장 HttpResponse() 활용


``` python
from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse
from django.core import serializers
from .models import Article


def article_json_2(request):
    articles = Article.objects.all()
    data = serializers.serialize('json', articles)
    return HttpResponse(data, content_type='application/json')
```

> 모델 구조 기반 -> 컬럼 명시 X 


![image](https://user-images.githubusercontent.com/93974908/196096133-8d4daaeb-6f15-41b0-92a5-5de774b43b5d.png)

<br>

#### 🚩 Serialization
▫ 직렬화  
▫ 데이터 구조나 객체 상태를 동일 혹은 다른 컴퓨터 환경에 저장하고, 나중에 재구성할 수 있는 포맷으로 변환하는 과정  

▶ 즉, 어떠한 언어나 환경에서도 **"나중에 다시 쉽게 사용할 수 있는 포맷으로 변환하는 과정**

▫ 변환 포맷 : **json**, xml, yaml 등

<br>

▫ serialize() : 복잡한 데이터를 JSON, XML 등의 유형으로 쉽게 변환할 수 있는 Python 데이터 타입으로 만들어 줌  

![image](https://user-images.githubusercontent.com/93974908/196096422-0856caa7-60fa-46b5-aba3-b0bd62be8d2e.png)

<br>

### 4️⃣ Django REST framework를 사용한 JSON 응답

#### 🚩 Django REST framework (DRF)
▫ Django에서 Restful API 서버를 쉽게 구축할 수 있도록 도와주는 오픈소스 라이브러리  
▫ Web API 구축을 위한 강력한 toolkit 제공  
▫ REST framework를 작성하기 위한 여러 기능 제공  

<br>

▫ 설치 후 등록 필요
``` python
# settings.py

INSTALLED_APPS = [
    ...
    'rest_framework',
    ...
]
```

▫ DRF의 serializer는 Django의 Form(ModelForm) 클래스와 매우 유사하게 작동  
``` python 
# articles/serializers.py

from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = '__all__'
```

``` python
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from .models import Article


# @api_view(['GET'])
@api_view()
def article_json_3(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)
```
> `serializer = ArticleSerializer(articles, many=True)` 이 serialize() 과정 

![image](https://user-images.githubusercontent.com/93974908/196097165-17268de5-7382-4081-91f0-affec353b573.png)



<br><br>

---

# Django REST framework - Single Model

▫ 단일 모델의 data를 Serialization하여 JSON으로 변환  

``` 
$ pip install djangorestframework
```

``` python
INSTALLED_APPS = [
    'articles',
    'django_extensions',
    'rest_framework',
    ...
]
```

<br>

## ModelSerializer 작성

▫ serializers.py 생성   
``` python
from rest_framework import serializers
from .models import Article


class ArticleListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        fields = ('id', 'title', 'content',)
```


### 🚩 ModelSerializer 클래스
▫ Model 정보에 맞춰 자동으로 필드 생성  
▫ serializer에 대한 유효성 검사기 자동 생성  
▫ .create() 및 .update()의 간단한 기본 구현 포함  

<br>

### Serializer 연습 (shell_plus)

``` shell
$ python manage.py shell_plus

>>> from articles.serializers import ArticleListSerializer
```

▫ 인스턴스 구조 확인
``` shell
>>> serializer = ArticleListSerializer()
>>> serializer
ArticleListSerializer():
    id = IntegerField(label='ID', read_only=True)
    title = CharField(max_length=100)
    content = CharField(style={'base_template': 'textarea.html'})
```

▫ Model instance 객체 serialize
``` shell
>>> article = Article.objects.get(pk=1)
>>> serializer = ArticleListSerializer(article)
>>> serializer
ArticleListSerializer(<Article: Article object (1)>):
    id = IntegerField(label='ID', read_only=True)
    title = CharField(max_length=100)
    content = CharField(style={'base_template': 'textarea.html'})

# serialized data 조회
>>> serializer.data
{'id': 1, 'title': 'Hair each base dark guess garden accept.', 'content': 'Religious ball another laugh light million. Federal public power another.\nDuring always recent maintain major others bank. Say place address. Wife tough outside system must. Develop road especially.'}
```

▫ QuerySet 객체 serialize

``` shell
>>> articles = Article.objects.all()
>>> serializer = ArticleListSerializer(articles)
>>> serializer.data
Traceback (most recent call last):
  ...
AttributeError: 'QuerySet' object has no attribute 'title'
```
> many=True 옵션이 아닐 시, 에러 발생

``` shell
>>> serializer = ArticleListSerializer(articles, many=True)
>>> serializer.data
[OrderedDict([('id', 1), ('title', 'Hair each base dark guess garden accept.'), ('content', ...
```

▫ QuerySet 또는 객체 목록을 serialize 하려면 **many=True**를 작성해야 함


<br><br>

## Build RESTful API - Article

### GET - List

▫ 게시글 데이터 목록 조회  
▫ DRF에서 `api_view` 데코레이터 작성은 필수!!! 

``` python
urlpatterns = [
    path('articles/', views.article_list)
]
```

``` python
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import ArticleListSerializer
from .models import Article


@api_view(['GET'])
def article_list(request):
    articles = Article.objects.all()
    serializer = ArticleListSerializer(articles, many=True)
    return Response(serializer.data)
```

▫ Postman  
![image](https://user-images.githubusercontent.com/93974908/196102553-62bb7d78-de67-4da3-bc09-abfb16b26c2c.png) 

<br>

#### 🚩 `api_view` decorator
▫ DRF view 함수가 응답해야 하는 HTTP 메서드 목록을 받음  
▫ 기본적으로 GET 메서드만 허용되며 다른 메서드 요청에 대해서는 405 Method Not Allowed로 응답  


<br><br>

### GET - Detail

▫ 단일 게시글 데이터 조회  

``` python
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
```
> 각 데이터의 상세 정보 제공

``` python
urlpatterns = [
    ...
    path('articles/<int:article_pk>/', views.article_detail),
]
```

```python
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import ArticleListSerializer, ArticleSerializer
from .models import Article


@api_view(['GET'])
def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    serializer = ArticleSerializer(article)
    return Response(serializer.data)
```

![image](https://user-images.githubusercontent.com/93974908/196103765-b4ecdba2-c658-4a92-b65c-d6174c0e6149.png)

<br><br>

### POST
▫ 게시글 데이터 생성  
▫ 성공 - 201 Created  
▫ 실패 - 400 Bad request

``` python
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .serializers import ArticleListSerializer, ArticleSerializer
from .models import Article


@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

![image](https://user-images.githubusercontent.com/93974908/196104785-cf0a15d8-9599-41ec-a865-95de1a27dba9.png)

> ArticleListSerializer - ArticleSerializer  
> : 어떤 필드를 출력할건지 차이  

<br>

#### 유효하지 않은 데이터에 대해 예외 발생시키기

![image](https://user-images.githubusercontent.com/93974908/196105183-2254dfba-14c6-4458-9a3c-2bf647f0b236.png)

▫ raise_exception 인자 사용 O
- DRF에서 제공하는 기본 예외 처리기에 의해 자동으로 처리되며 기본적으로 HTTP 400 응답 반환
``` python
elif request.method == 'POST':
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
```


<br><br>

### DELETE 
▫ 게시글 데이터 삭제  
▫ 성공 - 204 No Content 

``` python
@api_view(['GET', 'DELETE'])
def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```

![image](https://user-images.githubusercontent.com/93974908/196106672-aedad19a-79e7-4eb2-b578-9dc812907912.png)

<br><br>

### PUT

▫ 게시글 데이터 수정  
▫ 성공 - 200 OK

``` python
@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
```
> POST와 차이 : 앞쪽에 인스턴스 

> 200 상태 코드는 별도 명시 X 

![image](https://user-images.githubusercontent.com/93974908/196107553-bcec5b7c-13d2-4ec8-8f7d-929d6fdc99f5.png)

<br><br>

# Django REST framework - N:1 Relation

▫ N:1 관계에서의 모델 data를 Serialization하여 JSON으로 변환 

<br>

### GET - List
▫ 댓글 데이터 목록 조회  

``` python
from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
```

``` python
urlpatterns = [
    ...
    path('comments/', views.comment_list),
]
```
``` python
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import CommentSerializer
from .models import Comment

@api_view(['GET'])
def comment_list(request):
    if request.method == 'GET':
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
```

![image](https://user-images.githubusercontent.com/93974908/196109119-085105d3-90f5-44c8-9cd4-ec0d72bf65d2.png)


<br><br>

### GET - Detail
▫ 단일 댓글 데이터 조회  
> 같은 serializer 사용하였음

``` python 
urlpatterns = [
    ...
    path('comments/<int:comment_pk>/', views.comment_detail),
]
```

``` python
@api_view(['GET'])
def comment_detail(request, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)

    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
```

![image](https://user-images.githubusercontent.com/93974908/196110114-5b8e3971-7b4b-4c90-8a85-0bd48abd294b.png)

<br><br>

### POST
▫ 단일 댓글 데이터 생성  

``` python
urlpatterns = [
    ...
    path('articles/<int:article_pk>/comments/', views.comment_create),
]
```

``` python
@api_view(['POST'])
def comment_create(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
```
> 모델폼이 아니라 commit 존재 X -> 괄호에 바로 객체 할당

![image](https://user-images.githubusercontent.com/93974908/196111322-66027def-61de-4fb8-b48e-cefd5002dec2.png)
❌ 오류 발생  
모델에 존재하는 컬럼이므로 is.valid()로 검사함 -> BUT 나중에 들어가야 함   

▶ **읽기 전용 필드**  
'해당 필드를 **유효성 검사에서 제외**시키고 **데이터 조회 시에는 출력**'  

``` python
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',)
```

<br><br>

### DELETE & PUT
▫ 댓글 데이터 삭제 및 수정  

``` python
@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)

    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
```

<br><br>

## N:1 - 역참조 데이터 조회

### 1️⃣ 특정 게시글에 작성된 댓글 목록 출력 (기존 필드 override)
▫ Serializer 는 기존 필드를 override 하거나 추가적인 필드 구성 가능  

``` python
class ArticleSerializer(serializers.ModelSerializer):
    comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Article
        fields = '__all__'
```
> 댓글의 pk값만 출력됨

``` python
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',)


class ArticleSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = '__all__'
```
> 댓글에 대한 세부정보를 다 보고 싶으면

> 두 클래스의 상/하 위치 변경 필요  

<br><br>

### 2️⃣ 특정 게시글에 작성된 댓글 개수 출력 (새로운 필드 추가)
  
``` python
class ArticleSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)

    class Meta:
        model = Article
        fields = '__all__'
```
![image](https://user-images.githubusercontent.com/93974908/196182325-cc8bfb74-0134-4c06-a645-54622a509663.png)

> N쪽이 출력이 안 되기 때문에, override 하거나 새로운 컬럼을 추가하는 것이 필요 

#### 🚩 source
▫ serializers field's argument  
▫ 필드를 채우는 데 사용할 속성의 이름  
▫ 점 표기법을 사용하여 속성 탐색 가능  

<br>

> 특정 필드를 override / 추가한 경우, read_only_fields 동작 X   
> 
> Meta에서 read_only_fields를 사용하려면 테이블이 실제 물리적으로 존재해야 함


<br><br>

## Django shortcuts functions  

▫ render() 

▫ redirect()  

▫ get_object_or_404()  
: 모델 manager objects에서 get()을 호출하지만, 해당 객체가 없을 땐 기존 DoesNotExist 예외 대신 Http404를 raise 함  

``` python
# 기존 코드
article = Article.objects.get(pk=article_pk)

# 변경한 코드
article = get_object_or_404(Article, pk=article_pk)
```

▫ get_list_or_404()  
: 모델 manager objects에서 filter()의 결과를 반환하고, 해당 객체 목록이 없을 땐 Http404를 raise 함  

``` python
# 기존 코드
articles = Article.objects.all()

# 변경한 코드
articles = get_list_or_404(Article)
```