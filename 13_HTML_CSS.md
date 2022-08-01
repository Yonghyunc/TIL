# Today I Learned
1. HTML
2. CSS


<br/>

---
# Web이란?
## 1. 웹 사이트의 구성 요소
▶️ 웹 사이트
- 브라우저를 통해 접속하는 웹 페이지 (문서) 들의 모음
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

<br/>

---

# HTML
Hyper Text Markup Language


### Hyper Text (팀 버너스리)
참조(하이퍼링크)를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트

### Markup Language
태그 등을 이용하여 문서나 데이터 구조를 명시하는 언어 <br/>
`<title>Hello, HTML</title>`

==> 웹 페이지를 작성(구조화)하기 위한 언어

<br/>

HTML 스타일 가이드 -- 2 space

<br/><br/>

## HTML 기본 구조
- html : 문서의 최상위 요소
- head : 문서 메타데이터 요소
- body : 실제 데이터 내용

ex) body(사진) -> head(찍은 장소, 시간, 해상도 등)

<br/>

### head 예시
- title : 브라우저 상단 타이틀                        
- meta : 문서 레벨 메타데이터 요소                   
- link : 외부 리소스 연결 요소 (CSS파일, favicon 등) 
- script : 스트립트 요소                               
- style : CSS 직접 작성                               

 #### 🔗 [head.html]()

<br/>

Open Graph Protocol

<br/><br/>

### 요소 = 태그 + 내용
- 시작 태그 / 종료 태그 / 태그 사이에 위치한 내용
- 태그로 내용을 감싸는 것 (정보의 성격, 의미 정의)
- 내용 없는 태그 존재 (-> 닫는 태그 X)
  - br, hr, img, input, link, meta
- 요소 중첩 가능
  - 중첩 통해 하나의 문서 구조화
  - 여는 태그, 닫는 태그 잘 확인 --> 오류 안 남 (깨진 상태로 출력)

### 속성
- 태그별로 사용할 수 있는 속성 다름
- =사용 시 공백 NO
- 쌍따옴표 사용 <br/>
`<a href="https://google.com"></a>`
- 태그의 부가적인 정보 설정
- 요소는 속성을 가질 수 있으며, 추가적인 정보 제공 (경로, 크기 등)
- 보통 이름과 값이 하나의 쌍으로 존재

<br/>

- 태그와 상관없이 사용 가능한 속성 존재 (HTML Global Attribute)
  - id : 문서 전체에서 유일한 고유 식별자 지정
  - class : 공백으로 구분된 해당 요소의 클래스의 목록
  - data-* : 페이지에 개인 사용자 정의 데이터를 저장하기 위해 사용
  - style : inline 스타일
  - title : 요소에 대한 추가 정보 지정
  - tabindex : 요소의 탭 순서

    <img width="350" src=https://i.esdrop.com/d/f/GQtKpTuAPv/36nqh6jmKO.png alt="HTML Global Attribute">

 #### 🔗 [html_basic.html]()

<br/><br/>

### 시맨틱 태그 - 의미적 가치
- header : 머리말
- nav : 내비게이션
- aside : 사이드, 메인과 관련성이 적은 콘텐츠
- section : 문서의 일반적인 구분, 컨텐츠의 그룹
- article : 문서, 페이지, 사이트 안에서 독립적으로 구분되는 영역
- footer : 마지막 부분

  <img width="300" src=https://i.esdrop.com/d/f/GQtKpTuAPv/B0REVNZ1lZ.png alt="시맨틱 태그">

❔시맨틱 태그를 사용해야 하는 이유 <br/>
: (의미론적 마크업) 검색엔진 등에 의미 있는 정보의 그룹을 태그로 표현 / 검색엔진 최적화(SEO)

<br/><br/>

**렌더링** : 웹사이트 코드를 사용자가 보게 되는 웹 사이트로 바꾸는 과정 <br/>
**DOM (Document Object Model) 트리** : 텍스트 파일인 HTML 문서를 브라우저에서 렌더링 하기 위한 구조


<br/><br/>

---

## HTML 문서 구조화
요소 <br/>
➡️ 인라인 요소 : 글자처럼 취급 <br/>
➡️ 블록 요소 : 한 줄 모두 사용

 <br/>

### 텍스트 요소
  <img width="400" src=https://i.esdrop.com/d/f/GQtKpTuAPv/pcEU5uOfQb.png alt="텍스트 요소">

 <br/>

### 그룹 컨텐츠
  <img width="400" src=https://i.esdrop.com/d/f/GQtKpTuAPv/ShvmNHTdYG.png alt="그룹 컨텐츠">
  <img width="300" src=https://i.esdrop.com/d/f/GQtKpTuAPv/0f1r7a3Avy.png alt="그룹 컨텐츠2">

<br/>

### form
- 정보(데이터)를 서버에 제출하기 위해 사용하는 태그 <br/>
ex) 로그인(ID, PW) -> 서버 전송 // 게시글 작성 -> 서버 전송

- 기본 속성
  - action : form을 처리할 서버의 URL (데이터를 보낼 곳)
  - method : form을 제출할 때 사용할 HTTP 메서드 (GET / POST)
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

 #### 🔗 [form.html]()

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