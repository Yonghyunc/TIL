# TIL

[Front-end Framework](#front-end-framework)

[Vue](#vue)

<br><br>

---

# Front-end Framework

▫ FE 개발이란 ? - 사용자에게 보여주는 화면 만들기  
▫ Web App (SPA)을 만들 때 사용하는 도구


### SPA (Single Page Application)
▫ 이전까지는 사용자 요청에 적절한 페이지 별 template 반환 (SSR)  
> 서버가 모든 것을 만들고 렌더링하여 제공 

▫ SPA 는 서버에서 최초 1장의 HTML만 전달받아 모든 요청에 대응   
➡ CSR 방식으로 요청 처리

### CSR (Client Side Rendering)
▫ 서버로부터 최초 한 장의 빈 HTML을 받아옴   
▫ 각 요청에 대한 대응을 JS를 사용하여 필요한 부분만 다시 렌더링  
1. 새로운 페이지를 서버에 **AJAX**로 요청
2. 서버는 화면을 그리기 위해 필요한 데이터를 JSON 방식으로 전달
3. **JSON** 데이터를 JS로 처리, DOM 트리에 반영 (렌더링)

> 서버 : 최초의 HTML + 데이터

<장점>   
▫ 모든 HTML 페이지를 서버로부터 받아서 표시하지 않아도 됨 
- 트래픽 감소
- 응답 속도 빨라짐

▫ 매번 새 문서를 받아 새로고침하는 것이 아니라 필요한 부분만 고쳐 나가므로 각 요청이 끊김없이 진행  
- UX 향상

▫ BE와 FE의 작업 영역을 명확히 분리 O  
- 협업 용이

<단점>  
▫ 첫 구동 시 필요한 데이터가 많으면 많을수록 최초 작동 시작까지 오랜 시간이 소요  
▫ 검색 엔진 최적화(SEO)가 어려움  

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

``` vue
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

Vue CDN

``` vue
<script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
```

[03_html_vue.html](vue/03_html_vue.html)
![image](https://user-images.githubusercontent.com/93974908/198939304-1ef3007b-b938-41a5-8278-e4a4aa79781f.png)


v-model="message"
![image](https://user-images.githubusercontent.com/93974908/198939677-19d72331-5f55-498d-a940-a1dcae19bd98.png)


Vue => 변경사항 한번에 반영
1. Data changes
2. DOM re-render


<br><br>

## Vue instance

MVVM Pattern
▫ 소프트웨어 아키텍쳐 패턴의 일종  

![image](https://user-images.githubusercontent.com/93974908/198940158-8bf20a78-8b82-4425-80e8-69a3e1a83b2d.png)

Model과 View 사이에서 event를 듣고 조작하는 과정을 담당함 
M(model) - V(view) - VM(view model)

▫ View : 우리 눈에 보이는 부분 = DOM  
▫ Model : 실제 데이터 = JSON  
▫ View Model (Vue) 
- View를 위한 Model 
- View와 연결(바인딩)되어 Action을 주고 받음 
- Model이 변경되면 View Model도 변경되고 바인딩된 View도 변경됨 
- View에서 사용자가 데이터를 변경하면 View Model의 데이터가 변경되고 바인딩된 다른 View도 변경됨 


> View와 Model은 서로 모른다 (직접소통 X)

![image](https://user-images.githubusercontent.com/93974908/198940784-e4c2c7f2-6219-48d9-9fd9-335d3e1e3716.png)

Vue instance === 1개의 객체

### 생성자 함수  
new 연산자  
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

### el
▫ Vue instance와 DOM을 연결하는 옵션
- View와 Model을 연결하는 역할
> 대부분 id로 연결 

▫ Vue instance와 연결되지 않은 DOM 외부는 Vue의 영향 X  


``` html
<div id="app">
</div>

<script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
<script>
const app = new Vue({
    el: '#app',
})
```

▫ Vue와 연결되지 않은 div 생성 
``` html
  <div id="app">
    {{ message }}
  </div>

  <div>
    {{ message }}
  </div>
```
![image](https://user-images.githubusercontent.com/93974908/198943186-6d8ca4d5-d1d7-4d78-b1e3-a706afb55281.png)


### data 
▫ Vue instance의 데이터 객체 / 인스턴스 속성  
▫ 데이터 객체는 반드시 기본 객체 **{}** 여야 함   
▫ 객체 내부의 아이템들은 value로 모든 타입의 객체 O  
▫ 정의된 속성은 **interpolation`{{}}`** 을 통해 view 에 렌더링 가능

this => Vue의 메서드를 호출하는 객체


![image](https://user-images.githubusercontent.com/93974908/198943837-0d1b9cc0-7f08-4120-9b5b-a37f602f667a.png)

`$data` 생략가능   


### methods
▫ Vue instance의 method들을 정의하는 곳  

▫ method를 호출하여 data 변경 가능  

▫ 메서드를 정의할 때, Arrow Function 사용 XXXX   
화살표 함수의 this는 함수가 선언될 때 상위 스코프를 가리킴 (window)  
호출은 문제 없이 가능, BUT this로 Vue의 data 변경 X  

![image](https://user-images.githubusercontent.com/93974908/198945242-fcaac75e-6734-402f-b758-220b870fc1ae.png)

<br><br>

---

### Basic of Syntax

v-html


## Directives 
v-접두사가 있는 특수 속성에는 값 할당 O
값에는 JS 표현식 작성 O  
표현식의 값이 변경될 때 반응적으로 DOM에 적용하는 것  

![image](https://user-images.githubusercontent.com/93974908/198946790-08efeb17-7a1e-41fc-b679-4181b881e154.png)

: 을 통해 전달인자 받음 
. 으로 표시되는 특수 접미사 -  directive를 특별한 방법으로 바인딩해야 함  


v-text 
가장 기본적인 바인딩 
{{}} 와 동일한 역할 (정확히 동일 X)

v-html  
RAW HTML 표현  
단, 사용자가 입력하거나 제공하는 컨텐츠에는 절대 사용 금지 !!!  


v-show  
표현식에 작성된 값에 따라 element를 보여 줄 것인지 결정  


v-if


사용목적 다름   

v-for

특수 속성 key    
v-for 사용 시 반드시 key 속성을 각 요소에 작성   
각 요소가 고유한 값을 가지고 있지 않다면 생략 O  
> 여러 중복문의 key 값이 겹치면, view가 경고를 보냄  

key="index"
key="`arry-${index}`"

> 객체는 key 값 사용 일반적  
> 배열에서는 인덱스 + 문자열  

> 인덱스를 안 쓰더라도 key용으로 쓰는 경우 多

v-on
이벤트 
v-on의 축약어 @  



v-bind -> :

v-model 
양방향 바인딩  


> 09. => 2번 방식 
> 한글은 한글자를 모두 완성해야 출력됨 (하나의 글자가 만들어지려면 조합이 되어야하는 문자 해당)  
> IME

10.html

computed == methods  
하는 일은 똑같음   
computed는 처음에 한 번 실행 -> 이후 재사용  (종속된 사용자 값이 변할 때 재실행) / 소괄호 X (사용할 때는, 계산된 값이기 때문에)   
methods -> 사용할 때마다 재실행  / 소괄호 사용  (메서드는 호출해야 함)   


watch 
특정 데이터의 변화 감지  
감시하던 대상이 변경되었을 때, 실행됨
첫번째 인자 : 현재값  
두번째 인자 : 과거값
> 변화에 초점  

> watch의 함수이름이 감시하던 대상 이름과 같아야 함 

배열, 객체는 watch가 바로 들여다볼 수 없음 -> deep: true 사용 


filters 
