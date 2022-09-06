# Today I Learned
- [Django Form](#django-form)
- [Django ModelForm](#django-modelform)
- [Widgets]


<br/><br/>
---

# Django Form
- HTML form, input 태그를 통해 사용자로부터 데이터를 받으면 ➡ 들어오는 요청을 모두 수용 ➡ 필터링이 필요 (비정상적, 악의적 요청 O)
- 사용자가 입력한 데이터가 원하는 데이터 형식이 맞는지 유효성 검증이 필요
- Django Form : 쉽게 유효성 검증 O (유효성 검사를 단순화, 자동화)

<br/>

- Django는 Form에 관련된 작업의 세 부분 처리
1. 렌더링을 위한 데이터 준비 및 재구성
2. 데이터에 대한 HTML forms 생성
3. 클라이언트로부터 받은 데이터 수신 및 처리

<br/><br/>


## 📌 Form Class
: Django form 관리 시스템의 핵심
- Form Class 선언 = Model Class 선언과 비슷
- 상속을 통해 선언 (forms 라이브러리의 Form 클래스 상속)

<br/>

### 별도의 forms.py에서 작성 권장 (앱 폴더에 생성)
💛 articles/forms.py
``` python
from django import forms

class ArticleForm(forms.Form):
    # 사용자로부터 받을 데이터
    title = forms.CharField(max_length=10)
    content = forms.CharField()
```
> max_length가 forms에서는 필수입력값은 아님 (models에서는 필수)
> 
> txet 필드 존재 X

<br/>

💚 기존의 'new' view 함수, 템플릿
``` python
def new(request):
    return render(request, 'articles/new.html')
```
``` html
{% extends 'base.html' %}

{% block content %}
  <h1>NEW</h1>
  <form action="{% url 'articles:create' %}" method="POST">
    {% csrf_token %}
    <label for="title">Title: </label>
    <input type="text" name="title" id="title"><br>
    <label for="content">Content: </label>
    <input type="text" name="content" id="content"><br>
    <input type="submit">
  </form>
  <hr>
  <a href="{% url 'articles:index' %}">뒤로가기</a>
{% endblock content %}
```
<br/>

💚 새로운 'new' view 함수, 템플릿
``` python
from .forms import ArticleForm

def new(request):
    form = ArticleForm()
    context = {
        'form' : form, 
    }
    return render(request, 'articles/new.html', context)
```
``` html
{% extends 'base.html' %}

{% block content %}
  <h1>NEW</h1>
  <form action="{% url 'articles:create' %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
  </form>
  <hr>
  <a href="{% url 'articles:index' %}">뒤로가기</a>
{% endblock content %}
```
<br/><br/>

### ▶ Form rendering options
- `<lable> & <input>` 쌍에 대한 3가지 출력 옵션
1. **as_p()** ✔ : 각 필드가 `<p>`태그로 감싸져서 렌더링 (줄바꿈 일어남)
2. as_ul()
3. as_table()

<br/>

### ▶ Django의 HTML input 요소 표현
1. Form fields
- forms.CharField()
- 유효성 검사 로직 처리
- 한계 : input text 형태로만 출력

2. Widgets
- HTML input 요소 렌더링 담당
- 단순한 출력만 담당
`content = forms.CharField(widget=forms.Textarea)`


<br/><br/>


### 📌 Widgets 
- input element 표현 담당
- **단순히** HTML 렌더링 처리 (유효성 검증 X)

✅ 응용

``` python
class ArticleForm(forms.Form):
    # 장고의 스타일 가이드 권장사항
    NATION_A = 'kr'
    NATION_B = 'ch'
    NATION_C = 'jp'
    NATIONS_CHOICES = {
        (NATION_A, '한국'),
        (NATION_B, '중국'),
        (NATION_C, '일본'),
    }

    title = forms.CharField(max_length=10) 
    content = forms.CharField(widget=forms.Textarea)
    nation = forms.ChoiceField(choices=NATIONS_CHOICES)
```
> 여러 항목 선택 원하면 (radio)
> 
> 장고 공식 문서 (RadioSelect)
> 
> `nation = forms.ChoiceField(choices=NATIONS_CHOICES, widget=forms.RadioSelect)`

<br/><br/>

---

# Django ModelForm
- form을 더 쉽게 작성
- model을 기반으로 한 form

<br/>

## ModelForm Class
- Model을 통해 Form Class를 만들 수 있는 helper class

🚩 선언
- ModelForm 클래스를 상속받음
- 정의한 ModelForm 클래스 안에 Meta 클래스 선언 - 어떤 모델 기반인지 작성

<br/>

``` python
from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        # 어떤 모델을 기반으로 할지 (호출 X)
        model = Article
        # 모델필드 중 어떤 것을 출력할지
        fields = '__all__'
```
<br/>

### 📌 Meta Class
- ModelForm의 정보 작성
- 참조할 모델 + form에 적용할 field 정보

- `__all__` : 모델의 모든 필드 포함 가능
- `exclude = ('필드명')` : 특정 필드 제외 가능

> Meta data
> : 데이터를 표현하기 위한 데이터

<br/>

### 📌 참조 값 vs. 반환 값
``` python
def greeting():
  return '안녕하세요'

# 1. 참조 값
print(greeting)     # <function greeting at 0x10761caf0>
# 2. 반환 값
print(greeting())   # 안녕하세요
```
> 참조 값 언제 사용❔
> 
> 함수를 호출하지 않고 함수 자체를 그대로 전달하여, 다른 함수에서 "필요한 시점에" 호출하는 경우

<br/>

**❌ 주의사항** <br/>
단순히 모델 정보를 Meta라는 이름의 내부 클래스로 작성하도록 되어 있음 (문법적으로 접근 X)

<br/><br/>

---

## ModelForm with view functions
### 🔹 CREATE
``` python
def create(request):
    form = ArticleForm(request.POST)
    if form.is_valid():
        article = form.save()
        return redirect('articles:detail', article.pk)
    return redirect('articles:new')
```
<br/>

- is_valid() : 유효성 검사 (boolean으로 반환)
  - False인 경우 (통과 X) ➡ errors 속성에 값을 채워서 내려보냄
    ``` python
    def create(request):
    form = ArticleForm(request.POST)
    if form.is_valid():
        article = form.save()
        return redirect('articles:detail', article.pk)
    print(f'에러: {form.errors}')
    context = {
        'form': form,
    }
    return render(request, 'articles/new.html', context)
    ```

<br/>

- save() : form 인스턴스에 바인딩 된 데이터를 통해 데이터베이스 객체를 만들고 저장
  - instance 여부를 통해 생성할지 수정할지 결정
    ``` python
    # CREATE
    form = ArticleForm(request.POST)
    form.save()

    # UPDATE
    form = ArticleForm(request.POST, instance=article)
    form.save()
    ```

> 아무것도 입력하지 않았을 때 뜨는 팝업 -> required 

<br/><br/>

### 🔹 UPDATE
``` python
def edit(request, pk):
    article = Article.objects.get(pk=pk)
    form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form' : form,
    }
    return render(request, 'articles/edit.html', context)
```
``` python
def update(request, pk):
    article = Article.objects.get(pk=pk)
    form = ArticleForm(request.POST, instance=article)
    if form.is_valid():
        form.save()
        return redirect('articles:detail', article.pk)
    context = {
        'form': form,
    }
    return render(request, 'articles/edit.html', context)
```

> form = ArticleForm(request.POST, instance=article) <br/>
> 원래는 form = ArticleForm(data=request.POST, instance=article) <br/>
> data는 생략할 수 있고, instance는 생략할 수 없는 이유 <br/>
> data는 첫번째 인자, 즉 생략해도 data로 인식 <br/>
> instance는 두번째 인자가 아님, 즉 생략하면 file로 인식

<br/>

💙 ModelForm이 Form 보다 더 좋은 것이 아니라 각자 역할이 다른 것‼ <br/>
💙 공통점 - 사용자 요청 처리


### **Form**
- DB에 영향 미치지 않고 단순 데이터만 사용하는 경우
- ex) 로그인

vs. 
### **ModelForm**
- DB와 연관
- ex) 회원가입

<br/>

## Widgets
- 저장 시 영향 X, 사용자 입력 제한

``` python
class ArticleForm(forms.ModelForm):

    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'my-title',
                'placeholder': 'Enter the title',
                'max_length' : 10,
            }
        )
    )

    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'my-content',
                'placeholder' : 'Enter the content',
                'rows' : 5,
                'cols' : 50,
            }
        ),
        error_messages={
            'required': 'Please enter your content',
        }
    )

    class Meta:
        model = Article
        fields = '__all__'
```

<br/><br/>

---

# Handling HTTP requests
- HTTP requests 처리에 따른 view 함수 구조 변화 <br>

- new-create, edit-update
- 공통점
  - new-create : CREATE 로직 구현
  - edit-update : UPDATE 로직 구현
- 차이점
  - new, edit : GET 요청에 대한 처리만 (페이지 렌더링)
  - create, update : POST 요청에 대한 처리만 (실제 DB 조작)
- 이 공통점과 차이점을 기반으로, 하나의 view 함수에서 method에 따라 로직이 분리되도록 변경

``` python
def create(request):
    if request.method == 'POST':
        # create
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        # new
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)
```



<br/><br/>

---

# View Decorators
