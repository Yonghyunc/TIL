# Today I Learned
1. [HTML](#html)
2. [CSS](#css)


<br/>

---
# Web이란?
## 1. 웹 사이트의 구성 요소
▶️ 웹 사이트
- 브라우저를 통해 접속하는 웹 페이지 (**문서**) 들의 모음
- 정보 + 링크
- 링크를 통해 여러 웹 페이지를 연결한 것

HTML ➡️ 구조

CSS ➡️ 표현

Javascript ➡️ 동작, 처리, 계산

▶️ 브라우저
- 웹 사이트는 브라우저를 통해 동작
- 크롬, 엣지, 파이어폭스, 네이버 웨일 등
- Deprecated(더 이상 지원하지 않는) - 익스플로러
- 브라우저가 다양해서 동작마다 차이 발생 (파편화) -> 규칙 필요


## 2. 웹 표준과 크로스 브라우징
▶️ 웹 표준
- 웹에서 표준적으로 사용되는 기술이나 규칙
- 어떤 브라우저든 웹 페이지가 동일하게 보이도록 함 (**크로스 브라우징**)

- W3C (CSS의 표준) : 팀 버너스리
- WHATWG (HTML과 웹 API의 표준) 

<br/><br/>

---

# HTML
Hyper Text Markup Language


### Hyper Text (팀 버너스리)
참조(하이퍼링크)를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트 <br/>
링크들 간의 연결


### Markup Language
태그 등을 이용하여 문서나 데이터 구조를 명시하는 언어 <br/>
태그 – 글에 역할을 부여 <br/>
`<title>Hello, HTML</title>`

==> 웹 페이지를 작성(구조화)하기 위한 언어

<br/>

HTML 스타일 가이드 -- 2 space

<br/><br/>

## HTML 기본 구조

- html : 문서의 최상위 요소
- head : 문서 메타데이터 요소 (데이터들의 설명)
- body : 실제 데이터 내용 (문서에 보이는 부분)

ex) body(사진) -> head(찍은 장소, 시간, 해상도 등)

<br/>

**DOM (Document Object Model) 트리**
- 브라우저가 만드는 것
- 텍스트 파일인 HTML 문서를 브라우저에서 렌더링 하기 위한 구조


<br/>

### head 예시
- title : 브라우저 상단 타이틀                        
- meta : 문서 레벨 메타데이터 요소                   
- link : 외부 리소스 연결 요소 (CSS파일, favicon 등) 
- script : 스트립트 요소                               
- style : CSS 직접 작성                               

 #### 🔗 [head.html](https://github.com/Yonghyunc/TIL/blob/master/HTML/head.html)

<br/>

Open Graph Protocol

<br/><br/>

### 📢 요소 = 태그(tag) + 내용(content)
- 시작 태그 / 종료 태그 / 태그 사이에 위치한 내용
- `<h1>contents</h1>`
- 태그로 내용을 감싸는 것 (정보의 성격, 의미 정의)
- 내용 없는 태그 존재 (-> 닫는 태그 X)
  - br, hr, img, input, link, meta


- 요소 중첩 가능 --> 그래서  HTML은 트리구조(계층구조)
  - 중첩 통해 하나의 문서 구조화
  - 여는 태그, 닫는 태그 잘 확인 --> 오류 안 남 (깨진 상태로 출력) --> 디버깅 어려움



### 📢 속성 = 이름 + 값
- 태그별로 사용할 수 있는 속성 다름 <br/>
ex) <a> (anchor tag) : 하이퍼링크 연결 태그 --> 구현하기 위해서 속성 필요

- =사용 시 공백 NO
- 쌍따옴표 사용 <br/>
`<a href="https://google.com"></a>`


- 태그의 부가적인 정보 설정
- 요소는 속성을 가질 수 있으며, 추가적인 정보 제공 (경로, 크기 등)
- 보통 **이름**과 **값**이 하나의 쌍으로 존재

<br/>

