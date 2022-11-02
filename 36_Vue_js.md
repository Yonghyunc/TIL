# TIL

[Front-end Framework](#front-end-framework)

[Vue](#vue)

[Vue instance](#vue-instance)

[Basic of Syntax](#basic-of-syntax)

[Directives](#directives)

[Vue advanced](#vue-advanced)

<br><br>

---

# Front-end Framework

▫ FE 개발이란 ? - 사용자에게 보여주는 화면 만들기  
▫ Web App (SPA)을 만들 때 사용하는 도구

<br>

### SPA (Single Page Application)
▫ 이전까지는 사용자 요청에 적절한 페이지 별 template 반환 (SSR)  
> 서버가 모든 것을 만들고 렌더링하여 제공 

▫ SPA 는 서버에서 최초 1장의 HTML만 전달받아 모든 요청에 대응   
➡ CSR 방식으로 요청 처리

<br>

### CSR (Client Side Rendering)
▫ 서버로부터 최초 한 장의 빈 HTML을 받아옴   
▫ 각 요청에 대한 대응을 JS를 사용하여 필요한 부분만 다시 렌더링  
1. 새로운 페이지를 서버에 **AJAX**로 요청
2. 서버는 화면을 그리기 위해 필요한 데이터를 JSON 방식으로 전달
3. **JSON** 데이터를 JS로 처리, DOM 트리에 반영 (렌더링)

> 서버 : 최초의 HTML + 데이터

<br>

### <장점>   
▫ 모든 HTML 페이지를 서버로부터 받아서 표시하지 않아도 됨 
- 트래픽 감소
- 응답 속도 빨라짐

▫ 매번 새 문서를 받아 새로고침하는 것이 아니라 필요한 부분만 고쳐 나가므로 각 요청이 끊김없이 진행  
- UX 향상

▫ BE와 FE의 작업 영역을 명확히 분리 O  
- 협업 용이

<br>

### <단점>  
▫ 첫 구동 시 필요한 데이터가 많으면 많을수록 최초 작동 시작까지 오랜 시간이 소요  
▫ 검색 엔진 최적화(SEO)가 어려움  

<br>

> SEO
> 
> ▫ 검색 = 각 사이트가 운용하는 검색 엔진에 의해 이루어지는 작업  
> ▫ 검색 엔진 = 웹 상에서 존재하는 가능한 모든 정보들을 긁어 모으는 방식으로 동작  
> 
> 최근 CSR로 구성된 서비스의 비중이 증가하며 SPA 서비스도 검색 대상으로 넓히기 위해 JS를 지원하는 방식으로 발전   
> ▫ BUT, 여전히 CSR의 검색 엔진 최적화 문제가 모두 해결 X

<br><br>

---

# Vue

▫ 구조가 매우 직관적   
▫ HTML - JS - CSS

``` js
<template>
  <!-- HTML -->
  <div>
    <p>Hello :)</p>
  </div>
</template>

<script>
  // JavaScript
</script>

<style>
  /* CSS */
  p {
    color: black;
  }
</style>
```
<br>


▫ Vue CDN

``` js
<script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
```

<br>

▫ Vue devtools에서 data 변경 -> DOM 반영  
▫ 눈에 보이는 화면을 조작하는 것이 아닌 Vue가 가진 data를 조작   
[03_html_vue.html](vue/03_html_vue.html)
![image](https://user-images.githubusercontent.com/93974908/198939304-1ef3007b-b938-41a5-8278-e4a4aa79781f.png)


▫ input tag에 `v-model="message"`
- input에 값 입력 -> Vue data 반영
- Vue data -> DOM 반영
![image](https://user-images.githubusercontent.com/93974908/198939677-19d72331-5f55-498d-a940-a1dcae19bd98.png)


Vue ➡ 변경사항 한번에 반영
1. Data changes
2. DOM re-render


<br><br>

# Vue instance

## MVVM Pattern
▫ 소프트웨어 아키텍쳐 패턴의 일종  

![image](https://user-images.githubusercontent.com/93974908/198940158-8bf20a78-8b82-4425-80e8-69a3e1a83b2d.png)

▫ Model과 View 사이에서 event를 듣고 조작하는 과정을 담당함 

### **M(model) - V(view) - VM(view model)**

▫ View : 우리 눈에 보이는 부분 = DOM  

▫ Model : 실제 데이터 = JSON  

▫ View Model (Vue) 
- View를 위한 Model 
- View와 연결(바인딩)되어 Action을 주고 받음 
- Model이 변경되면 View Model도 변경되고 바인딩된 View도 변경됨 
- View에서 사용자가 데이터를 변경하면 View Model의 데이터가 변경되고 바인딩된 다른 View도 변경됨 


> View와 Model은 서로 모른다 (직접소통 X)

<br>

![image](https://user-images.githubusercontent.com/93974908/198940784-e4c2c7f2-6219-48d9-9fd9-335d3e1e3716.png)

Vue instance === 1개의 객체

<br><br>

## 생성자 함수  - new 연산자  
``` js
function Member(name, age, sId) {
    this.name = name
    this.age = age
    this.sId = sId
}

const member3 = new Member('isaac', 21, 2022654321)
```
▫ 함수 이름은 반드시 대문자로 시작  
▫ 생성자 함수를 사용할 때는 반드시 new 연산자 사용  

<br><br>

## el
▫ Vue instance와 DOM을 연결하는 옵션
- View와 Model을 연결하는 역할
> 대부분 id로 연결 

▫ Vue instance와 연결되지 않은 DOM 외부는 Vue의 영향 X  

<br>

▫ el 옵션에 #app 작성 = DOM 연결
``` html
<div id="app">
</div>

<script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
<script>
const app = new Vue({
    el: '#app',
})
```

<br>

▫ Vue와 연결되지 않은 div 생성 
- 연결 O : message 속성이 정의 되지 않았다는 경고 
- 연결 X : {{ message }} 그대로 출력
``` html
  <div id="app">
    {{ message }}
  </div>

  <div>
    {{ message }}
  </div>
```
![image](https://user-images.githubusercontent.com/93974908/198943186-6d8ca4d5-d1d7-4d78-b1e3-a706afb55281.png)


<br><br>

## data 
▫ Vue instance의 데이터 객체 / 인스턴스 속성  
▫ 데이터 객체는 반드시 기본 객체 **{}** 여야 함   
▫ 객체 내부의 아이템들은 value로 모든 타입의 객체 O  
▫ 정의된 속성은 **interpolation`{{}}`** 을 통해 view 에 렌더링 가능

**this** => Vue의 메서드를 호출하는 객체


![image](https://user-images.githubusercontent.com/93974908/198943837-0d1b9cc0-7f08-4120-9b5b-a37f602f667a.png)

`$data` 생략가능   


<br><br>

## methods
▫ Vue instance의 method들을 정의하는 곳  

▫ method를 호출하여 data 변경 가능  

▫ 메서드를 정의할 때, Arrow Function 사용 XXXX   
- 화살표 함수의 this는 함수가 선언될 때 상위 스코프를 가리킴 (window)  
- 호출은 문제 없이 가능, BUT this로 Vue의 data 변경 X  

[04_vue_start.html](vue/04_vue_start.html)

![image](https://user-images.githubusercontent.com/93974908/198945242-fcaac75e-6734-402f-b758-220b870fc1ae.png)

<br><br>

---

# Basic of Syntax

### Template Syntax 
▫ **랜더링 된 DOM**을 기본 Vue instance의 data에 **선언적으로 바인딩** 할 수 있는 **HTML 기반 template syntax**를 사용  

- 렌더링 된 DOM : 브라우저에 의해 보기 좋게 그려질 HTML 코드
- HTML 기반 template syntax : HTML 코드에 직접 작성할 수 있는 문법 제공  
- 선언적으로 바인딩 : Vue instance와 DOM 연결  

<br>

[06_basic_of_sytax.html](vue/06_basic_of_syntax.html)

### Template Interpolation
▫ 가장 기본적인 바인딩 방법 {{ }}   
▫ HTML을 일반 텍스트로 표현  
``` html
<div id="app">
  <p>메시지: {{ msg }}</p>
</div>


<script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
<script>
  const app = new Vue({
    el: '#app',
    data: {
      msg: 'Text interpolation',
    }
  })
</script>
```

<br>

### RAW HTML 
▫ v-html을 사용하여 바인딩  
``` html
<div id="app">
  <p>HTML 메시지 : <span v-html="rawHTML"></span></p>
</div>


<script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
<script>
  const app = new Vue({
    el: '#app',
    data: {
      msg: 'Text interpolation',
      rawHTML: '<span style="color:red"> 빨간 글씨</span>'
    }
  })
</script>
```

<br>

### JS 표현식 

``` html
<div id="app">
  <p>{{ msg.split('').reverse().join('') }}</p>
</div>


<script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
<script>
  const app = new Vue({
    el: '#app',
    data: {
      msg: 'Text interpolation',
    }
  })
</script>
```

<br><br>

---

# Directives 
▫ v-접두사가 있는 특수 속성에는 값 할당 O   
- 값에는 JS 표현식 작성 O  


▫ 역할 : 표현식의 값이 변경될 때 반응적으로 DOM에 적용하는 것  

![image](https://user-images.githubusercontent.com/93974908/198946790-08efeb17-7a1e-41fc-b679-4181b881e154.png)

- `:` 을 통해 전달인자 받음 
- `.` 으로 표시되는 특수 접미사 ➡  directive를 특별한 방법으로 바인딩해야 함  


<br>

[06_basic_of_sytax.html](vue/06_basic_of_syntax.html)

▫ 각각의 instance들은 연결된 DOM element에만 영향을 미침  


### v-text 
▫ 가장 기본적인 바인딩   
▫ {{}} 와 동일한 역할 (정확히 동일 X)

``` html
<div id="app2">
  <p v-text="message"></p>
  <!-- 같음 -->
  <p>{{ message }}</p>
</div>

  <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
<script>
  const app2 = new Vue({
    el: '#app2',
    data: {
      message: 'Hello!',
    }
  })
</script>
```
<br>

### v-html  
▫ RAW HTML 표현  
단, 사용자가 입력하거나 제공하는 컨텐츠에는 절대 사용 금지 !!!  

``` html
<div id="app2">
  <p v-html="html"></p>
</div>

<script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
<script>
  const app2 = new Vue({
    el: '#app2',
    data: {
      message: 'Hello!',
      html: '<a href="https://www.google.com">GOOGLE</a>'
    }
  })
</script>
```
<br>

### v-show  
▫ 표현식에 작성된 값에 따라 element를 보여 줄 것인지 결정  
▫ 요소 자체는 항상 DOM에 렌더링 됨

``` html
<div id="app3">
  <p v-show="isActive">보이니? 안보이니?</p>
</div>

<script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
<script>
  const app3 = new Vue({
    el: '#app3',
    data: {
      isActive: false
    }
  })
</script>
```


### v-if
▫ v-if v-else-if v-els 형태로 사용  

``` html
<div id="app3">
  <p v-if="isActive">안보이니? 보이니?</p>
</div>

<script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
<script>
  const app3 = new Vue({
    el: '#app3',
    data: {
      isActive: false
    }
  })
</script>
```
<br>

### v-show VS v-if
> 사용목적 다름   

▫ v-show  
- 표현식 결과와 관계 없이 렌더링  
- 초기 렌더링에 필요한 비용은 v-if보다 높을 수 있음 
- display 속성 변경으로 표현 여부를 판단하므로 렌더링 후 toggle 비용 적음 


▫ v-if
- 표현식 결과가 false 인 경우 렌더링 조차 되지 않음 
- 초기 렌더링 비용은 v-show 보다 낮을 수 있음 
- 표현식 값이 자주 변경되는 경우 잦은 재 렌더링으로 비용이 증가할 수 있음 

<br>

### v-for

[07_basic_of_syntax_2.html](vue/07_basic_of_syntax_2.html)

▫ 반복한 데이터 타입에 모두 사용 가능  
▫ 각 요소가 객체라면 dot notation으로 접근 O  
▫ 객체 순회 시 value가 할당되어 출력  


⭐ 특수 속성 key    
- v-for 사용 시 반드시 key 속성을 각 요소에 작성   
- vue 화면 구성 시 이전과 달라진 점을 확인하는 용도로 활용  
- 각 요소가 고유한 값을 가지고 있지 않다면 생략 O  
> 여러 중복문의 key 값이 겹치면, view가 경고를 보냄  

key="index"  
key="`arry-${index}`"

> 객체는 key 값 사용 일반적  
> 배열에서는 인덱스 + 문자열  

> 인덱스를 안 쓰더라도 key용으로 쓰는 경우 多

<br>

### v-on

[08_basic_of_syntax_3.html](vue/08_basic_of_syntax_3.html)

▫ `:`을 통해 전달받은 인자를 확인  
▫ 값으로 JS 표현식 작성  
▫ 이벤트가 발생하면 할당된 표현식 실행  
> 이벤트는 addEventListener의 첫번째 인자와 같음  

▫ method를 통한 data 조작도 가능  
▫ method에 인자를 넘기는 방법은 일반 함수를 호출할 때와 동일   
▫ `:`을 통해 전달된 인자에 따라 특별한 modifiers가 있을 수 있음  

▫ 축약어 ➡ @


<br>

### v-bind
▫ HTML 기본 속성에 Vue data 연결  
- 조건부 바인딩 
- 다중 바인딩 

▫ Vue data의 변화에 반응하여 DOM에 반영하므로 상황에 따라 유동적 할당 가능   

▫ 축약어 ➡ :

<br>

### v-model 

[09_basic_of_syntax_4.html](vue/09_basic_of_syntax_4.html)

▫ Vue instance와 DOM의 **양방향 바인딩**  
▫ Vue data 변경 시 v-model로 연결된 사용자 입력 element에도 적용  


> 한글은 한글자를 모두 완성해야 출력됨 (하나의 글자가 만들어지려면 조합이 되어야하는 문자 해당)  
> IME

<br><br>

---

# Vue advanced

### computed 

[10_computed.html](vue/10_computed.html)

== methods  
> 하는 일은 똑같음   


▫ computed
- 처음에 한 번 실행 -> 이후 재사용  (종속된 사용자 값이 변할 때 재실행) 
- 소괄호 X (사용할 때는, 계산된 값이기 때문에)   

▫ methods 
- 사용할 때마다 재실행  
- 소괄호 사용  (메서드는 호출해야 함)   

<br>

### watch 

[11_watch.html](vue/11_watch.html)

▫ 특정 데이터의 변화 감지  
1. watch 객체 정의
2. 감시할 대상 data 지정
3. data가 변할 시 실행할 함수 정의

▫ 감시하던 대상이 변경되었을 때, 실행됨  
▫ 첫번째 인자 : 현재값  
▫ 두번째 인자 : 과거값
> 변화에 초점  

> watch의 함수이름이 감시하던 대상 이름과 같아야 함 

▫ 배열, 객체는 watch가 바로 들여다볼 수 없음 -> deep: true 사용 

<br>


### filters 

[12_filters.html](vue/12_filters.html)

▫ 텍스트 형식화 적용 O  
▫ interpolation / v-bind 이용할 때 사용 가능  
▫ `|`로 추가  
▫ 이어서 사용 (chaining)도 가능  

``` html
<div id="app">
  <p>{{ numbers }}</p>
  <p>{{ numbers | getOddNums }}</p>
  <p>{{ numbers | getUnderTenNums }}</p>
  <p>{{ numbers | getUnderTenNums | getOddNums}}</p>
</div>
```


<br><br>

---

# 스타일 가이드⭐
## 1. v-for은 항상 key와 함께 사용하기 
▫ 내부 컴포넌트의 상태를 일관되게 유지하기 위해 v-for에 항상 key를 사용하기  
▫ 데이터의 예측 가능한 행동을 유지 시키기 (객체 불변성)

``` js
todos: [
  { id: 1, text: 'Learn to use v-for' },
  { id: 2, text: 'Learn to use key' }
]
```

``` html
<ul>
  <li
    v-for="todo in todos"
    :key="todo.id"
  >
    {{ todo.text }}
  </li>
</ul>
```
<br><br>

## 2. v-for을 쓴 엘리먼트에 절대 v-if를 사용하지 말기 
### 1️⃣ 목록의 항목을 필터링할 때
v-for="user in users" v-if="user.isActive"

▫ Vue가 디렉티브를 처리할 때, v-for가 v-if보다 높은 우선순위를 가짐  
▫ 따라서 일부분에 대해 출력을 하고 싶어도, v-for가 우선순위를 가지므로 전체를 반복해야 하는 비효율  

<br>

▫ isActive가 true인 user에 대해서만 name을 출력하는 로직 

``` html
<!-- bad -->

<ul>
  <li
    v-for="user in users"
    v-if="user.isActive"
    :key="user.id"
  >
    {{ user.name }}
  </li>
</ul>
```
▫ BUT, v-for가 우선순위를 가지므로 전체 users에 대해 반복하고 있음  

⬇

▫ computed 속성을 대신 반복하여 이러한 비효율 해결 O  
``` js
computed: {
  activeUsers() {
    return this.users.filter((user) => user.isActive)
  }
}
```
``` html
<!-- good -->

<ul>
  <li
    v-for="user in activeUsers"
    :key="user.id"
  >
    {{ user.name }}
  </li>
</ul>
```

▫ 처음부터 isActive가 true인 user들만 따로 골라내서 해당 users에 대해서만 v-for로 반복  

<br><br>

### 2️⃣ 목록을 숨기기 위해 렌더링을 피할 때  
▫ v-if를 컨테이너 엘리먼트로 옮겨서 사용  

``` html
<ul v-if="shouldShowUsers">
  <li
    v-for="user in users"
    :key="user.id"
  >
    {{ user.name }}
  </li>
</ul>
```

▫ 더 이상 목록의 모든 사용자에 대해 shouldShowUsers를 확인하지 않도록 함  (전체 한번만 확인)  
▫ 한 번 확인하고 shouldShowUsers가 false인 경우 v-for를 평가 X  