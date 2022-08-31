# Today I Learned
- Namespace
- Django Model
- 


<br/><br/>

---
# Namespace (이름공간)
개체를 구분할 수 있는 범위


<br/>

### 🔔 다른 앱에 같은 이름의 파일이 있을 때 2가지 문제 발생

< 해결책 >

#### 1. URL 이름 공간 <br/>
  `app_name = 'articles'`
    ➡️ 태그 사용 변화 `{% url 'articles:index' %}` (app_name:url_name)

<br/>

#### 2. 템플릿 이름 공간 - url은 잘 갔는데 응답을 엉뚱한 페이지를 함
- Django는 기본적으로 app_name/templates/경로에 있는 파일을 찾음 <br/>
  ➡️ articles/templates/ 와 pages/templates/ 가 존재
- 파일명이 겹치는 경우, 앱의 등록 순서에 따라 찾음

- But, 기본 경로를 바꿀 수는 없음
- 물리적으로 이름공간 만들어줘야 함 
`articles/templates/articles/index.html`
`pages/templates/pages/index.html`

> ❔ 반드시 template namespace를 고려해야 할까 ❔  <br/>
> 
> 단일 앱 프로젝트라면 상관 X  <br/>
> 하지만, 여러 앱을 사용할거라면 고려하는 것이 좋음

<br/><br/>

---

# Django Model
- Django는 웹 애플리케이션의 데이터를 구조화하고 조작하기 위핸 추상적인 계층(모델) 제공

<br/><br/>


## 💾 Database
- 체계화된 데이터의 모임
- 검색 및 구조화 같은 작업을 보다 쉽게 하기 위해 조직화된 데이터를 수집하는 저장 시스템


<br/>

### 1. 스키마(Schema)
  > 요약본  
- 뼈대(structure)
- 데이터베이스에서 자료 구조, 표현 방법, 관계 등을 정의한 구조

<br/>

### 2. 테이블(Table)
- 필드와 레코드를 사용해 조직된 데이터 요소들의 집합 <br/>
= 관계(relation) <br/>

    1. 필드(field)
        - 속성, 컬럼
        - 각 필드에는 고유한 데이터 형식 지정 (INT, TEXT 등)
    2. 레코드(record)
        - 실제 데이터
        - 튜플, 행
        - 테이블의 데이터는 레코드에 저장됨

<br/>

### 🔑 PK(Primary Key)
  - 기본 키
  - 각 레코드의 고유한 값 (식별자)
  - 다른 항목과 절대 중복될 수 없는 단일 값 (unique)

<br/>

### 📑 쿼리(Query)
  - 데이터를 조회하기 위한 명령어
  - 조건에 맞는 데이터를 추출하거나 조작하는 명령어
  - "Query를 날린다" == "데이터베이스를 조작한다"

<br/><br/>

## 🔨 Model
- 데이터베이스를 컨트롤할 수 있게 해주는 도구
- 사용하는 데이터들의 필수적인 필드(컬럼)들 + 동작들
- 저장된 데이터베이스의 구조
- 모델 클래스 1개 == 데이터베이스 테이블 1개

<br/>

> Model != Database <br/>
> 
> 데이터베이스는 장고에 포함X <br/>
> 독립적으로 존재하는 데이터베이스와 소통하기 위해 Model 사용

> 매핑 : 하나의 값을 다른 값으로 대응시키는 것

<br/>


### 모델 작성 (models.py)
- 모델 클래스를 작성하는 것은 데이터베이스 테이블의 스키마를 정의하는 것
- 모델 클래스 == 테이블 스키마
  > id는 테이블 생성시 자동으로 생성됨

  ``` python
  class Article(models.Model):
      title = models.CharField(max_length=10)
      content = models.TextField()
  ```
<br/>

#### 1. django.db.models 모듈의 Model 클래스를 상속받음
  - **클래스 상속 기반 형태의 Django 프레임워크 개발**

<br/>

#### 2. models 모듈을 통해 어떠한 타입의 DB 필드(컬럼)을 정의할 것인지 정의
  - 클래스 변수가 하나의 필드
  1. 클래스 변수(속성)명 : DB 필드의 이름
  2. 클래스 변수 값 : DB 필드의 데이터 타입 <br/>

  > 필드 이름 = 변수 타입 ==> 스키마

<br/>