- 태그와 상관없이 사용 가능한 속성 존재 (HTML Global Attribute)
  - **id** : 문서 전체에서 유일한 고유 식별자 지정
  - **class** : 공백으로 구분된 해당 요소의 클래스의 목록
  - data-* : 페이지에 개인 사용자 정의 데이터를 저장하기 위해 사용
  - **style** : inline 스타일
  - title : 요소에 대한 추가 정보 지정
  - tabindex : 요소의 탭 순서

    <img width="350" src=https://i.esdrop.com/d/f/GQtKpTuAPv/36nqh6jmKO.png alt="HTML Global Attribute">

 #### 🔗 [html_basic.html](https://github.com/Yonghyunc/TIL/blob/master/HTML/html_basic.html)

<br/><br/>

### 시맨틱 태그 - 의미적 가치
- header : 머리말
- nav : 내비게이션
- aside : 사이드, 메인과 관련성이 적은 콘텐츠
- section : 문서의 일반적인 구분, 컨텐츠의 그룹
- article : 문서, 페이지, 사이트 안에서 독립적으로 구분되는 영역
- footer : 마지막 부분

> Non semantic : div, span 등

  <img width="300" src=https://i.esdrop.com/d/f/GQtKpTuAPv/B0REVNZ1lZ.png alt="시맨틱 태그">

❔시맨틱 태그를 사용해야 하는 이유 <br/>
: (의미론적 마크업) 검색엔진 등에 의미 있는 정보의 그룹을 태그로 표현 / 검색엔진 최적화(SEO) <br/>
: 원래 div로 묶던 것들을 의미를 넣어 구분 -> 스크린 리더가 읽는 것이 가능해짐

<br/><br/>

**렌더링** : 웹사이트 코드를 사용자가 보게 되는 웹 사이트로 바꾸는 과정


<br/><br/>

---

## HTML 문서 구조화
### 요소 <br/>
➡️ 인라인 요소 : 글자처럼 취급 <br/> -- 글자만큼만 공간 사용
➡️ 블록 요소 : 한 줄 모두 사용 -- 가로로 100% 모든 공간 사용

 <br/>

### 텍스트 요소
(= 인라인 요소)
  <img width="500" src=https://i.esdrop.com/d/f/GQtKpTuAPv/pcEU5uOfQb.png alt="텍스트 요소">

 <br/>

### 그룹 컨텐츠
(= 블록 요소)
  <img width="500" src=https://i.esdrop.com/d/f/GQtKpTuAPv/ShvmNHTdYG.png alt="그룹 컨텐츠">

- `<div>` =  division / 달라지는 건 없지만 구역을 나누기 위해 (구분)

  <img width="400" src=https://i.esdrop.com/d/f/GQtKpTuAPv/0f1r7a3Avy.png alt="그룹 컨텐츠2">

<br/>

### form
- 정보(데이터)를 서버에 제출하기 위해 사용하는 태그 <br/>
ex) 로그인(ID, PW) -> 서버 전송 // 게시글 작성 -> 서버 전송

- 기본 속성
  - action : form을 처리할 서버의 URL (데이터를 보낼 곳)
  - method : form을 제출할 때 사용할 HTTP 메서드 (GET / POST) -- 어떤 요청?
  - enctype : method가 post인 경우 데이터 유형
    - application/x-www-form-urlencoded : 기본값
    - multipart/form-data : 파일 전송 시
    ``` html
    <form action="/search" method="GET">
    </form>
    ```

<br/>

### input
- 실제로 데이터 입력
- 대표적인 속성
  - name : 이름
  - value : 값
    - 이름/값 페어로 전송됨
  - required, readonly, autofocus ......
  ``` html
  <form action="/search" method="GET">
    <input type="text" name="q">
  </form>
  ```

<br/>

### input lable
- label을 클릭하여 input 자체의 초점을 맞추거나 활성화 시킬 수 있음
- `<input>`에 id 속성 // `<label>`에 for 속성 활용
  ``` html
  <label for="agreement">개인정보 수집에 동의합니다.</label>
  <input type="checkbox" name="agreement" id="agreement">
  ```

 #### 🔗 [form.html](https://github.com/Yonghyunc/TIL/blob/master/HTML/form.html)

<br/>

### input 유형
1. 일반 - 입력 받기 위해 제공
    - text
   - password : *
   - email
   - number : min, max, step 속성 활용 가능
   - file : accept 속성 활용하여 파일 타입 지정 가능


<br/>

