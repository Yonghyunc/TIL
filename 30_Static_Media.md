# TIL

[Managing static files](#managing-static-files)

[Image Upload](#image-upload)

[Image Resizing](#image-resizing)

[QuerySet API Advanced](#queryset-api-advanced)


<br><br>

---

# Managing static files
개발자가 서버에 미리 준비한 혹은 사용자가 업로드한 정적파일을 클라이언트에게 제공하는 방법  

<br>

### 📌 정적 파일 (static file)
◽ 응답할 때 별도의 처리 없이 파일 내용을 그대로 보여주면 되는 파일  (요청한 것을 그대로)  
◽ 파일 자체가 고정되어 있음 (변경 X)  
◽ ex) 이미지, 자바스크립트, CSS 등

◽ 내장 앱 (별도로 앱 추가 X) **staticfiles**

<br>

### 📌 미디어 파일 (Media File)
◽ 사용자가 웹에서 업로드하는 정적 파일  
◽ 유저가 업로드한 모든 정적 파일  
> 미디어 파일을 정적 파일에 속함 

<br>

▶ 웹 서버의 기본 동작   
특정 위치(URL)에 있는 자원을 요청(HTTP request) 받아서  
응답(HTTP response)을 처리하고 제공(serving) 하는 것  

➡ "자원과 자원에 접근 가능한 주소가 있다"  

즉, 웹 서버는 요청 받은 URL로 서버에 존재하는 정적 자원을 제공

<br><br>

## static files 구성하기

1️⃣ INSTALLED_APPS 에 django.contrib.staticfiles 가 포함되어 있는지 확인
> 기본적으로 내장되어 있음


2️⃣ STATIC_URL 정의
> 기본적으로 정의되어 있음
``` python
STATIC_URL = '/static/'
```

3️⃣ 앱의 static 폴더에 정적 파일을 위치하기

4️⃣ 템플릿에서 static 템플릿 태그를 사용하여 지정된 경로에 있는 정적 파일의 URL 만들기

<br><br>

### ⭐ Django template tag

**{% load %}**  
◽ load tag  
◽ 특정 라이브러리, 패키지에 등록된 모든 템플릿 태그, 필터 업로드  
> 파이썬의 import문과 유사

<br>

**{% static '' %}**  
◽ static tag  
◽ STATIC_ROOT에 저장된 정적 파일에 연결  

<br><br>

### ⭐ Static files 관련 Core Settings
1️⃣ STATIC_ROOT  
◽ 기본값 : None  
◽ 장고 프로젝트에서 사용하는 모든 정적 파일을 한 곳에 모아 넣는 경로  
◽ 배포를 위해 정적 파일을 수집하는 디렉토리의 절대 경로  (개발 과정 사용 X)  
◽ 개발 과정에서 DEBUG 속성 값이 True 로 설정되어 있으면 해당 값 작용 X

> **소프트웨어 배포**  
> ◽ 프로그램 및 애플리케이션을 서버와 같은 기기에 설치하여 서비스를 제공하는 것   
> ◽ 클라우드 컴퓨팅 서비스(AWS, Google Cloud, MS Azure 등)에 프로그램 및 애플리케이션을 설치해 제공하는 것  

◽ 배포 환경에서 실행 시 다른 서버에 의해 실행되므로 정적 파일 경로를 알 수 없음 ➡ STATIC_ROOT

> **collectstatic**
> 
> ``` python
> STATIC_ROOT = BASE_DIR / 'staticfiles'
> ```
> `$ python manage.py collectstaticfiles`
> 
> 장고에서 기본적으로 만들어져 있는 admin 페이지를 구성하기 위한 폰트, 색상 등등 관련 정적 파일
> 
> 무슨 역할을 하는지만 알아두자! (결과 확인 후엔 삭제)

<br>

2️⃣ STATICFILES_DIRS  
◽ 기본값 : []  
◽ **app/static/** 디렉토리 경로를 사용하는 것 외에 추가적인 정적 파일 경로 목록을 정의하는 리스트  
``` python
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
```
<br>

3️⃣ STATIC_URL  
◽ 기본값 : None   
◽ STATIC_ROOT에 있는 정적 파일을 참조할 때 사용할 URL  
◽ 개발 단계에서는 app/static/ 경로, STATICFILES_DIRS 경로에서 탐색  
◽ **실제 파일이나 디렉토리 X, URL로만 존재**  
◽ 비어 있지 않은 값으로 설정 한다면 반드시 slash(/)로 끝나야 함  
``` python
STATIC_URL = '/static/'
```

<br><br> 

## Static files 사용하기 

### 🔹 static file 가져오기

#### 1️⃣ 기본 경로에 있는 static file 가져오기  (app/static/)  

❶ articles(앱)/static/rticles 경로에 이미지 파일 배치  
❷ static tag를 사용해 이미지 파일 출력  
`{% load static %}`
> extend 보다 아래쪽에 작성  

``` html
<img src="{% static 'articles/sample_img_1.jpg' %}" alt="sample1">
```
> block 안쪽에 작성

❸ 이미지 출력 확인

<br>

#### 2️⃣ 추가 경로에 있는 static file 가져오기 (STATICFILES_DIRS)
❶ 추가 경로 작성  
``` python
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
```
❷ static/ 경로에 이미지 파일 생성   
◽ 최상단에 static 폴더 생성   

❸ static tag를 사용해 이미지 파일 출력
`{% load static %}`

``` html
<img src="{% static 'sample_img_2.jpg' %}" alt="sample2">
```

❹ 이미지 출력 확인
![image](https://user-images.githubusercontent.com/93974908/194975400-0a9e6ae5-9c6b-4039-a5a9-7c0b1fad8d85.png)

<br><br>

### 🔹 STATIC_URL 확인하기  
실제 정적 파일이 제공되려면 이미지 주소 필요

http://127.0.0.1:8000/**static**/articles/sample_img_1.jpg   
중 static이 STATIC_URL   

◽ 이미지 파일을 요청하기 위한 주소  
![image](https://user-images.githubusercontent.com/93974908/194974409-e932ebd7-634f-4523-97da-485d9b32bc08.png)

<br><br>

---

# Image Upload
Django ImageField를 사용해 사용자가 업로드한 정적 파일 (미디어 파일) 관리하기  

<br>

### 📌 ImageField()
◽ 이미지 업로드에 사용하는 모델 필드  
◽ FileField를 상속 받음 ➡ FileField의 모든 속성 및 메서드를 사용 가능  
➕ 사용자에 의해 업로드된 객체가 유효한 이미지인지 검사  

◽ ImageField 인스턴스는 최대 길이가 100자인 문자열로 DB에 생성됨  
◽ max_length 인자를 사용하여 최대 길이 변경 가능  

<br>

### 📌 FileField()
◽ FileField(upload_to='', storage=None, max_length=100, **options)  
◽ 파일 업로드에 사용하는 모델 필드  
◽ 2개의 선택 인자 (upload_to, storage)

<br>

### 📌 FileField / ImageField를 사용하기 위한 단계  
1️⃣ settings.py에 **MEDIA_ROOT**, **MEDIA_URL** 설정   
2️⃣ **upload_to** 속성을 정의하여 업로드된 파일에 사용할 MEDIA_ROOT의 하위 경로 지정 (선택사항)
> MEDIA_ROOT/path  
> upload_to에 MEDIA_ROOT 뒤의 path를 작성

<br><br>

### ⭐ MEDIA_ROOT
◽ 기본값 : ''  
◽ 사용자가 업로드한 파일들을 보관할 디렉토리의 절대 경로  
◽ Django는 성능을 위해 업로드 파일은 DB에 저장 X ➡ **"파일 경로"** 저장  
◽ MEDIA_ROOT는 STATIC_ROOT와 반드시 다른 경로로 지정해야 함  
``` python
MEDIA_ROOT = BASE_DIR / 'media'
```

<br>

### ⭐ MEDIA_URL
◽ 기본값 : ''   
◽ MEDIA_ROOT에서 제공되는 미디어 파일을 처리하는 URL  
◽ 업로드된 파일의 주소(URL)를 만들어주는 역할  
◽ 비어 있지 않은 값으로 설정한다면 반드시 slash(/)로 끝나야 함  
◽ MEDIA_URL은 STATIC_URL과 반드시 다른 경로로 지정해야 함  
``` python
MEDIA_URL = '/media/'
```
<br>

➕ urls.py에서 경로를 추가해야 함  
[공식문서](https://docs.djangoproject.com/en/4.1/howto/static-files/#serving-static-files-during-development)

``` python
from django.contrib import admin
from django.urls import path, include
# 아래 두 줄
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
    path('accounts/', include('accounts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # 경로 추가
```
◽ 업로드된 파일의 URL == settings.MEDIA_URL  
◽ 위 URL을 통해 참조하는 파일의 실제 위치 == settings.MEDIA_ROOT  

<br><br>

## CREATE

❶ ImageField 작성  
``` python
# models.py

image = models.ImageField(blank=True)
```
> 실제로 데이터타입은 문자열, varchar(100)

> 기존 컬럼 사이 작성해도 실제 테이블에 추가될 때는 마지막에 추가됨  

#️⃣ Model field option  
**blank**   
◽ 기본값 : False  
◽ True 일 경우, 빈 문자열 허용  
◽ 유효성 검사에서 사용(is_valid)  

**null**  
◽ 기본값 : False  
◽ True 일 경우, 빈 값을 DB에 NULL로 저장  
  > ❗ null 관련 주의사항 ❗  
  >
  > "CharField, TextField와 같은 문자열 기반 필드에는 null 옵션 사용을 피해야 함"  
  > ➡ 데이터베이스의 일관성  
  > 문자열 기반 필드에 null=True로 설정 시, 데이터 없음에 대한 표현 : "빈 문자열" / "NULL"  
  >
  > Django는 문자열 기반 필드에서 NULL이 아닌 빈 문자열을 사용하는 것이 규칙 !! 

<br>

❷ Migration  
◽ ImageField 사용 위해서는 Pillow 라이브러리 설치 필요  
`$ pip install Pillow`

<br>

❸ image 필드 출력 확인  
![image](https://user-images.githubusercontent.com/93974908/194979004-9bbf381d-54c1-4261-8abb-a71e3912c2ec.png)
◽ 파일 / 이미지 업로드 시에는 form 태그에 **enctype 속성**을 변경해야 함 
``` html
<!-- enctype="multipart/form-data" -->

<form action="" method="POST" enctype="multipart/form-data">
```

#️⃣ form 태그의 enctype(인코딩) 속성 값  
**aplication/x-www-form-urlencoded**
◽ 기본값, 모든 문자 인코딩

**multipart/form-data**
◽ 파일/이미지 업로드 시 반드시 사용  
◽ 전송되는 데이터 형식 지정  
◽ `<input type="file">`을 사용할 경우 사용

**text/plain**
 
<br>


❹ request.FILES  
◽ 파일 및 이미지는 request의 POST 속성 값으로 넘어가지 않고 FILES 속성 값에 담겨 넘어감  
``` python
# views.py

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
...
```

<br>

❺ 이미지 첨부하기  

![image](https://user-images.githubusercontent.com/93974908/194981527-81a30d20-d22f-424c-bca2-693ba50c4cba.png)
> 이미지 첨부 X : 빈 문자열 저장  
> 이미지 첨부 O : "경로" 저장 + MEDIA_ROOT 경로에 이미지 업로드됨

◽ media 폴더 자동 생성   
![image](https://user-images.githubusercontent.com/93974908/194981476-b7923e00-a2ca-48b7-b2e4-85bec6cb5311.png)
> media 파일에 대한 경로를 settings.py에 작성해놨기 때문에 자동으로 생성됨  

#️⃣ 같은 이미지 업로드?
![image](https://user-images.githubusercontent.com/93974908/194981765-0d9ebbcb-10d8-4f70-88b1-f5ee15763ac8.png)
> 구분될 수 있도록 장고가 임의의 난수 값을 붙여 저장함  

<br><br>

## READ  
``` html
{% if article.image %}
  <img src="{{ article.image.url }}" alt="{{ article.image }}">
{% endif %}
```
◽ article.image.url : 업로드 파일 경로  
◽ article.image : 업로드 파일 이름  

◽ if문을 통해 이미지 데이터가 있는 경우만 이미지 출력할 수 있도록 처리  



<br><br>

## UPDATE
◽ 이미지는 바이너리 데이터이기 때문에 텍스트처럼 일부만 수정 X  
◽ 때문에 새로운 사진으로 대체하는 방식을 사용  

❶ enctype="multipart/form-data"  
❷ request.FILES  
❸


### upload_to 
1️⃣ 문자열 값이나 경로 지정 방법  
``` python
image = models.ImageField(blank=True, upload_to='images/')
```
``` python
image = models.ImageField(blank=True, upload_to='%Y/%m/%d/')
```

![image](https://user-images.githubusercontent.com/93974908/194999512-d12e72c9-06b2-4eee-9805-4a9fe226a75d.png)



2️⃣ 함수 호출 방법   
◽ 반드시 2개의 인자를 받음 (instance, filename)   

**instance**
◽ FileField가 정의된 모델의 인스턴스  
◽ 대부분 이 객체는 아직 DB에 저장되기 전이므로 아직 PK 값이 없을 수 있음  

**filename**  
◽ 기존 파일 이름  

``` python
def articles_image_path(instance, filename):
    return f'images/{instance.user.username}/{filename}'

image = models.ImageField(blank=True, upload_to=articles_image_path)
```
![image](https://user-images.githubusercontent.com/93974908/195000739-42faa5b4-e724-4d0b-85c0-9b3af38cb7da.png)


<br><br>

---

# Image Resizing
◽ 실제 원본 이미지를 서버에 그대로 로드 X  
➡ 업로드 시 이미지 자체를 resizing
> HTML `<img>` 태그에서 직접 사이즈 조정 가능 

<br>

◽ django-imagekit 모듈 설치 및 등록  
`$ pip install django-imagekit`

``` python
INSTALLED_APPS = [
    ...
    'django_extensions',
    'imagekit',
    ...
```
> 이미지 처리를 위한 Django 앱 
>> 썸네일, 해상도, 사이즈, 색깔 등 조정 O


<br><br>

## 썸네일 만들기  
### 1️⃣ 원본 이미지 저장 X

``` python
# models.py

from imagekit.processors import Thumbnail
from imagekit.models import ProcessedImageField


class Article(models.Model):
    image = ProcessedImageField(
        blank=True,
        upload_to='thumbnails/',
        processors=[Thumbnail(200,300)],
        format='JPEG',
        options={'quality': 80},
    )
```
> ProcessedImageField()의 파라미터로 작성된 값들은 makemigrations 후에 변경이 되더라도 다시 makemigrations를 해줄 필요없이 즉시 반영됨 

![image](https://user-images.githubusercontent.com/93974908/195008217-ce14b7a2-259f-4dbe-9839-464d7bba7a73.png)

<br>

### 2️⃣ 원본 이미지 저장 O
``` python
# models.py

from imagekit.processors import Thumbnail
from imagekit.models import ProcessedImageField, ImageSpecField


class Article(models.Model):
    image = models.ImageField(blank=True)
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[Thumbnail(200,300)],
        format='JPEG',
        options={'quality': 80},
    )
```


> 썸네일을 언제 만들어줘?  
> detail 페이지 수정

![image](https://user-images.githubusercontent.com/93974908/195008315-b1b13b73-332c-4c13-8f85-547b875b7e8f.png)


파일트리의 CACHE : 실제 출력이 이뤄졌을 때 생성됨  
![image](https://user-images.githubusercontent.com/93974908/195007896-bb13cd2b-de97-4713-a1c4-74ada53227ed.png)



<br><br>

---


# QuerySet API Advanced

![image](https://user-images.githubusercontent.com/93974908/195009586-a4bbe583-d2d6-4862-ae20-d6dd25fa3036.png)

![image](https://user-images.githubusercontent.com/93974908/195009625-085f8a63-1871-4485-a455-0b55d7caddf6.png)

![image](https://user-images.githubusercontent.com/93974908/195009668-8c19d692-e538-4aaa-858b-ed6bc5336fae.png)

![image](https://user-images.githubusercontent.com/93974908/195009877-67c708c8-f787-498d-b0b9-9c7628a6b0a9.png)

![image](https://user-images.githubusercontent.com/93974908/195009993-ea8c54d6-b9b1-4bf7-8793-6ec4aaba0007.png)

![image](https://user-images.githubusercontent.com/93974908/195010221-6c554295-33fc-48a2-ab7f-08fe095c1211.png)

.count()

<br><br>

## Sorting data
◽ 나이가 어린 순으로 이름과 나이 조회  
``` python
User.objects.order_by('age').values('first_name', 'age')
```

**order_by(*fields)** 
◽ 정렬  
◽ 기본 : 오름차순 정렬  
◽ 필드명에 '-'(하이픈)을 붙이면 내림차순 정렬  
◽ 인자로 '?'를 입력하면 랜덤 정렬 
``` python
User.objects.order_by('?').values('first_name', 'age')
```

**values(*fields, **expressions)** 
◽ 딕셔너리 요소들을 가진 QuerySet 반환  

<br>

◽ 이름과 나이를 나이가 많은 순서대로 조회  
``` python
User.objects.order_by('-age').values('first_name', 'age')
```
<br>

◽ 이름, 나이, 계좌 잔고를 나이가 어린 순으로, 만약 같은 나이라면 계좌 잔고가 많은 순으로 정렬해서 조회  
``` python
User.objects.order_by('age', '-balance').values('first_name', 'age', 'balance')
```
> order_by 주의사항
> `User.objects.order_by('balance').order_by('-age')`  
> 다음과 같이 쓸 경우 마지막 호출만 적용됨


<br><br>

## Filtering data

◽ 중복없이 모든 지역 조회  
``` python
User.objects.distinct().values('country')
```

◽ 지역 순으로 오름차순 정렬하여 중복없이 모든 지역 조회
``` python
User.objects.distinct().values('country').order_by('country')
```

◽ 이름과 지역이 중복없이 모든 이름과 지역 조회  
``` python
User.objects.distinct().values('first_name', 'country')
```

◽ 이름과 지역 중복없이 지역 순으로 오름차순 정렬하여 모든 이름과 지역 조회
``` python
User.objects.distinct().values('first_name', 'country').order_by('country')
```

◽ 나이가 30인 사람들의 이름 조회
``` python
User.objects.filter(age=30).values('first_name')
```

◽ 나이가 30살 이상인 사람들의 이름과 나이 조회
``` python
User.objects.filter(age__gte=30).values('first_name', 'age')
```

> **Field lookups**  
> 
> 필드명 뒤 '__' (double-underscore) 뒤에 작성  
> `field__lookuptype=value`
> filter(), exclude(), get()에 대한 키워드 인자로 사용됨  

◽ 나이가 30살 이상이고 계좌 잔고가 50만원 초과인 사람들의 이름, 나이, 계좌 잔고 조회
> 이상 : __gte  
> 초과 : __gt
``` python
User.objects.filter(age__gte=30, balance__gt=500000).values('first_name', 'age', 'balance') 
```

◽ 이름에 '호'가 포함되는 사람들의 이름과 성 조회
``` python
User.objects.filter(first_name__contains='호').values('first_name', 'last_name')
```

◽ 핸드폰 번호가 011로 시작하는 사람들의 이름과 핸드폰 번호 조회  
``` python
User.objects.filter(phone__startswith='011-').values('first_name', 'phone')
```

◽ 이름이 '준'으로 끝나는 사람들의 이름 조회
``` python
User.objects.filter(first_name__endswith='준').values('first_name')
```

◽ 경기도 혹은 강원도에 사는 사람들의 이름과 지역 조회
``` python
User.objects.filter(country__in=['경기도', '강원도']).values('first_name', 'country')
```

◽ 경기도 혹은 강원도에 살지 않는 사람들의 이름과 지역 조회
``` python
User.objects.exclude(country__in=['경기도', '강원도']).values('first_name', 'country')
```

**exclude()**
◽ 주어진 매개변수와 일치하지 않는 객체를 포함하는 QuerySet 반환


◽ 나이가 가장 어린 10명의 이름과 나이 조회
> sql에서 LIMIT
``` python
User.objects.order_by('age').values('first_name', 'age')[:10]
```
> QuerySet도 리스트와 같이 iterable 이기 때문에 슬라이싱 O

◽ 나이가 30이거나 성이 김씨인 사람들 조회 (OR)
> 기본적으로 filter()와 같은 메서드의 키워드 인자는 AND statement를 따름  

``` python
User.objects.filter(Q(age=30) | Q(last_name='김'))
```

**'Q' object**
◽ 각각의 조건을 변수에 담아, 그 변수들을 조합하여 더 복잡한 쿼리문을 만들 수 있음  
◽ '&' 및 '|'를 사용하여 Q객체를 결합할 수 있음  
> ,도 사용 가능

◽ 조회를 하면서 여러 Q객체를 제공할 수도 있음  

<br>

![image](https://user-images.githubusercontent.com/93974908/195019479-e7db64f7-6858-45fd-9d7b-bc063a3ad5d8.png)

<br><br>

## Aggregation (Grouping data)


**aggregate()**  
◽ 전체 queryset에 대한 값 계산   
◽ 딕셔너리 반환  

◽ Aggregation functions 
  - Avg, Count, Max, Min, Sum 등  


◽ 나이가 30살 이상인 사람들의 평균 나이 조회  
``` python
from django.db.models import Avg

User.objects.filter(age__gte=30).aggregate(Avg('age'))

# 딕셔너리 key 이름 수정 가능
User.objects.filter(age__gte=30).aggregate(평균=Avg('age'))
```


◽ 가장 높은 계좌 잔액 조회
``` python
from django.db.models import Max

User.objects.aggregate(Max('balance'))
```


◽ 모든 계좌 잔액 총액 조회
``` python
from django.db.models import Sum

User.objects.aggregate(Sum('balance'))
```

**annotate()**
◽ 쿼리의 각 항목에 대한 요약 값 계산  
◽ SQL의 GROUP BY에 해당  
◽ '주석을 달다' 라는 사전적 의미  


◽ 각 성씨가 몇 명씩 있는지 조회
``` python
from django.db.models import Count

User.objects.values('last_name').annotate(Count('last_name'))
```

◽ 각 지역별로 몇 명씩 살고 있는지 조회
``` python
from django.db.models import Count

User.objects.values('country').annotate(Count('country'))

# 딕셔너리 key 이름 수정 가능
User.objects.values('country').annotate(num_of_country=Count('country'))
```

◽ 각 지역별로 몇 명씩 살고 있는지 + 지역별 계좌 잔액 평균 조회
``` python
from django.db.models import Avg, Count

User.objects.values('country').annotate(num_of_country=Count('country'), avg_balance=Avg('balance'))
```
