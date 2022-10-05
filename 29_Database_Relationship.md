# TIL

<br><br>

---
# A many-to-one relationship
▫ RDB의 모든 테이블에는 기본 키 속성 有   
➡ **외래 키**를 사용하여 각 행에서 서로 다른 테이블 간 **관계**를 만드는 데 사용 가능  

▫ 관계 : 테이블 간의 상호작용을 기반으로 설정되는 여러 테이블 간의 논리적인 연결  

![image](https://user-images.githubusercontent.com/93974908/193952702-826c7cd5-7a4c-4cb9-99f9-71c739932b6b.png)
> 공유된 고객 id를 기반으로 연결되며 다양한 명령 처리 가능

<br>

### ▶ RDB에서의 관계
▫ 1 : 1  
한 테이블의 레코드 하나가 다른 테이블의 레코드 단 한 개와 관련된 경우  

▫ **N : 1**  
한 테이블의 0개 이상의 레코드가 다른 테이블의 레코드 한 개와 관련된 경우  

▫ N : N  
한 테이블의 0개 이상의 레코드가 다른 테이블의 0개 이상의 레코드와 관련된 경우  

<br>

## 🔑 Foreign Key
▫ 외래 키 (외부 키)  
▫ 관계형 데이터베이스에서 한 테이블의 필드 중 다른 테이블의 행을 식별할 수 있는 키  

- 참고하는 테이블 = 외래 키  
- 참조되는 테이블 = 기본 키

▫ 참조하는 테이블의 행 1개의 값은, 참조되는 테이블의 행 값에 대응됨 ➡ 참조되는 테이블에 나타나지 않는 값 포함 ❌  

▫ 참조하는 테이블 행 여러 개가, 참조되는 테이블의 동일한 행 참조 ⭕ ➡ **"N : 1"**

▫ 키를 사용하여 부모 테이블의 유일한 값을 참조 (참조 무결성)  
▫ 외래 키의 값이 반드시 부모 테이블의 기본 키 일 필요 X, BUT 유일한 값이어야 함  

> 🔎 참조 무결성  
> 
> ▫ 데이터베이스 관계 모델에서 관련된 2개의 테이블 간 일관성   
> ▫ 외래 키가 선언된 테이블의 외래 키 속성의 값은 그 테이블의 부모가 되는 테이블의 기본 키 값으로 존재해야 함 


<br><br>

---
# N : 1 (Comment - Article)
▫ Comment(N) - Article(1)  
▫ "0개 이상의 댓글은 1개의 게시글에 작성될 수 있음"  

![image](https://user-images.githubusercontent.com/93974908/193953776-aae7c782-d79d-4cdf-80e3-343258c089d4.png)

> 댓글은 게시글과 관련 있으니, Article 앱에서 작성  

> 모델 작성 = 스키마 작성  
> 타입 = 모델 필드  
> 제약조건 = 옵션

<br>

## ▶ Django Relationship fields
1️⃣ OneToOneField()  - 1 : 1     
2️⃣ **ForeignKey()** - N : 1  
3️⃣ ManyToManyField() - N : N  

<br>

## 🔑 ForeignKey(to, on_delete, **options)
▫ N : 1 담당  

▫ 필수 위치 인자 
1. 참조하는 model class
2. on_delete 옵션
   - 외래 키가 참조하는 객체가 사라졌을 때, 어떻게 처리할 지
   - 데이터 무결성 위해 매우 중요!~! 
   - **CASCADE** : 부모 객체가 삭제되었을 때 이를 참조하는 객체도 모두 삭제 
      > 게시물 삭제 시 댓글도 삭제
   - PROTECT, SET_NULL, SET_DEFAULT 등 

<br><br>

## 💻 Comment Model
<br>

### 1️⃣ Comment 모델 정의
``` python
# articles/models.py

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
```
▫ 외래 키 필드는 ForeignKey 클래스를 작성하는 위치와 관계없이 필드 마지막에 작성됨  
▫ ForeignKey() 클래스의 인스턴스 이름은 참조하는 모델 클래스 이름의 소문자로 작성하는 것 권장  
(Article ➡ article)

> 🔎 데이터 무결성 
>  
> ▫ 데이터의 정확성, 일관성을 유지하고 보증하는 것  
> ▫ 데이터베이스나 RDBMS의 중요한 기능  
> 
> ▫ 무결성 제한의 유형
> 1. 개체 무결성
> 2. 참조 무결성
> 3. 범위 무결성

<br>

✔ 장고(파이썬) ↔ ORM ↔ DB(SQL)

<br><br>

### 2️⃣ 모델 작성 후 마이그레이션

![image](https://user-images.githubusercontent.com/93974908/193956105-6260b0d7-d39f-43c1-bc57-7ea03f512898.png)

> ▫ ForeignKey 모델 필드로 인해 작성된 컬럼의 이름 = **article_id**  
> ▫ 소문자로 쓰라고 한 이유 : 어떤 모델을 참조하는 FK인지 직관적으로 알 수 있음

▫ **sqlmigrate** : 생성된 마이그레이션 파일이 어떤 SQL 문장을 실행하는지 보여줌  
```shell
$ python manage.py sqlmigrate articles 0002
```

``` shell
BEGIN;
--
-- Create model Comment
--
CREATE TABLE "articles_comment" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "content" text NOT NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL, "article_id" bigint NOT NULL REFERENCES "articles_article" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "articles_comment_article_id_59ff1409" ON "articles_comment" ("article_id");
COMMIT;
```
<br><br>

### 3️⃣  댓글 생성 연습  
``` shell
$ python manage.py shell_plus
```

#### ❶ 댓글 생성
![image](https://user-images.githubusercontent.com/93974908/193958307-7d5be0ce-da21-4562-93b5-4105ab140a3e.png)
```
# 1. Comment 클래스의 인스턴스 comment 생성
# 2. 인스턴스 변수 저장
# 3. DB에 댓글 저장
```

❌ 에러 발생
![image](https://user-images.githubusercontent.com/93974908/193958330-d70353b4-df72-4f62-92ec-800c767b083b.png)
> ▫ 어떤 게시글에 달리는 댓글인지 모름 (article_id 값이 누락됨)   
> ▫ BUT 댓글은 단독으로 존재할 수 없음    
> 
> ▫ 어떤 Article을 참고하고 있는지 FK 값을 넣어줘야 함

<br>

#### ❷ 댓글 속성 값 확인 

![image](https://user-images.githubusercontent.com/93974908/193958690-4af1b76c-f118-47bf-bd03-d64a41330ab5.png)
```
# 4. 게시글 생성

# 7. 외래 키 데이터 입력
> comment.article_id = article.pk ➡ 가능은 하지만 권장 X

# 8. DB에 댓글 저장
```

![image](https://user-images.githubusercontent.com/93974908/193958735-d70efe34-4f9b-4b5b-9580-99ac3807dac9.png)


<br>

#### ❸ comment 인스턴스를 통한 article 값 접근

![image](https://user-images.githubusercontent.com/93974908/193958868-c4739a77-15f5-45d0-9a54-749a9d2cf277.png)
```
결과는 같지만 어디서 조회하는지는 다름 

# 10. comment가 가지고 있는 컬럼의 값을 가져옴  
# 11. article 테이블에 있는 pk를 가져옴

> article_id 에는 객체를 집어넣을 수 없음  
> comment.article_id = article ❌
```


![image](https://user-images.githubusercontent.com/93974908/193959275-e8e16639-a8df-4efb-98b4-788aa503966e.png)

```
# 12. 댓글 속성 값 확인
# 13. 클래스 변수명인 article로 조회 시 해당 참조하는 게시물 객체 조회 가능 
# 14. 1번 댓글이 작성된 게시물의 content 조회
```
<br>

#### ❹ 두번째 댓글 작성

![image](https://user-images.githubusercontent.com/93974908/193959430-8a719935-a40e-4b7b-ba0d-87334091495e.png)


![image](https://user-images.githubusercontent.com/93974908/193959475-6151af2d-4520-423a-82ef-e08bbb54b151.png)


<br><br>

## ▶ 관계 모델 참조

> 1쪽에서는 N을 참조할 수 있는 정보가 X  
> 해결방안 ?

<br>

### 🔹 Related manager - 장고 제공  
▫ N:1, M:N 관계에서 사용 가능한 문맥  
▫ 역참조 시 사용가능한 manager 생성  

<br>

### 🔹 역참조  
▫ 나를 참조하는 테이블을 참조하는 것  
▫ 즉, 본인을 외래 키로 참조 중인 다른 테이블에 접근하는 것  
> comment ----참조----> article  
> comment <---역참조--- article

<br>

### 🔹 **article.comment_set.method()**
▫ 실제 Article 클래스에는 Comment와 어떠한 관계도 작성되어 있지 않음  
▫ 대신 장고가 comment_set 자동 생성해 article.comment_set 형태로 댓글 객체 참조 가능  


![image](https://user-images.githubusercontent.com/93974908/193960555-78c96da4-e748-4fe3-a182-9384b7f7ce76.png)
```
# 18. 1번 게시글 조회

# 20. dir() : 해당 인스턴스가 사용할 수 있는 모든 메서드 출력 
```

![image](https://user-images.githubusercontent.com/93974908/193960957-f3d1f0d0-1428-4c87-8cfc-764c5de9cb21.png)
```
# 21. 1번 게시글에 작성된 모든 댓글 조회 (역참조)

# 22 ~ 23. 1번 게시글에 작성된 모든 댓글 출력
```

✔ **related_name**  
▫ ForeignKey 클래스의 선택 옵션  
▫ 별칭이 아니라 대체 ➡ 변경 시, comment_set은 더 이상 사용 X   
▫ 작성 후 마이그레이션 필요  

▫ 선택 옵션이지만 반드시 사용해야하는 상황 有 ➡ 다대다 관계  

<br>

### 4️⃣ admin site 등록

``` python
# articles/admin.py

from django.contrib import admin
from .models import Article, Comment


admin.site.register(Article)
admin.site.register(Comment)

# admin 사이트에 등록한다.
```

<br><br>

## 💻 Comment 구현

<br>

### 1️⃣ CREATE
<br>

#### ❶ 사용자로부터 댓글 데이터를 입력 받기 위한 CommentForm 작성
``` python
# articles/forms.py

from django import forms
from .models import Article, Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
```
<br>

#### ❷ detail 페이지에서 CommentForm 출력
``` python
#articles/views.py

from .forms import ArticleForm, CommentForm


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    context = {
        'article': article,
        'comment_form': comment_form,
    }
    return render(request, 'articles/detail.html', context)
```
![image](https://user-images.githubusercontent.com/93974908/193981031-a383d06b-6c8d-40e3-8ff1-3d6f58cf0d23.png)

> 댓글을 쓸 사람이 어떤 위치에 쓸지 선택 가능  
> BUT 해당 게시글에만 쓸 수 있게 하고 싶음  
> 
> ➡ 외래 키 필드는 사용자의 입력으로 받는 것이 아니라 view 함수 내에서 받아 별도로 처리되어 저장되어야 함

<br>

#### ❸ 외래 키 필드를 출력에서 제외
``` python
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('article',)
```

<br>

#### ❹ 외래 키 받아오는 함수
``` python
path('<int:pk>/comments/', views.comments_create, name='comments_create'),
```
▫ variabl routing 사용  

``` python
def comments_create(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment_form.save()
    return redirect('articles:detail', article.pk)
```

> 🔎 댓글 생성 과정  
> comment = Comment()  
> comment.content = 'aaa'  
> comment.article = articles  
> comment.save()  
> 위의 view 함수는 article 객체 저장이 이루어질 타이밍이 없음  

<br>

#### ❺ save 메서드의 commit 옵션을 사용해 DB에 저장되기 전 article 객체 저장
``` python
def comments_create(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.save()
    return redirect('articles:detail', article.pk)
```
✔ **save(commit=False)**  
▫ 아직 데이터베이스에 저장되지 않은 인스턴스를 반환  
▫ 저장하기 전에 객체에 대한 사용자 지정 처리를 수행할 때 유용하게 사용  

<br><br>

### 2️⃣ READ (작성한 댓글 목록 출력하기)
▫ 특정 article에 있는 모든 댓글을 가져온 후 context에 추가
``` python
# articles/views.py

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)
```
▫ detail 템플릿에서 댓글 목록 출력
``` html
<!-- articles/detail.html -->

  <hr>
  <h4>댓글 목록</h4>
  <ul>
    {% for comment in comments %}
      <li>{{ comment.content }}</li>
    {% endfor %}
  </ul>
  <hr>
  <form action="{% url 'articles:comments_create' article.pk %}" method="POST">
    {% csrf_token %}
    {{ comment_form }}
    <input type="submit">
  </form>
```


<br><br>

### 3️⃣ DELETE (댓글 삭제)

▫ 첫 번째 방법
``` python
path('<int:comment_pk>/comments/delete/', views.comments_delete, name='comments_delete',),
```
``` python
def comments_delete(request, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    article_pk = comment.article.pk
    comment.delete()
    return redirect('articles:detail', article_pk)
```
▫ 두 번째 방법 ✔
``` python
path('<int:article_pk>/comments/<int:comment_pk>/delete', views.comments_delete, name='comments_delete',),
```
``` python
def comments_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('articles:detail', article_pk)
```

▫ 각각의 댓글에 삭제버튼이 들어가야 함
``` html
<!-- articles/detail.html-->

  <h4>댓글 목록</h4>
  <ul>
    {% for comment in comments %}
      <li>
        {{ comment.content }}
        <form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method="POST">
          {% csrf_token %}
          <input type="submit" value="delete">
        </form>
      </li>
    {% endfor %}
  </ul>
```

<br><br>

### ▶ Comment 추가 사항

1. 댓글 개수 출력
   - DTL filter - length 사용
   - Queryset API - count() 사용

2. 댓글이 없는 경우 대체 컨텐츠 출력
   - for empty 사용

``` html
<!-- articles/detail.html-->

  <h4>댓글 목록</h4>
  {% if comments %}
    <p>{{ comments|length }}개의 댓글이 있습니다.</p>
  {% endif %}
  <ul>
    {% for comment in comments %}
      <li>
        {{ comment.content }}
        <form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method="POST">
          {% csrf_token %}
          <input type="submit" value="delete">
        </form>
      </li>
    {% empty %}
      <p>댓글이 없어요..</p>
    {% endfor %}
```

<br><br>

---
# N : 1 (Article - User)
▫ Article(N) - User(1)  
▫ "0개 이상의 게시글은 1명의 회원에 의해 작성될 수 있음"  
<br>

### ▶ Django 에서 User 모델을 참조하는 방법  
1. settings.AUTH_USER_MODEL
   - 문자열을 반환함
   - models.py의 모델 필드에서 User 모델을 참조할 때 사용
2. get_user_model()
   - 객체를 반환함
   -  models.py가 아닌 다른 모든 곳에서 User 모델을 참조할 때 사용

<br>

## 💻 모델 관계 설정

![image](https://user-images.githubusercontent.com/93974908/193986111-8e452056-4f42-476f-9490-919e931f3547.png)

<br>

### ▶ Article 모델에 User 모델을 참조하는 외래 키 작성
``` python
# articles/models.py

from django.db import models
from django.conf import settings


class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```
> models.py ➡ settings.AUTH_USER_MODEL  
> 다른 모든 곳 ➡ get_user_model()

<br>

### ▶ 마이그레이션 진행   
▫ 기존 데이터와 테이블이 존재해서 컬럼추가가 불가
➡ 값을 넣어줘야 추가됨  

![image](https://user-images.githubusercontent.com/93974908/193986830-6a5c0dc5-00b9-483a-91c0-5da4d76fdbf9.png)
> 우선 1번 유저가 모든 게시물을 작성한 것으로 됨


<br><br>

## 1️⃣ CREATE 
▫ 인증된 회원의 게시글 작성 구현  
▫ 작성 전 로그인을 먼저 진행한 상태로 진행  

### ArticleForm
``` python
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ('user',)
```
> 외래 키 데이터 누락 -> 작성자 정보 함께 저장 필요 -> save의 commit 옵션 활용
``` python
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)
```

<br><br>

## 2️⃣ DELETE
▫ 게시글 작성자만 삭제 가능하도록 함
``` python
def delete(request, pk):
    if request.user.is_authenticated:
        article = Article.objects.get(pk=pk)
        if request.user == article.user:
            article.delete()
            return redirect('articles:index')
    return redirect('articles:detail', article.pk)
```


<br><br>

## 3️⃣ UPDATE
▫ 게시글 작성자만 수정 가능하도록 함

``` python
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            # form = ArticleForm(data=request.POST, instance=article)
            if form.is_valid():
                form.save()
                return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm(instance=article)
    else:
        return redirect('articles:index')
    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'articles/update.html', context)
```
<br>

➕ 게시글의 작성자가 아니라면, 수정 / 삭제 버튼 출력 X  

``` html
<!-- articles/detail.html-->

  {% if request.user == article.user %}
    <a href="{% url 'articles:update' article.pk %}">UPDATE</a>
    <form action="{% url 'articles:delete' article.pk %}" method="POST">
      {% csrf_token %}
      <input type="submit" value="DELETE">
    </form>
  {% endif %}
```

## 4️⃣ READ
▫ 게시글 작성자 출력
``` html
<p><b>작성자 : {{ article.user }}</b></p>
```
<br><br>

---
# N : 1 (Comment - User)
▫ Comment(N) - User(1)  
▫ "0개 이상의 댓글은 1명의 회원에 의해 작성될 수 있음"  

<br>

## 💻 모델 관계 설정

![image](https://user-images.githubusercontent.com/93974908/193994070-cd63491e-10ad-42ba-91bf-8381e2f567cf.png)
> Comment는 외래 키 2개를 갖는 테이블이 됨

<br>

### ▶ Comment 모델에 User 모델을 참조하는 외래 키 작성 

``` python
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
```

<br>

### ▶ 마이그레이션 진행
> Article - User 관계와 동일하게 진행 

![image](https://user-images.githubusercontent.com/93974908/193994872-811eac8b-6724-4ec4-9d41-59b11cc01936.png)

<br><br>

## 1️⃣ CREATE 
▫ 인증된 회원의 댓글 작성  
▫ 작성 전 로그인을 먼저 진행한 상태로 진행  

### CommentForm
``` python
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('article', 'user',)
```
> 불필요한 user 정보가 출력되고 있었음  

### 외래 키 데이터 누락 

``` python
def comments_create(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.user = request.user
        comment.save()
    return redirect('articles:detail', article.pk)
```
> `comment.user = request.user`
> 
> save 전에만 진행하면 됨  
> user 필드는 사용자로부터 받는 것이 아니라 request 객체에서 가져와서 처리  


<br>

## 2️⃣ READ
▫ 댓글 작성자 출력
> detail.html 페이지 수정

<br>

## 3️⃣ DELETE
▫ 댓글 작성자 본인만 삭제 가능하게 함  
``` python
def comments_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('articles:detail', article_pk)
```
▫ 해당 댓글의 작성자가 아니라면, 삭제 버튼 출력 X


<br><br>

## 인증된 사용자에 대한 접근 제한하기  
▫ is_authenticated  
▫ View decorator  

``` python
@require_POST
def comments_create(request, pk):
    if request.user.is_authenticated:
        article = Article.objects.get(pk=pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.user = request.user
            comment.save()
        return redirect('articles:detail', article.pk)
    return redirect('accounts:login')


@require_POST
def comments_delete(request, article_pk, comment_pk):
    if request.user.is_authenticated:
        comment = Comment.objects.get(pk=comment_pk)
        # article_pk = comment.article.pk
        if request.user == comment.user:
            comment.delete()
    return redirect('articles:detail', article_pk)
```

``` html
  {% if request.user.is_authenticated %}
    <form action="{% url 'articles:comments_create' article.pk %}" method="POST">
      {% csrf_token %}
      {{ comment_form }}
      <input type="submit">
    </form>
  {% else %}
    <a href="{% url 'accounts:login' %}">댓글을 작성하려면 로그인 하세요.</a>
  {% endif %}
```


<br><br>

➕ **isort**

▫ 장고에서 원하는 import style guide에 맞춰 정리해줌  
▫ 설치 : `$ python -m pip install "isort >= 5.1.0"`   
▫ 실행 : `$ isort accounts/views.py`  