2. 항목 중 선택 (+ label 태그) 
   - 동일 항목은 name을 지정하고 선택된 항목에 대한 value를 지정해야 함
   - checkbox : 다중 선택
   - radio : 단일 선택  

<br/>

3. 기타
   1. 다양한 종류의 input을 위한 picker 제공
      -  color
      -  date
   2. hidden : 사용자에게 보이지 않는 input

<br/>

4. 종합
- `<input>` 요소의 동작은 type에 따라 달라지므로, 각각의 내용을 숙지해야 함!!

<br/><br/>

---

# CSS
Cascading Style Sheets
(계단식)
- 스타일을 지정하기 위한 언어
- 선택하고, 스타일 지정

``` css
h1 {
  color: blue;
  font-size: 15px;  
}
```
<img width="300" src=https://i.esdrop.com/d/f/GQtKpTuAPv/fyseNlIjg0.png alt="css">

- 선택자를 통해 스타일을 지정할 HTML 요소 선택
- 속성과 값, 하나의 쌍
  - 속성(property) : **어떤** 스타일 기능을 변경할지 결정
  - 값(value) : **어떻게**스타일 기능을 변경할지 결정

<br/>

## CSS 정의 방법
1. 인라인 
  - 해당 태그에 직접 style 속성 활용
2. 내부 참조 
  - `<style>` (`<head>`태그 내)
3. **외부 참조**
  - 분리된 CSS 파일 (`<head>` 내 `<link>`를 통해 불러오기)

<br/>

### CSS with 개발자 도구
- styles : 해당 요소에 선언된 모든 CSS
- computed : 해당 요소에 최종 계산된 css


<br/><br/>

---
## CSS Selectors
1. **기본 선택자**
☑️ 선택하고 스타일 지정하므로 선택자 필요

- 전체 선택자, 요소 선택자
- 클래스 선택자, 아이디 선택자, 속성 선택자

2. **결합자**
- 자손 결합자, 자식 결합자
- 일반 형제 결합자, 인접 형제 결합자

3. 의사 클래스/요소
- 링크, 동적 의사 클래스
- 구조적 의사 클래스, 기타 의사 클래스, 의사 엘리먼트, 속성 선택자

 #### 🔗 [css_selectors.html](https://github.com/Yonghyunc/TIL/blob/master/HTML/css_selectors.html)

<br/>