### Django Model Field
- 테이블의 필드(컬럼)에 저장할 데이터 유형 정의 <br/>
🔗 [Django Model Field](https://www.djangoproject.com/)

<br/>

- CharField() : 길이가 제한이 있는 문자열 타입 (최대 255자)
  - 필수 인자 : max_length (필드 길이 제한, 유효성 검증)

<br/>

- TextField() : 긴 텍스트
  - 장고에 어떤 데이터베이스를 사용하느냐에 따라 최대 길이가 달라짐 (기본 : SQLite)
  - max_length : 사용자 입력 단계 반영O, 유효성 검증X

<br/>

- DateTimeField() : 날짜 및 시간
  - auto_now_add : 최초 생성 일자
  - auto_now : 최종 수정 일자
  > 헷갈리지 말고 잘 기억하자!


<br/><br/>

## ⭐ Migration ⭐
- 모델에 대한 청사진을 만들고 이를 통해 데이터 생성
- Django가 모델에 생긴 변화를 DB에 반영하는 방법

<br/>

### 1. makemigrations
> 청사진 (설계도)

`python manage.py makemigrations`
- 모델의 변경사항에 대한 새로운 migration을 만들 때 사용
- 0001_initial.py

<br/>

### 2. migrate
`python manage.py migrate`
- makemigrations로 만든 설계도를 실제 db.sqlute3 DB 파일에 반영
- 모델과 DB의 동기화

> db.splite3 마우스 우클릭 open database

> 테이블 이름 내부 규칙 : appname_classname

<br/>

➕ Migrations 기타 명령어
1. showmigrations : migrations 파일들이 migrate 됐는지 여부 확인
2. sqlmigrate : 해당 migrations 파일이 SQL 문으로 어떻게 해석될 지 미리 확인

<br/><br/>

## 추가 필드 정의
(모델 변경사항 반영하기) <br/>

1️⃣ 추가 모델 필드 작성 후 다시 한번 makemigrations 진행

2️⃣ Django 입장에서는 이미 존재하는 테이블에 새로운 컬럼이 추가되는 요구 사항을 받았는데, 이 컬럼들은 기본적으로 빈 값으로 추가될 수 없음
-> 기본 값으로 어떤 값을 설정할 것인지 물어봄
```
 1) Provide a one-off default now (will be set on all existing rows)
 2) Quit, and let me add a default in models.py
Select an option:
```
- 각 보기 번호의 의미
  1) 다음 화면으로 넘어가서 새 컬럼의 기본 값을 직접 입력하는 방법
  2) 현재 과정에서 나가고 모델 필드에 defalut 속성을 직접 작성하는 방법

  > '1' 입력 후 Enter
```
Please enter the default value now, as valid Python
You can accept the default 'timezone.now' by pressing 'Enter' or you can provide another value.
The datetime and django.utils.timezone modules are available, so you can do e.g. timezone.now
Type 'exit' to exit this prompt
[default: timezone.now] >>>
```

3️⃣ 아무것도 입력하지 않고 Enter 입력하면 Django에서 기본적으로 파이썬의 timezone 모듈의 now 메서드 반환 값을 기본 값으로 사용하도록 해줌

4️⃣ 새로운 설계도가 만들어짐
```
Migrations for 'articles':
  articles\migrations\0002_auto_20220831_1349.py
    - Add field created_at to article
    - Add field updated_at to article
```

> 기존 설계도를 수정한 것이기 때문에 의존성 O
``` python
dependencies = [
        ('articles', '0001_initial'),
    ]
```

5️⃣ 새로운 설계도와 DB 동기화 진행
`python manage.py migrate`

<br/><br/>

## ❗ 반드시 ❗ 기억해야 할 migration 3단계
1. models.py에서 변경사항이 발생하면
2. migrations 파일 생성 (설계도 생성) - makemigrations
3. DB 반영 (모델과 DB 동기화) - migrate


<br/>

### Model = "웹 애플리케이션의 데이터를 **구조화**하고 **조작**하기 위한 도구"

<br/><br/>

## 📣 ORM
> 중간 번역
- Object-Relational-Mapping
- 객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간에 데이터를 변환하는 프로그래밍 기술
- 장점
  - SQL을 잘 알지 못해도 객체지향 언어로 DB 조작이 가능
  - 객체 지향적 접근으로 인한 높은 생산성
- 단점
  - ORM 만으로 완전한 서비스를 구현하기 어려운 경우가 있음
- 사용하는 이유 : **생산성**

<br/><br/>

---

# QuerySet API
## 사전 준비
1. `$ pip install ipython django-extensions`

2. app 추가

3. 패키지 목록 업데이트


<br/>

