# TIL

[DOM](#dom)

[Event](#event)

[this](#this)

<br><br>

---

# DOM

### Browser APIs

▫ 웹 브라우저에 내장된 API로, 웹 브라우저가 현재 컴퓨터 환경에 관한 데이터를 제공하거나, 오디오를 재생하는 등 여러가지 유용하고 복잡한 일을 수행할 수 있게 함   
▫ 자바스크립트로 사용  

▫ 종류
- DOM
- Geolocation API - 지리정보
- WebGL - 그래픽
- 등등


<br><br>

## DOM
> 브라우저가 기본적으로 제공 


▫ 문서 객체 모델  
▫ 문서의 구조화된 표현을 제공   
▫ 프로그래밍 언어 (자바스크립트)가 DOM 구조에 접근할 수 있는 방법 제공   
> 웹 페이지 변경 위해서는 접근이 필요함!! 

- 문서 구조, 스타일, 내용 등을 쉽게 변경 O
- HTML 콘텐츠 추가, 제거, 변경하고, 동적으로 페이지에 스타일을 추가하는 등 HTML/CSS 조작 O

▫ HTML 문서를 구조화하여 **각 요소는 객체로 취급**  
▫ 프로그래밍 언어적 특성을 활용한 조작 가능  

> 웹 페이지 결과물을 불러오려면, HTML / CSS / JavaScript 필요  
> JS는 브라우저에서 DOM API를 통해 문서를 동적으로 수정, 사용자 인터페이스 실시간 업데이트  

▫ DOM은 문서를 논리 트리로 표현  

▫ 웹 페이지는 일종의 문서  
▫ DOM은 웹 페이지의 객체 지향 표현   ➡ 스크립트 언어(ex. 자바스크립트)를 이용해 DOM 수정 O 

<br>

### DOM의 주요 객체
1️⃣ window   
▫ DOM을 표현하는 창   
▫ 가장 최상위 객체 (작성 시 생략 가능)   
> 창 전체를 의미  
> 크롬 : 하나의 탭 

``` 
▫ 새 탭 열기
> window.open()

▫ 경고 대화 상자 표시
> window.alert()

▫ 인쇄 대화 상자 표시
> window.print()
```

<br>

2️⃣ document   

▫ 브라우저가 불러온 웹 페이지  

▫ window의 하위 객체  
▫ 문서 전체를 의미   

> **파싱**   
> 
> ▫ 구문 분석, 해석  
> ▫ 브라우저가 문자열을 해석하여 DOM Tree로 만드는 과정    

<br>

▶ navigator, location, history, screen 등 

<br><br>

## DOM 조작
▫ DOM 조작 순서
1. 선택
2. 조작 (생성, 추가, 삭제 등)


<br>

### 선택 관련 메서드 

1️⃣ document.querySelector(선택자)  -- 단일 선택   
▫ 제공한 선택자와 일치하는 element **한 개** 선택  
▫ 첫 번째 element 객체 반환 

2️⃣ document.querySelectorAll(선택자)  -- 다증 선택   
▫ 제공한 선택자와 일치하는 **여러** element 선택  
▫ 문자열로 받음  
▫ NodeList를 반환  

> # = id   
> . = class

``` html
  <script>
      console.log(document.querySelector('#title'))
    console.log(document.querySelectorAll('.text'))
    console.log(document.querySelector('.text'))
    console.log(document.querySelectorAll('body > ul > li'))
  </script>
```

![image](https://user-images.githubusercontent.com/93974908/197454740-0212d3d5-aabb-45ba-89e7-548c59376864.png)

> **NodeList**  
> 
> ▫ index로만 각 항목에 접근 가능   
> ▫ 다양한 배열 메서드 사용 가능 (ex. forEach)  
> ``` html
> liTags = document.querySelectorAll('body > ul > li')
>
>liTags.forEach(element => {
>    console.log(element)
>})
>```
> ![image](https://user-images.githubusercontent.com/93974908/197454961-2d4a1d22-a0c5-4b51-8665-60e66ee99e70.png)
> 
> ▫ querySelectorAll()에 의해 반환되는 NodeList는 DOM의 변경사항을 실시간 반영 X
>> 순회, 길이 => 실시간 반영 시 역효과 => 정적 NodeList 반환  
>> 실시간으로 반영되는 타입도 존재  


<br>

### 조작 관련 메서드  
1️⃣ 생성 : document.createElement(tagName)    
▫ 작성한 tagName의 HTML 요소를 생성하여 **반환** (변수에 담아 사용 가능) 

2️⃣ 입력 : Node.innerText   
> 속성값  
▫ 태그와 태그 사이 텍스트 형태 입력값     
▫ 줄 바꿈 인식, 숨겨진 내용 무시 등 

3️⃣ 추가 : Node.appendChild()   
> Node : 하나하나의 태그 

▫ 괄호 안의 Node(태그)를 특정 부모 Node의 자식 NodeList 중 마지막 자식으로 삽입  
▫ 한번에 오직 하나의 Node 만 추가 가능  
▫ 추가된 Node 객체 **반환** 

4️⃣ 삭제 : Node.removeChild()    
▫ DOM 에서 자식 Node 제거  
▫ 제거된 Node **반환**  

<br>

![image](https://user-images.githubusercontent.com/93974908/197456540-5d58b547-ed6b-429c-9cbc-0b3d2231f862.png)
<br>

5️⃣ 속성 조회 및 설정  
▫ Element.getAttribute(name)   
- 해당 요소의 지정된 값(문자열) 반환  

▫ Element.setAttribute(name, value)
- 지정된 요소의 값 설정 
- 속성이 이미 존재하면 값 갱신, 존재하지 않으면 새 속성 추가 

<br>
``` html
  <script>
    const aTag = document.createElement('a')
    aTag.setAttribute('href', 'https://google.com')
    aTag.innerText = '구글'

    const divTag = document.querySelector('div')
    divTag.appendChild(aTag)

    const h1Tag = document.querySelector('h1')
    h1Tag.classList.toggle('blue')
  </script>
```

![image](https://user-images.githubusercontent.com/93974908/197459264-6b9b8cc3-738d-48f6-bd08-57c240069bea.png)

<br>

![image](https://user-images.githubusercontent.com/93974908/197459738-c89a60ed-a8ea-4387-b823-40d01dc5000d.png)
> red 위에 blue가 덮어써짐

<br><br>

---

# Event 
▫ 프로그래밍하고 있는 시스템에서 일어나는 사건 혹은 발생   
▫ 각 이벤트에 대해 조작할 수 있도록 특정 시점을 시스템이 알려주는 것  
> 웹 페이지 버튼을 클릭한다면, 이벤트 발생 --> 클릭이라는 사건에 대한 결과를 받거나 조작 가능 

<br>

## Event object
▫ 네트워크 활동이나 사용자와의 상호작용 같은 사건의 발생을 알리기 위한 객체   
▫ 이벤트 발생 (사용자 행동, 특정 메서드 호출 등)   

1️⃣ DOM 요소는 Event를 받고 (**수신**)   
2️⃣ 받은 Event를 **처리**할 수 있음   
-  addEventListener() : html 요소에 부착

<br>

### addEventListener()  
"**대상**에 *특정 Event*가 발생하면 할 일 등록"   
**EventTarget**.addEventListener(*type*, listener)   

▫ 지정한 Event가 대상에 전달될 때마다 호출할 함수 설정  
▫ Event를 지원하는 모든 객체를 대상으로 지정 가능 

▫ type 
- 반응할 Event 유형을 나타내는 대소문자 구분 문자열  
- input, click, submit ...
- [다양한 이벤트](https://developer.mozilla.org/en-US/docs/Web/Events)

▫ listener 
- 지정된 타입의 Event를 수신할 객체 
- 콜백 함수가 들어가야 함 
- 콜백 함수는 발생한 Event의 데이터를 가진 Event 기반 객체를 **유일한** 매개변수로 받음  

<br>
▫ 버튼을 클릭하면, 특정 변수 값 변경  
``` html
<body>
  <button id="btn">버튼</button>
  <p id="counter">0</p>

  <script>
    const btn = document.querySelector('#btn')
    let countNum = 0

    // 이벤트 핸들러 작성 
    btn.addEventListener('click', function (event) {
      const pTag = document.querySelector('#counter')
      countNum += 1
      pTag.innerText = countNum
    })
  </script>
</body>
```


<br>

▫ input에 입력하면, 입력 값을 실시간으로 출력 
> 이벤트에 모든 데이터가 다 들어있음

``` html
<body>
  <input type="text" id="text-input">
  <p></p>
  <script>
    // 1. input 선택
    const inputTag = document.querySelector('#text-input')

    // 2. 이벤트 핸들러 부착
    inputTag.addEventListener('input', function (event) {

      const pTag = document.querySelector('p')
      // console.log(event.target.value)
      pTag.innerText = event.target.value
    })
  </script>
</body>
```

<br>

▫ input에 입력하면, 입력 값을 실시간으로 출력 + 버튼을 클릭하면, 출력된 값의 클래스 토글  
![image](https://user-images.githubusercontent.com/93974908/197464921-28d8e570-af85-48b9-b03a-51b89970bc02.png)

``` html
<body>
  <h1></h1>
  <button id="btn">클릭</button>
  <input type="text">

  <script>
    const btn = document.querySelector('#btn')
    btn.addEventListener('click', function (event) {
      const h1Tag = document.querySelector('h1')
      h1Tag.classList.toggle('blue')
    })

    const inputTag = document.querySelector('input')
    inputTag.addEventListener('input', function (event) {
      const h1Tag = document.querySelector('h1')
      h1Tag.innerText = event.target.value
    })

  </script>
</body>
```

<br>

### Event 취소 - event.preventDefault()

▫ 현재 Event의 기본 동작 중단  
▫ HTML 요소의 기본 동작을 작동하지 않게 막음  

``` html
<body>
  <div>
    <h1>정말 중요한 내용</h1>
  </div>

  <script>
    const h1Tag = document.querySelector('h1')
    h1Tag.addEventListener('copy', function (event) {
      event.preventDefault()
      alert('복사 노노')
    })
  </script>
</body>
```

![image](https://user-images.githubusercontent.com/93974908/197467238-249a1aba-f7f6-41db-ba52-0c7663300bf6.png)

<br><br>

## Event 종합 실습 

### ▫ 버튼을 클릭하면, 랜덤 로또 번호 6개 출력  


자바스크립트 - 랜덤 모듈 X 

프로그래밍 기능 도움 라이브러리 - lodash(_)

``` html
<body>
  <h1>로또 추천 번호</h1>
  <button id="lotto-btn">행운 번호 받기</button>
  <div id="result"></div>

  <script src="https://cdn.jsdelivr.net/npm/lodash@4.17.21/lodash.min.js"></script>
  <script>
    const btn = document.querySelector('#lotto-btn')
    btn.addEventListener('click', function (event) {

      // 공이 들어갈 컨테이너 생성
      const ballContainer = document.createElement('div')
      ballContainer.classList.add('ball-container')

      // 랜덤한 숫자 6개 만들기
      const numbers = _.sampleSize(_.range(1, 46), 6)

      // 공 만들기
      numbers.forEach((number) => {
        const ball = document.createElement('div')
        ball.innerText = number
        ball.classList.add('ball')
        ball.style.backgroundColor = 'crimson'
        ballContainer.appendChild(ball)
      })
      // 공 컨테이너는 결과 영역의 자식으로 넣기
      const resultDiv = document.querySelector('#result')
      resultDiv.appendChild(ballContainer)
    })


  </script>
</body>
```

![image](https://user-images.githubusercontent.com/93974908/197469684-aeb612ed-8f41-42f9-9e6d-aff566aee46a.png)

<br>

### ▫ CREATE, READ 기능을 충족하는 todo app 만들기

``` html
<body>
  <form action="#">
    <input type="text" class="inputData">
    <input type="submit" value="Add">
  </form>
  <ul></ul>

  <script>
    // 폼의 기본 이벤트 막기
    const formTag = document.querySelector('form')

    const addTodo = function (event) {
      event.preventDefault()

      // 입력값 저장
      const inputTag = document.querySelector('.inputData')
      const data = inputTag.value

      if (data.trim()) {
        const liTag = document.createElement('li')
        liTag.innerText = data

        const ulTag = document.querySelector('ul')
        ulTag.appendChild(liTag)

        event.target.reset()
      } else {
        alert('내용 입력 ㄱㄱ ')
      }
    }

    formTag.addEventListener('submit', addTodo) 
  </script>
</body>
```

> 콜백함수에 이름을 붙여서 빼내줌 - 재사용 가능 


![image](https://user-images.githubusercontent.com/93974908/197471737-3f3233db-f1fd-4607-a205-e4ffbaaa4388.png)

![image](https://user-images.githubusercontent.com/93974908/197471993-2ff2472c-aecd-4e54-8856-b6052932d339.png)

<br><br>

---

# this
▫ 어떠한 object를 가리키는 키워드  
> 자바 - this, 파이썬 - self  => 인스턴스 자기자신


▫ 자바스크립트의 함수는 호출될 때 this를 암묵적으로 전달 받음  

▫ 자바스크립트는 해당 함수 호출 방식에 따라 this에 바인딩 되는 객체가 달라짐 
> 다른 프로그래밍 언어는 어디서 호출되었는지에 따라 값이 고정되어 있음 

▫ 즉, 함수를 호출할 때 **함수가 어떻게 호출 되었는지에 따라 동적으로 결정됨**  

"HOW"

<br>

1. 전역 문맥에서의 this - 고정 
2. **함수** 문맥에서의 this
    - 단순 호출
    - Method (객체의 메서드)
    - Nested


<br>

###  전역 문맥에서의 this
▫ 브라우저의 전역 객체인 window를 가리킴  
> 전역객체 = 모든 객체의 유일한 최상위 객체

## 함수 문맥에서의 this

▫ this의 값은 함수를 호출한 방법에 의해 결정됨  

1️⃣ 단순 호출   
▫ 전역 객체  
▫ 브라우저 - window  
▫ Node.js - global 

2️⃣ Method   
▫ 메서드로 선언하고 호출한다면, 객체의 메서드이므로 해당 객체가 바인딩

> this = 본인을 호출한 메서드

3️⃣ Nested (Function 키워드)   
▫ forEach의 콜백 함수에서의 this가 메서드의 객체를 가리키지 못하고 전역 객체 window를 가리킴  
``` js
const myObj = {
    numbers: [1],
    myFunc() {
        console.log(this)           // myObj
        this.numbers.forEach(function (number) {
            console.log(number)     // 1
            console.log(this)       // window
        })
    }
}
```
▫ 단순 호출이므로 thid -> window  

▫ 어떻게 해결? ➡ 화살표 함수
``` js
const myObj = {
    numbers: [1],
    myFunc() {
        console.log(this)           // myObj
        this.numbers.forEach((number) => {
            console.log(number)     // 1
            console.log(this)       // myObj
        })
    }
}
```
▫ 화살표 함수에서 this는 자신을 감싼 정적 범위  
▫ 화살표 함수는 호출의 위치와 상관없이 상위 스코프를 가리킴  
> Lexical scope this  
> ▫ 함수를 어디서 호출하는지가 아니라 어디에 선언하였는지에 따라 결정  
> ▫ Static scope - 대부분의 프로그래밍 언어에서 따름  

> 함수 내의 함수 상황에서 this 를 쓸거면 화살표 함수 (기능상의 차이 X)

❌ BUT addEventListener에서 콜백 함수는 화살표 함수 ❌   
addEventListener 에서의 콜백 함수는 
- function 키워드인 경우, event.target  
- 화살표 함수의 경우, 전역(window)

<br>

▫ this가 호출되는 순간에 결정되는 것 (런타임)  
장점  
- 함수(메서드)를 하나만 만들어서 여러 객체에서 재사용할 수 있음

단점 
- 이런 유연함이 실수로 이어질 수 있음

> JS this가 좋은지 나쁜지 판단하는 게 중요한 것은 아님! 