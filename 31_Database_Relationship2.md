# TIL
[Many-to-many relationship](#many-to-many-relationship-m--n)  

[ManyToManyField](#manytomanyfield)

[M:N (Article - User)](#mn-article---user)

<br><br>

---
# Many-to-many relationship (M : N)
◽ 한 테이블의 0개 이상의 레코드가 다른 테이블의 0개 이상의 레코드와 관련된 경우  
◽ 양쪽 모두에서 N:1 관계를 가짐  

<br>

> **데이터 모델링**  
> 
> ◽ 주어진 개념으로부터 논리적인 데이터 모델을 구성하는 작업  
> ◽ 물리적인 데이터베이스 모델로 만들어 고객의 요구에 따라 특정 정보 시스템의 데이터베이스에 반영하는 작업  

<br>

**target model**  
◽ 관계 필드를 가지지 않은 모델  

**source model**  
◽ 관계 필드를 가진 모델  

> Comment(N) - Article(1) 관계에서  (Comment --> Article 참조)  
>  
> ◽ Comment : source model  
> ◽ Article : target model

<br><br>

## N:1 의 한계  
환자(N) - 의사(1) 모델  
``` python 
from django.db import models


class Doctor(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'


class Patient(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'
```
``` python
# 각각 2명의 의사와 환자를 생성하고 환자는 서로 다른 의사에게 예약 했다고 가정

In [1]: doctor1 = Doctor.objects.create(name='alice')

In [2]: doctor2 = Doctor.objects.create(name='bella')

In [3]: patient1 = Patient.objects.create(name='carol', doctor=doctor1)

In [4]: patient2 = Patient.objects.create(name='dane', doctor=doctor2)

In [5]: doctor1
Out[5]: <Doctor: 1번 의사 alice>

In [6]: doctor2
Out[6]: <Doctor: 2번 의사 bella>

In [7]: patient1
Out[7]: <Patient: 1번 환자 carol>

In [8]: patient2
Out[8]: <Patient: 2번 환자 dane>

# 1번 환자(carol)가 두 의사 모두에게 방문하려고 함
# 동일한 환자지만 다른 의사에게 예약하기 위해서는 객체를 하나 더 만들어서 예약을 진행해야 함
In [9]: patient3 = Patient.objects.create(name='carol', doctor=doctor2)

In [10]: patient3
Out[10]: <Patient: 3번 환자 carol>

# 동시에 예약 불가
In [11]: patient4 = Patient.objects.create(name='carol', doctor=doctor1, doctor2)
  File "<ipython-input-11-d8f6d418c249>", line 1
    patient4 = Patient.objects.create(name='carol', doctor=doctor1, doctor2)
                                                                           ^
SyntaxError: positional argument follows keyword argument
```


<br><br>

## 중개모델
◽ 환자 모델의 외래 키를 삭제하고 별도의 예약 모델을 새로 작성  

``` python
from django.db import models


class Doctor(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'


class Patient(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'


class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.doctor_id}번 의사의 {self.patient_id}번 환자'
```

◽ Reservation에서는 Doctor과 Patient에 바로 접근 가능  

◽ _set 사용하여 역참조

``` python
In [1]: doctor1 = Doctor.objects.create(name='alice')

In [2]: patient1 = Patient.objects.create(name='carol')

In [3]: doctor1
Out[3]: <Doctor: 1번 의사 alice>

In [4]: patient1
Out[4]: <Patient: 1번 환자 carol>

In [5]: Reservation.objects.create(doctor=doctor1, patient=patient1)
Out[5]: <Reservation: 1번 의사의 1번 환자>

# 의사 -> 예약 : 1번 의사가 본인에게 예약된 모든 환자 조회
In [6]: doctor1.reservation_set.all()
Out[6]: <QuerySet [<Reservation: 1번 의사의 1번 환자>]>

# 환자 -> 예약 : 1번 환자가 어떤 의사들을 방문해야 하는지 조회
In [7]: patient1.reservation_set.all()
Out[7]: <QuerySet [<Reservation: 1번 의사의 1번 환자>]>

In [8]: patient2 = Patient.objects.create(name='dane')

# 1번 의사에게 새로운 환자 예약 생성
In [9]: Reservation.objects.create(doctor=doctor1, patient=patient2)
Out[9]: <Reservation: 1번 의사의 2번 환자>

# 1번 의사의 예약 정보 조회
In [10]: doctor1.reservation_set.all()
Out[10]: <QuerySet [<Reservation: 1번 의사의 1번 환자>, <Reservation: 1번 의사의 2번 환자>]>
```

<br><br>

## Django ManyToManyField
``` python
from django.db import models


class Doctor(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'


class Patient(models.Model):
    doctors = models.ManyToManyField(Doctor)
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'
```
◽ manytomany를 어디 썼는지에 따라 참조와 역참조 관계만 달라짐  

> patient에 썼을 때,
> patient ---참조---> doctor  
> patient <--역참조-- doctor  
> 종속관계 X  

◽ 단, 어디에 작성되었는지에 따라 테이블명은 바뀜 (크게 의미 X)  


``` python
In [1]: doctor1 = Doctor.objects.create(name='alice')

In [2]: patient1 = Patient.objects.create(name='carol')

In [3]: patient2 = Patient.objects.create(name='dane')


# 1번 환자가 1번 의사에게 예약
In [4]: patient1.doctors.add(doctor1)

# patient1 - 자신이 예약한 의사목록 확인 
In [5]: patient1.doctors.all()
Out[5]: <QuerySet [<Doctor: 1번 의사 alice>]>

# doctor1 - 자신의 예약된 환자목록 확인 (역참조)
In [6]: doctor1.patient_set.all()
Out[6]: <QuerySet [<Patient: 1번 환자 carol>]>


# 의사가 환자를 예약
In [7]: doctor1.patient_set.add(patient2)

# doctor1 - 자신의 예약된 환자목록 확인 (역참조)
In [8]: doctor1.patient_set.all()
Out[8]: <QuerySet [<Patient: 1번 환자 carol>, <Patient: 2번 환자 dane>]>

# patient1 - 자신이 예약한 의사목록 확인 
In [9]: patient2.doctors.all()
Out[9]: <QuerySet [<Doctor: 1번 의사 alice>]>


# 예약 취소
# doctor가 patient 진료 예약 취소
In [10]: doctor1.patient_set.remove(patient1)

In [14]: doctor1.patient_set.all()
Out[14]: <QuerySet [<Patient: 2번 환자 dane>]>

# patient가 doctor 진료 예약 취소
In [15]: patient2.doctors.remove(doctor1)

In [16]: patient2.doctors.all()
Out[16]: <QuerySet []>
```

◽ Django는 ManyToManyField를 통해 중개 테이블을 자동으로 생성함  

<br>

> 의사.patient_set.  
> 환자.doctors.  
> -> 통일하면 좋지 않을까?

### ⭐ related_name  
역참조 시 이름 변경  
``` python
class Patient(models.Model):
    doctors = models.ManyToManyField(Doctor, related_name='patients')
```

``` python
In [1]: doctor1 = Doctor.objects.create(name='alice')

# related_name을 설정하면 기존 _set manager는 사용 X
In [2]: doctor1.patient_set.all()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-2-e81b89c43a95> in <module>
----> 1 doctor1.patient_set.all()

AttributeError: 'Doctor' object has no attribute 'patient_set'

In [3]: doctor1.patients.all()
Out[3]: <QuerySet []>
```
<br>

### ⭐ through
◽ 중개 테이블을 수동으로 지정하려는 경우 through 옵션 사용  
◽ 중개 테이블에 추가 데이터 사용하려는 경우 사용  


``` python
from django.db import models


class Doctor(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'


class Patient(models.Model):
    doctors = models.ManyToManyField(Doctor, related_name='patients', through='Reservation')
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'


class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    symptom = models.TextField()
    reserved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.doctor_id}번 의사의 {self.patient_id}번 환자'
```
◽ through 설정  
◽ Reservation Class 수정 (+ 증상, 예약일)  



``` python
In [1]: doctor1 = Doctor.objects.create(name='alice')

In [2]: patient1 = Patient.objects.create(name='carol')

In [3]: patient2 = Patient.objects.create(name='dane')

# 1. Reservation class를 통한 예약 생성
In [4]: reservation1 = Reservation(doctor=doctor1, patient=patient1, symptom='headache')

In [5]: reservation1.save()

In [6]: reservation1
Out[6]: <Reservation: 1번 의사의 1번 환자>

# 2. Patient 객체를 통한 예약 생성
In [6]: patient2.doctors.add(doctor1, through_defaults={'symptom':'flu'})
```

<br><br>

---

# ManyToManyField
◽ ManyToManyField(to, **options)  
◽ 다대다(M:N) 관계 설정 시 사용하는 모델 필드  
◽ 하나의 필수 위치인자 (M:N 관계로 설정할 모델 클래스)가 필요  
◽ 모델 필드의 RelatedManager를 사용하여 관련 개체 추가, 제거, 생성 등 가능  
- add(), remove(), create(), clear(), ...

<br>

### ▶ 데이터베이스에서의 표현  
◽ Django는 다대다 관계를 나타내는 중개 테이블을 만듦  
◽ 테이블 이름 : ManyToManyField 이름 + 이를 포함하는 모델의 테이블 이름
◽ **'db_tale'** : 중개 테이블 이름 변경 

<br>

## ManyToManyField's Arguments
### 1️⃣ related_name  
◽ target model이 source model을 참조할 때 사용할 manager name  
◽ ForeignKey의 related_name과 동일  

### 2️⃣ through  
◽ 중개 테이블을 직접 작성하는 경우, 중개 테이블을 나타내는 Django 모델 지정  
◽ 일반적으로 중개 테이블에 추가 데이터를 사용하는 다대다 관계와 연결하려는 경우 사용  

### 3️⃣ symmetrical  
◽ 기본값 : True  
◽ 자기 자신과 다대다 관계를 설정할 때만 사용  (대칭)  

◽ True일 경우,
- _set 매니저를 추가 하지 않음 
- 대칭 관계 (팔로우 시 자동 맞팔로우)

◽ 대칭을 원하지 않는 경우 False로 설정 

<br>

## Related Manager
◽ N:1 혹은 M:N 관계에서 사용 가능한 문맥  
◽ Django는 모델 간 N:1 혹은 M:N 관계가 설정되면 역참조시에 사용할 수 있는 manager 생성  

◽ 같은 이름의 메서드여도 각 관계(N:1, M:N)에 따라 다르게 사용 및 동작됨
- N:1에서는 target 모델 객체만 사용 가능
- **M:N 관계에서는 관련된 두 객체에서 모두 사용 가능**  

◽ 메서드 종류 : **add()**, **remove()**, create(), clear(), set() 등  

### add()
◽ "지정된 객체를 관련 객체 집합에 추가"  
◽ 이미 존재하는 관계에 사용하면 관계 복제 X  
◽ 모델 인스턴스, 필드 값(PK)을 인자로 허용  

### remove()
◽ "관련 객체 집합에서 지정된 모델 개체를 제거"  
◽ 내부적으로 QuerySet.delete()를 사용하여 관계가 삭제됨  
◽ 모델 인스턴스, 필드 값(PK)을 인자로 허용 

<br>

### 중개 테이블 필드 생성 규칙  
1️⃣ source model != target model  
◽ id  
◽ <containing_model>_id  
◽ <other_model>_id

2️⃣ ManyToManyField가 동일한 모델을 가리키는 경우  
◽ id  
◽ from_<model>_id  
◽ to_<model>_id  


<br><br>

---

# M:N (Article - User)
좋아요👍 기능 구현  

<br>

### 1️⃣ like_users 필드 추가 
``` python
like_users = models.ManyToManyField(settings.AUTH_USER_MODEL)
```

```
ERRORS:
articles.Article.like_users: (fields.E304) Reverse accessor for 'articles.Article.like_users' clashes with reverse accessor for 'articles.Article.user'.
```
◽ 역참조 name이 같음 -> 둘 중 하나를 related_name 설정  
◽ 이런 상황에서 주로 어떤걸 바꿀까?  - 일반적으로 M:N을 바꿈  

Article:User (N:1)  
article.user  
**user.article_set**  

Article:User (M:N)  
article.like_users  
**user.article_set** => like_articles


``` python
# articles/models.py

from django.db import models
from django.conf import settings


class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
```


![image](https://user-images.githubusercontent.com/93974908/195233359-a82fc1fd-1830-439b-baba-f1b1cff6f29c.png)


<br>

### ✔ User - Article 간 사용 가능한 related manager 정리  
◽ article.user : 게시글을 작성한 유저 - N:1

◽ user.article_set : 유저가 작성한 게시글(역참조) - N:1

◽ article.like_users : 게시글을 좋아요한 유저 - M:N

◽ user.like_articles : 유저가 좋아요한 게시글(역참조) - M:N  

<br><br>

### 2️⃣ LIKE 구현

▶ url
``` python
path('<int:article_pk>/likes/', views.likes, name='likes'),
```
<br>

▶ view  
``` python
# articles/views.py

def likes(request, article_pk):
    article = Article.objects.get(pk=article_pk)

    # 좋아요 추가할지 취소할지 무슨 기준으로 if문 작성?!
    # 현재 게시글에 좋아요를 누른 유저 목록에 현재 좋아요를 요청하는 유저가 있는지 없는지를 확인
    # if request.user in article.like_users.all():

    # 현재 게시글에 좋아요를 누른 유저 중에 현재 좋아요를 요청하는 유저를 검색하여 존재하는지 확인
    if article.like_users.filter(pk=request.user.pk).exists():
        # 좋아요 취소 (remove) 
        article.like_users.remove(request.user)
    else:
        # 좋아요 추가 (add)
        article.like_users.add(request.user)
    return redirect('articles:index')
```
◽ POST 요청만 받음  
◽ 로그인된 사용자만 좋아요 기능 사용할 수 있도록 함   

> in 연산자는 데이터의 크기가 커지면 비효율적 

&nbsp; ⬇
### .exists()
✔ QuerySet에 결과가 포함되어 있으면 True를 반환하고 그렇지 않으면 False 반환  
✔ 특히 큰 QuerySet에 있는 특정 개체의 존재와 관련된 검색에 유용  

<br>

▶ template
``` html
<!-- articles/index.html -->

<div>
  <form action="{% url 'articles:likes' article.pk %}" method="POST">
    {% csrf_token %}
    {% if request.user in article.like_users.all %}
      <input type="submit" value="좋아요 취소">
    {% else %}
      <input type="submit" value="좋아요">
    {% endif %}
  </form>
</div>
```
![image](https://user-images.githubusercontent.com/93974908/195272093-7660f2d3-66f0-4fc1-a0fb-4d48a2dc9224.png)

<br><br>

### 3️⃣ 데코레이터 & is_authenticated 추가
▶ view  
``` python
# articles/views.py

@require_POST
def likes(request, article_pk):
    if request.user.is_authenticated:
        article = Article.objects.get(pk=article_pk)

        if article.like_users.filter(pk=request.user.pk).exists():
            article.like_users.remove(request.user)

        else:
            article.like_users.add(request.user)

        return redirect('articles:index')
      
    return redirect('accounts:login')
```
◽ POST 요청만 받음  
◽ 로그인된 사용자만 좋아요 기능 사용할 수 있도록 함   


<br><br>

# M:N (User - User)
팔로우 기능 구현 

<br>

## Profile
### ▶ url  
``` python
path('profile/<str:username>/', views.profile, name='profile'),
```

> ❗ 주의사항 ❗
> 
> `path('<str:username>/', views.profile, name='profile')`  
> url에서 profile을 빼버리고 해당 url을 제일 위로 보내면,  
> 모든 문자열 url이 전부 해당 경로로 가버림  
> 즉, 아래의 모든 path가 다 죽어버림  
> 제일 아래에 있으면 상관 없겠지만, 확장성을 위하여 저렇게 사용 X  

<br>

### ▶ view  
``` python
# accounts/views.py

from django.contrib.auth import get_user_model


def profile(request, username):
    User = get_user_model()
    person = User.objects.get(username=username)

    context = {
        'person': person,
    }
    return render(request, 'accounts/profile.html', context)
```
<br>

### ▶ template  

◽ 누구의 프로필  
◽ 누가 작성한 게시글 목록  
◽ 누가 작성한 댓글 목록   
◽ 누가 좋아요한 게시글 목록    

``` html
<!-- accounts/profile.html -->

{% extends 'base.html' %}

{% block content %}
  <h1>{{ person.username }}님의 프로필</h1>
  <hr>

  <h2>{{ person.username }}이 작성한 모든 게시글</h2>
  {% for article in person.article_set.all %}
    <div>{{ article.title}}</div>
  {% endfor %}
  <hr>

  <h2>{{ person.username }}이 작성한 모든 댓글</h2>
  {% for comment in person.comment_set.all %}
    <div>{{ comment.content }}</div>
  {% endfor %}
  <hr>

  <h2>{{ person.username }}이 좋아요한 모든 게시글</h2>
  {% for article in person.like_articles.all %}
    <div>{{ article.title }}</div>
  {% endfor %}

  <a href="{% url 'articles:index' %}">back</a>
{% endblock content %}
```
<br>

◽ base.html 에 내 프로필 바로가기 추가
``` html
<!-- base.html-->

<a href="{% url 'accounts:profile' user.username %}">내 프로필</a>
```
![image](https://user-images.githubusercontent.com/93974908/195260998-c08544dc-25e6-42c8-9a07-f669e5964775.png)

<br>

◽ 작성자 이름을 누르면 작성자 프로필로 가기
``` html
<!-- articles/index.html -->

  {% for article in articles %}
    <p>
      <b>작성자 : <a href="{% url 'accounts:profile' article.user %}">{{ article.user }}</a></b>
    </p>
    <p>글 번호 : {{ article.pk }}</p>
    <p>제목 : {{ article.title }}</p>
    <p>내용 : {{ article.content }}</p>
    ...
  {% endfor %}
```
> article.user !!!!! 

<br><br>

## Follow

### ▶ model
``` python
# accounts/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
```
<br>

### ▶ url
``` python
path('<int:user_pk>/follow/', views.follow, name='follow'),
```

<br>

### ▶ view
``` python
# accounts/views.py

def follow(request, user_pk):
    User = get_user_model()
    me = request.user
    you = User.objects.get(pk=user_pk)
    if me != you:
        # 내가(request.user) 그 사람의 팔로워 목록에 있다면
        # if me in you.followers.all():
        if you.followers.filter(pk=me.pk).exists():
            # 언팔로우
            you.followers.remove(me)

        else:
            # 팔로우
            you.followers.add(me)
    return redirect('accounts:profile', you.username)
```
<br>

### ▶ template
◽ 팔로우 / 언팔로우 버튼
``` html
<!-- accounts/profile.html -->

  {% if request.user != person %}
    <div> 
      <form action="{% url 'accounts:follow' person.pk %}" method="POST">
        {% csrf_token %}
          {% if request.user in person.followers.all %}
          <input type="submit" value="언팔로우">
          {% else %}
          <input type="submit" value="팔로우">
          {% endif %}
      </form>
    </div>
  {% endif %}
```

<br>

◽ 팔로워 / 팔로잉 수 
``` html
<!-- accounts/profile.html -->

  <div>
    팔로워 : {{ person.followers.all|length }} / 팔로잉 : {{ person.followings.all|length }}
  </div>
```
![image](https://user-images.githubusercontent.com/93974908/195272313-ebe53078-7c4a-4c38-b5fa-12ff1498ab0b.png)
<br>

### ▶ 데코레이터 & is_authenticated 추가
``` python
@require_POST
def follow(request, user_pk):
    if request.user.is_authenticated():
        User = get_user_model()
        me = request.user
        you = User.objects.get(pk=user_pk)
        if me != you:
            # 내가(request.user) 그 사람의 팔로워 목록에 있다면
            # if me in you.followers.all():
            if you.followers.filter(pk=me.pk).exists():
                # 언팔로우
                you.followers.remove(me)

            else:
                # 팔로우
                you.followers.add(me)
        return redirect('accounts:profile', you.username)
    return redirect('accounts:login')
```


<br><br>

---

# ➕ Fixtures
## 초기 데이터의 필요성  

◽ Django 프로젝트의 앱을 처음 설정할 때 동일하게 준비된 데이터로 DB를 미리 채우는 것이 필요한 순간 O  

◽ Django에서는 fixtures를 사용해 앱에 초기 데이터 제공  

◽ 즉, migrations와 fixtures를 사용해 data와 구조 공유  

<br>

## 초기 데이터 제공  

### fixtures
◽   

◽ 기본 경로 :   `app_name/fixtures/`

◽ 생성 (추출) : dumpdata  
```
$ python manage.py dumpdata [app_name[.ModelName] [app_name[.ModelName] ...]] > {filename}.json
```
``` json
[{"model": "articles.article", "pk": 1, "fields": {"user": 1, "title": "���ƿ�", "content": "�� ���ƿ�", "created_at": "2022-10-12T04:52:22.265Z", "updated_at": "2022-10-12T04:52:22.265Z", "like_users": [1, 2]}}, {"model": "articles.article", "pk": 2, "fields": {"user": 1, "title": "��", "content": "����", "created_at": "2022-10-12T05:39:26.460Z", "updated_at": "2022-10-12T05:39:26.460Z", "like_users": [1, 2]}}, {"model": "articles.article", "pk": 3, "fields": {"user": 2, "title": "2��", "content": "�ۼ���", "created_at": "2022-10-12T05:53:59.230Z", "updated_at": "2022-10-12T05:53:59.230Z", "like_users": [2]}}]
```
<br>

```
$ python manage.py dumpdata --indent 4 [app_name[.ModelName] [app_name[.ModelName] ...]] > {filename}.json
```
``` json
[
{
    "model": "articles.article",
    "pk": 1,
    "fields": {
        "user": 1,
        "title": "���ƿ�",
        "content": "�� ���ƿ�",
        "created_at": "2022-10-12T04:52:22.265Z",
        "updated_at": "2022-10-12T04:52:22.265Z",
        "like_users": [
            1,
            2
        ]
    }
},
{
    "model": "articles.article",
    "pk": 2,
    "fields": {
        "user": 1,
        "title": "��",
        "content": "����",
        "created_at": "2022-10-12T05:39:26.460Z",
        "updated_at": "2022-10-12T05:39:26.460Z",
        "like_users": [
            1,
            2
        ]
    }
},
{
    "model": "articles.article",
    "pk": 3,
    "fields": {
        "user": 2,
        "title": "2��",
        "content": "�ۼ���",
        "created_at": "2022-10-12T05:53:59.230Z",
        "updated_at": "2022-10-12T05:53:59.230Z",
        "like_users": [
            2
        ]
    }
}
]
```
```
$ python manage.py dumpdata --indent 4 articles.article > articles.json

$ python manage.py dumpdata --indent 4 articles.comment > comments.json

$ python manage.py dumpdata --indent 4 accounts.user > users.json

```
> 앱 폴더 하위에 fixtures 폴더 만들어서 json 파일 보관 

<br>

◽ 로드 (불러오기) : loaddata

```
$ python manage.py migrate

$ python manage.py loaddata articles.json comments.json users.json
```
> 한번에 로드할 때는 순서 상관 X  
> 따로 할 때는 순서 상관 있을 수도 (관계에 따라)  
> users -> articles -> comments

<br><br>

---

# Improve Query
최적화  

