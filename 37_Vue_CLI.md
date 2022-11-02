# TIL


[Vue CLI](#vue-cli)

[SFC](#sfc)

[Pass Props & Emit Events](#pass-props--emit-events)

<br><br>

---

# Vue CLI

## Node.js
▫ 자바스크립트는 브라우저를 조작하는 유일한 언어 ➡ BUT, 브라우저 밖에서는 구동 X  
▫ 자바스크립트를 구동하기 위한 런타임 환경인 Node.js로 인해 브라우저가 아닌 환경에서도 구동 O  

<br>

### NPM (Node Package Manage)  
▫ 자바스크립트 패키지 관리자  
- pip와 마찬가지로 다양한 의존성 패키지 관리  

▫ Node.js의 기본 패키지 관리자  (설치 시 함께 설치 O)  

<br><br>

## Vue CLI  
▫ Vue 개발을 위한 표준 도구  


▫ 설치 (위치 상관 X)  
`$ npm install -g @vue/cli`

▫ 프로젝트 생성 (vscode terminal에서 진행)  
`$ vue create vue-cli`

▫ Vue 버전 선택  
![image](https://user-images.githubusercontent.com/93974908/199365248-31c3dd6e-450b-407d-ba51-ccb48f14e19f.png)

> 프로젝트를 성공적으로 만들면 폴더가 생성됨 => 폴더 내부로 이동해야 함  


▫ 프로젝트 디렉토리로 이동  
`$ cd vue-cli`


▫ 프로젝트 실행  
`$ npm run serve`

![image](https://user-images.githubusercontent.com/93974908/199365579-179eac51-c0e6-4888-a70c-83d0d6b19972.png)

> 서버 끄는 방법 : ctrl + c


<br><br>

## Vue CLI 프로젝트 구조   

> git init이 되어있는 상태로 만들어짐  
> 이미 git을 하고 있는 폴더 내부에서 만들 경우 반드시 .git을 지워줘야 함  

![image](https://user-images.githubusercontent.com/93974908/199365979-08685a51-a86f-4f4f-ae1e-57c728734a1a.png)

<br>

### 📁 node_modules  
▫ node.js 환경의 여러 의존성 모듈  
▫ python의 **venv**와 비슷한 역할 ➡ 매우 무거움 (.gitignore에 추가되어있음)

### 📝 Babel 
> babel.config.js

▫ "JavaScript complier"  
▫ 자바스크립트의 ES6+ 코드를 구버전으로 번역/변환  
➡ 원시 코드(최신 버전)를 목적 코드(구 버전)로 옮기는 과정  

### 📝 Webpack
▫ "static module bundler" 
> module ➡ .js

▫ 모듈 간의 의존성 문제를 해결하기 위한 도구  
▫ 프로젝트에 필요한 모든 모듈을 매핑하고 내부적으로 종속성 그래프를 빌드함  

<br>

### module
▫ 개발하는 애플리케이션의 크기가 커지고 복잡해지면 파일 하나에 모든 기능을 담기가 어려워짐  
▫ 따라서 자연스럽게 파일을 여러 개로 분리하여 관리 하게 되었고, 이때 분리된 파일 각각이 모듈 ➡ 즉, **js 파일 하나가 하나의 모듈**  
▫ 모듈을 대개 기능 단위로 분리하며, 클래스 하나 혹은 특정한 목적을 가진 복수의 함수로 구성된 라이브러리 하나로 구성됨   
▫ ESM, AMD, CommonJS, UMD 등  

✔ module의 의존성 문제 
▫ 모듈의 수가 많아지고 라이브러리 혹은 모듈 간의 의존성이 깊어지면서 특정한 곳에서 발생한 문제가 어떤 모듈 간의 문제인지 파악 어려움  
➡ **모듈 간 의존성 문제 해결 위해 Webpack 등장**  

<br>

### Bundler 
▫ 모듈 의존성 문제를 해결해주는 작업 : 번들링 (Bundling)  
▫ 모듈들을 하나로 묶어주고 묶인 파일은 하나(혹은 여러 개)로 만들어짐  
▫ 번들링된 결과물은 개별 모듈의 실행 순서에 영향을 받지 않고 동작  

▫ Vue CLI는 이러한 Babel, Webpack에 대한 초기 설정이 자동으로 되어 있음

> 2016, left-pad  
> 
[Deno](https://deno.land/) - Node.js의 문제점 개선 (스스로)

<br><br>

### 📝 package.json  
▫ 프로젝트의 종속성 목록과 지원되는 브라우저에 대한 구성 옵션 포함 


<br>

### 📝 package-lock.json
▫ node_modules에 설치되는 모듈과 관련된 모든 의존성을 설정 및 관리  
▫ 협업 및 배포 환경에서 정확히 동일한 종속성을 설치하도록 보장하는 표현  
▫ 사용할 패키지 버전 고정  
▫ 개발 과정 간 의존성 패키지 충돌 방지  
▫ python의 **requirements.txt** 역할  
> npm 설치하면 자동으로 업데이트 (수정 필요 X)


<br>

### ⭐ public/index.html 
![image](https://user-images.githubusercontent.com/93974908/199371213-20ff6594-56d6-49c1-b6f8-443f8cc4e72a.png)

▫ Vue 앱의 뼈대가 되는 html 파일  
▫ Vue 앱과 연결될 요소 O  

▫ favicon.ico
![image](https://user-images.githubusercontent.com/93974908/199371057-903bd392-52f3-46b7-a003-2433849b170a.png)

▫ 다른 문서와 연결되는 코드 
``` html
<div id="app"></div>
```

<br>

### 📁 src
![image](https://user-images.githubusercontent.com/93974908/199371304-af937ad9-8852-44d1-8bf8-1ccce4fa37e4.png)

▫ src/assets 
- 정적 파일을 저장하는 디렉토리 

▫ scr/components
- 하위 컴포넌트들이 위치  

▫ src/App.vue
- 최상위 컴포넌트 
- public/index.html 과 연결됨   

▫  src/main.js
- webpack이 빌드를 시작할 때 가장 먼저 불러오는 entry point
- index.html과 App.vue를 연결시키는 작업 
- Vue 전역에서 활용할 모듈을 등록할 수 있는 파일 (별도 수정 X)


<br><br>

---
# SFC

## Component
▫ UI를 독립적이고 **재사용** 가능한 조각들로 나눈 것  
▫ CS에서는 다시 사용할 수 있는 범용성을 위해 개발된 소프트웨어 구성 요소를 의미  
▫ 하나의 app을 구성할 때 중첩된 컴포넌트들의 tree로 구성하는 것이 보편적  
▫ src/App.vue를 root node로 하는 tree의 구조를 가짐  
▫ 유지보수 쉬움 + 재사용성  

▫ 우리가 사용하는 웹 서비스는 여러 개의 컴포넌트로 이루어져 있음  
▫ 하나의 컴포넌트를 만들어두면 반복되는 UI를 쉽게 처리할 수 있음  

### Component 기반 architecture 특징 
▫ 관리 용이 ➡ 유지/보수 비용 감소  
▫ 재사용성  
▫ 확장 가능  
▫ 캡슐화  
▫ 독립적  

<br>

> Vue에서 말하는 Component란? ➡ 이름이 있는 재사용 가능한 Vue instance

<br><br>

## SFC (Single File Component)
▫ 하나의 .vue 파일이 하나의 Vue instance이고, 하나의 컴포넌트  
▫ Vue instance에서는 HTML, CSS, JavaScript 코드를 한번에 관리  
➡ Vue instance를 기능 단위로 작성!!!!!  
▫ 컴포넌트 기반 개발의 핵심 기능  

![image](https://user-images.githubusercontent.com/93974908/199373067-64a77f0b-3ce1-4955-8cfd-23e60d5786eb.png)

<br><br>

## Vue component 

![image](https://user-images.githubusercontent.com/93974908/199373504-d13b38f9-e999-4a5f-a681-854ced3626f2.png)

### 🔹 템플릿 (HTML)
▫ HTML의 body 
▫ 눈으로 보여지는 부분  
▫ 다른 컴포넌트를 HTML 요소처럼 추가 가능  

### 🔹 스크립트 (JavaScript)
▫ JavaScript 코드가 작성되는 곳  
▫ 컴포넌트 정보, 데이터, 메서드 등 vue 인스턴스를 구성하는 대부분이 작성됨  

> 파일 자체가 컴포넌트 이므로, 원래 작성하던 코드와는 달라짐  

### 🔹 스타일 (CSS)
▫ CSS 가 작성되며 컴포넌트의 스타일 담당 

▫ 컴포넌트들이 tree 구조를 이루어 하나의 페이지를 만듦  
▫ root에 해당하는 최상단의 component가 App.vue  
▫ 이 App.vue를 index.html과 연결  
▫ 결국 index.html 파일 하나만을 rendering ➡ SPA  

<br><br>

## Vue component 실습  

### MyComponent.vue  
> 이름 규칙 : 대문자 + 카멜케이스 

<br>

1. src/components/ 안에 생성 
- vue 자동완성 (확장 프로그램)

<br>

2. script에 이름 등록
- 다른 파일이 불러갈 때 해당 이름을 이용  

<br>

3. template에 요소(최상위 태그) 추가 
- templates 안에는 반드시 하나의 요소만 추가 가능 (비어 있어도 안됨) ➡ 해당 요소 안에 추가 요소 작성  

<br><br>

### component 등록 3단계 ⭐⭐⭐
1. 불러오기
2. 등록하기
3. 보여주기 

<br>

1️⃣ 불러오기  

``` js
// 1. 불러오기
import MyComponent from './components/MyComponent.vue'
import MyComponent from '@/components/MyComponent'
```
▫ @ : src의 shortcut  
▫ .vue 생략 가능  

<br>

2️⃣ 등록하기  

``` js
export default {
  name: 'App',
  components: {
    HelloWorld,
    // 2. 등록하기
    MyComponent
  }
}
```
<br>


3️⃣ 보여주기

``` html
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <!-- 3. 보여주기 -->
    <MyComponent/>
    <HelloWorld msg="Welcome to Your Vue.js App"/>
  </div>
```
▫ 닫는 태그만 있는 요소처럼 사용  

<br>

![image](https://user-images.githubusercontent.com/93974908/199375530-e49bb3ee-0120-42e8-93e7-aef1709a9854.png)

<br><br>

### 자식 컴포넌트 작성  
``` html
<template>
  <div class="border">
    <h1>내가 만든 새로운 컴포넌트🤗</h1>
    <MyComponentItem/>
    <MyComponentItem/>
    <MyComponentItem/>
  </div>
</template>

<script>
// 1. 불러오기
import MyComponentItem from '@/components/MyComponentItem'

export default {
  name: 'MyComponent',
  components: {
    // 2. 등록하기
    MyComponentItem,
  }
}
</script>

<style>
  .border {
    border: solid;
    color: rgb(13, 172, 119);
  }
</style>
```

▫ 불러오고(import) 안 쓰면 error  
▫ 등록하고 안 쓰면 error  

![image](https://user-images.githubusercontent.com/93974908/199379271-af7e407d-e8c1-4450-9460-9f0a545e4b6a.png)

▫ 컴포넌트의 재사용성  

<br><br>


---

# Pass Props & Emit Events

## Data in component

▫ 동적 웹페이지 ➡ 웹페이지에서 다뤄야 할 데이터 등장  
▫ 한 페이지 내에서 같은 데이터를 공유해야 함, BUT 페이지들은 컴포넌트로 구분되어 있음  

<br>

❓ MyComponent에 정의된 data를 MyChild에서 사용하려면 ❓     
▫ MyChild에도 똑같은 data 정의 ➡ 동일한 데이터가 아님 ➡ ❌  
▫ 필요한 컴포넌트끼리 데이터를 주고 받음 ➡ 데이터 흐름 파악 어려움 / 개발 속도 저하 / 유지보수 어려움 ➡ ❌  

<br> 

▫ 컴포넌트는 부모-자식 관계를 가지고 있으므로, **부모-자식 관계만 데이터를 주고받게 함**  
- 데이터 흐름 파악 용이 
- 유지 보수 쉬움  

<br><br>

## pass props & emit event 
▫ 부모 => 자식으로의 데이터 흐름  
- pass **props** 방식 (데이터)

▫ 자식 => 부모로의 데이터 흐름  
- **emit** event 방식 (이벤트)

<br><br>

## Pass Props 

▫ 요소의 속성을 사용하여 데이터 전달   
▫ props는 부모 컴포넌트의 정보를 전달하기 위한 사용자 지정 특성   
▫ 자식 컴포넌트는 props 옵션을 사용하여 수신하는 props를 명시적으로 선언해야 함   

``` html
<!-- App.vue -->

<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <MyComponent/>
    <HelloWorld msg="Welcome to Your Vue.js App😎"/>
  </div>
</template>
```
``` html
<!-- HelloWorld.vue -->

<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
```

▫ App.vue의 <HelloWorld/> 요소에 msg="~"라는 property 설정  
▫ 하위 컴포넌트인 HelloWorld는 자신에게 부려된 msg property를 template에서 {{ msg }} 형태로 사용  

<br>

▫ pass props :  부모 => 자식  
▫ 정적인 데이터를 전달하는 경우 static props라고 명시하기도 함 
▫ `prop-data-name="value"` 형태로 데이터 전달  
> 이때 속성의 키 값은 **케밥** 케이스

> html -> JS  
> 케밥 -> 카멜  

▫ Prop 명시  
▫ 데이터를 받는 하위 컴포넌트에서도 props에 대해 명시적으로 작성해주어야 함  

``` html
<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  }
}
</script>
```
▫ 전달받은 props를 type과 함께 명시  
▫ 컴포넌트를 문서화할 뿐만 아니라, 잘못된 타입이 전달하는 경우 브라우저의 자바스크립트 콘솔에서 사용자에게 경고  

<br><br>

### 실습 

``` html
<!-- MyComponent.html -->

<template>
  <div class="border">
    <h1>내가 만든 새로운 컴포넌트🤗</h1>
    <MyComponentItem static-props="MyComponent에서 보낸 데이터➡"/>
  </div>
</template>
```
> 보낼 때는 케밥 케이스 사용

<br>

``` html
<!-- MyComponentItem.html -->

<template>
  <div>
    <h3>MyComponent의 자식 컴포넌트👶</h3>
    <p>{{ staticProps }}</p>
  </div>
</template>

<script>
export default {
  name: 'MyComponentItem',
  props: {
    staticProps: String,
  }
}
</script>
``` 
> 받을 때는 카멜 케이스

▫ 부모 템플릿(html)에서 kebab-case로 넘긴 변수를 자식의 스크립트(vue)에서 자동으로 camelCase로 변환하여 인식함  

<br>

![image](https://user-images.githubusercontent.com/93974908/199405763-c2f602f7-81de-4b29-9ed0-e8533314fea7.png)

<br><br>

### Dynamic props 
▫ 변수를 props로 전달할 수 있음  
▫ v-bind directive를 사용해 데이터를 **동적**으로 바인딩  
▫ 부모 컴포넌트의 데이터가 업데이트 되면 자식 컴포넌트로 전달되는 데이터 또한 업데이트 됨  



``` html
<!-- MyComponent.html -->

<template>
    <div class="border">
    <h1>내가 만든 새로운 컴포넌트🤗</h1>
    <MyComponentItem 
      static-props="MyComponent에서 보낸 데이터➡"
      :dynamic-props="dynamicProps"
    />
  </div>
</template>

<script>
    export default {
        ...
  data: function () {
      return {
          dynamicProps: '이건 동적인 데이터🤘',
    }
  }
}
</script>
```
▫ Vue CLI에서는 data가 함수의 return 객체여야 함 - 스코프 문제 때문에   
➡ 각 vue 인스턴스는 같은 data 객체를 공유하므로 새로운 data 객체를 반환하여 사용해야 함  


``` html
<!-- MyComponentItem.html -->

<template>
  <div>
    <h3>MyComponent의 자식 컴포넌트👶</h3>
    <p>{{ staticProps }}</p>
    <p>{{ dynamicProps }}</p>
  </div>
</template>

<script>
export default {
  name: 'MyComponentItem',
  props: {
    staticProps: String,
    dynamicProps: String,
  }
}
</script>
```

![image](https://user-images.githubusercontent.com/93974908/199408112-b0924067-db40-4223-af18-0550831f7e8d.png)


▫ `:dynamic-props="dynamicProps"`는 앞의 key 값이란 이름으로 뒤의 "" 안에 오는 데이터를 전달하겠다는 뜻  
▫ 즉, `:my-props="dynamicProps"`로 데이터를 넘긴다면, 자식 컴포넌트에서 myProps로 데이터를 받아야 함  
▫ v-bind로 묶여있는 "" 안의 구문은 javascript의 구문 ➡  dynamicProps 라고 하는 변수에 대한 data 전달 가능  

<br><br>

### 단방향 데이터 흐름  
▫ 모든 props는 부모에서 자식으로 (아래로) 단방향 바인딩 형성  
▫ 부모 속성이 업데이트되면 자식으로 흐르지만 반대 방향은 X  
(부모 컴포넌트가 업데이트 될 때마다 자식 컴포넌트의 모든 prop들이 최신 값으로 새로고침 됨)   

▫ 목적 : 하위 컴포넌트가 실수로 상위 컴포넌트 상태를 변경하여 앱의 데이터 흐름을 이해하기 힘들게 만드는 것 방지  
➡ 문제 발생하면 부모만 찾아가면 됨  

▫ 하위 컴포넌트에서 prop 변경 시도 ➡ Vue가 콘솔에서 경고 출력

> 아래에서 데이터를 올릴 때는 event를 통해서 간접적으로 소리침  

<br><br>

## Emit Event 
▫ 자식 => 부모 컴퍼넌트로 데이터 전달 시 이벤트를 발생시킴  
▫ 이벤트 발생 
1. 데이터를 이벤트 리스너의 콜백함수의 인자로 전달
2. 부모 컴포넌트는 해당 이벤트를 통해 데이터를 받음 

> 데이터를 직접적으로 올리는 것은 아님 (데이터 흐름은 단방향이니까)   
> 이벤트의 인자로 넣어서 올림  

<br>

### $emit
▫ $emit 메서드를 통해 부모 컴포넌트에 이벤트를 발생
- $emit('event-name') 형식으로 사용  
- 부모 컴포넌트에 event-name이라는 이벤트 발생시킴


``` html
<!-- MyComponentItem.html -->

<template>
  <div>
    ...
    <button @click="childToParent">클릭!</button>
  </div>
</template>

<script>
export default {
  ...
  methods: {
    childToParent: function () {
      this.$emit('child-to-parent', '자식이 보낸 데이터📧')
    }
  }
}
</script>
```
▫ 이벤트를 발생 (emit) 시킬 때 인자로 데이터 전달 가능  

> emit은 기본 속성값 -> $ 붙여줘야 함  

> 한 단계 위로만 가능 / 점프 불가


▫ Emit Event 흐름 
1. 자식 컴포넌트의 핸들러 함수 호출
2. 호출된 함수에서 $ emit을 통해 상위 컴포넌트에 이벤트 발생
3. 상위 컴포넌트는 이벤트를 청취하여 연결된 핸들러 함수 호출
4. 호출된 함수 실행  


``` html
<!-- MyComponent.html -->

<template>
  <div class="border">
    <h1>내가 만든 새로운 컴포넌트🤗</h1>
    <MyComponentItem 
      static-props="MyComponent에서 보낸 데이터➡"
      :dynamic-props="dynamicProps"
      @child-to-parent="parentGetEvent"
    />
  </div>
</template>

<script>
export default {
  ...
  methods: {
    parentGetEvent: function (childData) {
      console.log('Good👍')
      console.log(childData)
    }
  }
}
</script>
```
▫ 전달한 데이터는 이벤트와 연결된 핸들러 함수의 인자로 사용 가능  

![image](https://user-images.githubusercontent.com/93974908/199413865-fc177def-36a3-4374-b38b-15502af6339e.png)

<br>

▫ 동적 데이터도 전달 가능 
``` html
<!-- MyComponentItem.html -->

<template>
  <div>
    ...
    <input 
      type="text" 
      v-model="childInputData"
      @keyup.enter="childInput"
    >
  </div>
</template>

<script>
export default {
  ...
  data: function () {
    return {
      childInputData: null
    }
  },
  methods: {
    ...,
    childInput: function () {
      this.$emit('child-input', this.childInputData)
      this.childInputData = null
    }
  }
}
</script>
```
``` html
<!-- MyComponent.html -->

<template>
  <div class="border">
    <h1>내가 만든 새로운 컴포넌트🤗</h1>
    <MyComponentItem 
      ...
      @child-input="getDynamicData"
    />
  </div>
</template>

<script>
export default {
  ...,
  methods: {
    ...,
    getDynamicData: function (childInputData) {
      console.log(`입력값 : ${childInputData}`)
    }
  }
}
</script>
```


![image](https://user-images.githubusercontent.com/93974908/199419284-08137186-1f57-4d71-bdb5-fd6970a5377e.png)

<br>

> 🤗 자식 컴포넌트에서 부모 컴포넌트로 이벤트를 발생  
> ➡ 이벤트에 데이터를 담아 전달 가능 
> 
> 🤗 부모 컴포넌트에서는 이벤트를 청취  
> ➡ 전달받은 데이터는 이벤트 헨들러 함수의 인자로 사용 

<br>

> kebab - HTML   
> camel - JS  

**props**  
▫ 상위 => 하위 흐름에서 HTML 요소로 내려줌 : kebab-case  
▫ 하위에서 받을 때 JavaScript에서 받음 : camelCase  

**emit**   
▫ emit 이벤트를 발생시키면 HTML 요소가 이벤트를 청취함 : kebab-case  
▫ 메서드, 변수명 등은 JavaScript에서 사용함 : camelCase  