### CSS 선택자 정리
- 전체 선택자 (*)
- 요소 선택자
- 클래스 선택자 (.)
- 아이디 선택자 (#)
  - 중복될 수 있으니 하나의 고유한 id만 사용
- 속성 선택자
- 결합자

<br/>

### CSS 적용 우선순위
1. 중요도 ( !important )
2. 우선 순위
- 인라인 > id > class, 속성, pseudo-clss > 요소, pseudo-element
3. CSS 파일 로딩 순서

``` html
<p>1</p>
<p class="blue">2</p>
<p class="blue green">3</p>
<p class="green blue">4</p>
<p id="red" class="blue">5</p>
<h2 id="red" class="blue">6</h2>
<p id="red" class="blue" style="color: yellow;">7</p>
<h2 id="red" class="blue" style="color: yellow;">8</h2>
```
```css
h2 {
  color: dartviolet !important;
}
p {
  color: orange;
}
.blue {
  color: blue;
}
.green {
  color: green;
}
#red {
  color: red;
}
```
> 1 오렌지 : 클래스, ID X -> p태그 <br/>
> 2 블루 : 클래스 <br/>
> 3 그린 : css에서 뒤에 나온 클래스가 적용됨 <br/>
> 4 그린 : css에서 뒤에 나온 클래스가 적용됨 <br/>
> 5 레드 : ID <br/>
> 6 다크바이올렛 : h2태그 important <br/>
> 7 옐로우 : inline <br/>
> 8 다크바이올렛 : inline이 있어도 important 적용


<br/>

### CSS 결합자
- 자손 결합자 (공백) : 모든
  - `.box p` : box 클래스 아래의 모든 p태그

<br/>

- 자식 결합자 (>) : 한 단계 아래만
  - `.box > p` : box 클래스 한 단계 아래의 p
  - 
<br/>

- 일반 형제 결합자 (~) : 뒤에 있는 모든 형제
  - `p ~ span` : p 뒤의 모든 span 형제들

<br/>

- 인접 형제 결합자 (+) : 바로 옆 (같은 깊이)
  - `p + p` : p 에 병렬적으로 바로 뒤에 위치한 p
  - 바로 다음 라인에 붙어야 함!!!


<br/>

### CSS 상속
부모 요소의 속성을 자식에게 상속
- 상속 O : text 관련 요소 등
- 상속 X : box model 관련 요소, position 관련 요소 등

<br/><br/>

---

## CSS 기본 스타일

### 크기 단위
- px (픽셀) : 고정적인 단위
- % (백분율) : 가변적인 레이아웃
- em : 상속 영향 O, 상대적인 사이즈
- rem : 상속 영향 X, 최상위 요소 사이즈 기준

### 크기 단위 (viewport)
디바이스 화면을 기준으로 상대적인 사이즈 결정
- vw, vh, vmin, vmax

<br/>

### 색상 단위
- 색상 키워드
- RGB 색상 : #000000 / rgb()
- HSL 색상 : 색상, 채도, 명도

<br/>

### 문서 표현


<br/><br/>

---

## Box model
**CSS의 모든 요소는 네모(박스모델)이고,** <br/>
**위에서부터 아래로(Cascading), 왼쪽에서 오른쪽으로 쌓인다.**

<br/>

<img width="400" src=https://i.esdrop.com/d/f/GQtKpTuAPv/z2SJi6xPBN.png alt="box model">

- Margin : 테두리 바깥의 여백
- Border : 테두리
- Padding : border와 content 사이의 여백
- Content : 내용

<br/>

### box-sizing
- 기본적으로 모든 요소의 box-sizing은 content-box
- padding을 제외한 순수 contents 영역만을 box로 지정
- 다만, 우리가 일반적으로 영역을 볼 때는 border까지의 너비를 100px 보는 것을 원함
- 그 경우 box-sizing을 border-box로 설정

  <img width="400" src=https://i.esdrop.com/d/f/GQtKpTuAPv/bVwgWNv9nY.png alt="box sizing">

<br/><br/>

---

## Display

**모든 요소는 display에 따라 크기와 배치가 달라진다**

- **block**
  - 줄바꿈
  - 화면 크기 전체의 가로 폭 차지
> div / ul, ol, li / p / hr / form 등

<br/>

- **inline**
  - 줄바꿈 X
  - content 너비만큼 가로 폭 차지
  - width, height, margin-top, margin-bottom 지정 X
  - 상하 여백 => line-height
> span / a / img / input, label / b, em, i, strong 등

<br/>

- **inline-block**
  - block + inline
  - block처럼 행동하는데 겉으로 보이기에는 inline처럼 보임
    - 외부적 - inline (한 줄에 표시 가능)
    - 내부적 - block (width, height, margin 등 적용 가능)

<br/>

- none
  - 화면 표시 X, 공간 X

<br/>

- visibility: hidden
  - 화면 표시 X, 공간 O


<br/><br/>

---

## Position
문서 상에서 요소의 위치 지정
**CSS는 position으로 위치의 기준 변경**

<br/>

- static : 기준 위치 <br/>
모든 요소는 기본적으로 position이 static(↓→)

<br/>

1. relative : 상대 위치
- 자기 자신의 static 위치를 기준으로 이동
- static일 때 공간은 남겨두고 이동 -> top, left, right 등 이용하여 이동
- 모습만 이동, 공간은 그대로 차지

<br/>

2. absolute : 절대 위치
- 아무 공간을 차지하지 않고 붕 떠있음
- **static이 아닌** 가장 가까이 있는 부모/조상 요소를 기준으로 이동
- 부모 중에 static이 없으면 브라우저 화면 기준으로 이동
> absolute를 쓸 때는 부모를 항상 주의 깊게 봐야함!! (누구를 기준으로 움직이고 싶은지)

<br/>

3. fixed : 고정 위치
- viewport 기준으로 이동
- 스크롤 시에도 항상 같은 곳 위치
- 레이아웃 공간 차지 X

<br/>

4. sticky : 스크롤에 따라 static -> fixed로 변경