### ✔️ Shell
- 운영체제 상에서 다양한 기능과 서비스를 구현하는 인터페이스 제공
- 사용자 <-> 셸 <-> 운영체제

- Python Shell

<br/>

4. Diango Shell
`$ python manage.py shell_plus`

5. 첫 ORM 명령어 사용하기
    ``` python
    In [1]: Article.objects.all()
    Out[1]: <QuerySet []>
    ```

<br/><br/>

### ✔️ Database API
- Article.objects.all()
(Model class).(Manager).(Queryset API)
- Queryset API => 데이터 조작, 명령

<br/>

### ✔️ objects manager
- 다양한 쿼리 셋 아이템들을 제공해줌

<br/><br/>

## 🤍 Query
- "쿼리문을 작성한다" = 원하는 데이터를 얻기 위해 데이터베이스에 요청을 보낼 코드 작성

<br/>

## 🤍 QuerySet
- 데이터베이스에게서 전달 받은 객체 목록 (데이터 모음)
- 리스트 형태 (필터, 정렬 등 O)

- But 데이터베이스가 단일한 객체를 반환할 때는 모델의 인스턴스로 반환됨 (QuerySet X)

<br/>

### ✔️ QuerySet API
- QuerySet과 상호작용하기 위해 사용하는 도구 (메서드, 연산자 등)

<br/><br/>

## 🤍 CRUD
Create / Read / Update / Delete <br/>
생성   / 조회 /  수정  / 삭제

<br/>

### ▶️ CREATE
데이터 객체를 생성하는 3가지 방법
<br/>

- 첫번째 방법
   1. article = Article() : 클래스를 통한 인스턴스 생성
   2. article.title : 클래스 변수명과 같은 이름의 인스턴스 변수 생성 후 값 할당
   3. article.save() : 저장

  > 한국 시간으로 변경하려고 해도 저장 시 UTC가 유지됨 <br/>
  > -> 읽을 때 한국 시간으로 보여줌

<br/>

- 두번째 방법
  - 인스턴스 생성 시 초기 값을 함께 작성하여 생성
  - `article = Article(title='second', content='django!')`
  - `article.save()`

<br/>

- 세번째 방법
  - QuerySet API 중 create() 메서드 활용
  - `Article.objects.create(title='third', content='django!')`
  - save 없이 바로 데이터 반환

<br/>

#### ⭐ .save()
- 객체를 데이터베이스에 저장
- save 호출 전까지는 객체의 id값은 None
- 반드시 save를 호출해야 테이블에 레코드가 생성됨

<br/><br/>

### ▶️ READ
1. return new querysets
2. do not return querysets

- all() : 전체 데이터 조회
  - `Article.objects.all()` 
  - `articles = Article.objects.all()` 담아서 사용 가능 -> 반복 가능한 개체 (for문 사용 가능)

- get() : 단일 데이터 조회
  - 객체를 찾을 수 없다면 에러
  - 둘 이상이면 에러
  - => 고유성(uniqueness)을 보장하는 조회에서 사용 (pk)
  - `Article.objects.get(id=1)`
  - `Article.objects.get(pk=1)`

- filter() : 무조건 QuerySet 반환
  - `Article.objects.filter(content='django!')`
  - pk 조회 X
    - QuerySet 반환
    - 해당 값이 없으면 빈 QuerySet 반환

> pk는 get으로만 조회 권장

- Field lookups
  - 조건 설정
  - filter(), exclude(), get()의 키워드 인자로 지정
  - `Article.objects.filter(content__contains='dj')`

<br/><br/>
> 수정 또는 삭제 전 조회 먼저~


### ▶️ UPDATE
`article.title = 'byebye'`
`article.save()`

<br/>

### ▶️ DELETE
`article.delete()`

> 1,2,3번 입력된 테이블에서 1번 데이터를 삭제하면, 다음 데이터 삽입 시 4번에 들어감 (1번은 비워둠)
> 삭제한 번호 재사용 X

<br/>

➕ 출력 형태가 불편하다면, 
__str__()

``` python
# class Article(models.Model): 내부에
      def __str__(self):
              return self.title
```
➡️ DB 변경사항 X, 출력에만 영향 --> migration 불필요

``` python
# 출력 결과
In [1]: Article.objects.all()
Out[1]: <QuerySet [<Article: second>, <Article: third>]>
```

<br/><br/>

---

# CRUD with view functions


- CREATE 로직을 구현하기 위해서는 2개의 view 함수가 필요!!
1. 글 작성 후 페이지 리턴
2. 데이터 받아서 DB에 저장하는 함수

