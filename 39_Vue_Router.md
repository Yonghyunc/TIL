# TIL

[UX & UI](#ux--ui)

[Vue Router](#vue-router)

[Navigation Guard](#navigation-guard)

[Articles with Vue](#articles-with-vue)

<br><br>

---

# UX & UI

## UX (User Experience)
▫ 유저와 가장 가까이에 있는 분야  
▫ 데이터를 기반으로 유저를 조사하고 분석해서 개발자, 디자이너가 이해할 수 있게 소통  
▫ 유저가 느끼는 느낌, 태도, 행동을 디자인   
> 메뉴바를 사람들이 잘 안 쓰니까 크기를 줄이거나 위치를 바꾸자

<br>

▫ 좋은 UX를 설계하기 위해서는  
➡ 사람들의 마음과 생각을 이해하고 정리해서 우리 제품에 녹여내는 과정 필요  
➡ 유저 리서치, 데이터 설계 및 정제, 유저 시나리오, 프로토타입 설계 등이 필요  

<br><br>

## UI (User Interface)
▫ 유저에게 보여지는 화면 디자인  
▫ UX를 고려한 디자인 반영, 이 과정에서 기능 개선/추가가 필요한 경우 프론트엔드 개발자와 가장 많이 소통   
> 메뉴바의 위치는 구성 상 여기가 가장 좋겠어

<br>

> **Interface** 
> 
> ▫ 서로 다른 두 개의 시스템, 장치 사이에서 정보나 신호를 주고받는 경우의 접점   
> ▫ 즉, 사용자가 기기를 쉽게 동작 시키는데 도움을 주는 시스템   
> - CLI 
> - GUI 

<br>

▫ 좋은 UI를 설계하기 위해서는   
➡ 심미적인 부분만 중요한 것이 아니라 사용자가 보다 쉽고 편리하게 사용할 수 있도록 하여야 함  
➡ 통일된 디자인을 위한 디자인 시스템, 소통을 위한 중간 산출물, 프로토타입 등 필요  
➡ UI 디자인에 있어 가장 중요한 것은 협업  

<br><br>

## Prototyping  
### Software prototyping
▫ 애플리케이션의 프로토타입을 만드는 것  
▫ 개발 중인 소프트웨어 프로그램의 완성되기 전 버전을 만드는 것   
▫ 한 번에 완성 버전이 나올 수 없기에 중간마다 현재 상태 체크  

<br>
▫ UI/UX 디자인을 prototyping 하기 위한 도구는 굉장히 많고 경쟁이 심함  

<br>

### 🖱 Figma
▫ 인터페이스 디자인을 위한 협업 웹 애플리케이션   
▫ 협업에 중점을 두면서 UI/UX 설계에 초점을 맞춤  

- 웹 기반 시스템을 가짐 (웹 환경에서 동작) - 매우 가벼운 환경에서 실행 O 
- 실시간으로 팀원들이 협업할 수 있는 기능 제공 
- 직관적이고 다양한 디자인 툴 제공
- Figma 사용자들이 만든 다양한 플러그인 존재  
- 대부분의 기능 무료 사용 O

▫ 기존의 모든 불필요한 과정을 생략하고 디자인 그 자체에만 집중 할 수 있게 함  

<br><br>

---

# Vue Router
## Routing
▫ 네트워크에서 경로를 선택하는 프로세스  
▫ 웹 서비스에서의 라우팅 (유저가 방문한 URL에 대해 적절한 결과를 응답하는 것)

<br>

### Routing in SSR
▫ Server가 모든 라우팅을 통제
▫ URL로 요청이 들어오면 응답으로 완성된 HTML 제공    
▫ 결과적으로, Routiog(URL)에 대한 결정권을 서버가 가짐  

<br>

### Routing in SPA/CSR 
▫ 서버는 하나의 HTML 만을 제공  
▫ 이후 모든 동작은 하나의 HTML 문서 위에서 JS 활용  
▫ 즉, **하나의 URL**만 가질 수 있음

<br>

### Why Routing ?
▫ 동작에 따라 URL이 반드시 바뀌어야 하는가 ? 
➡ 꼭 그렇지는 않지만, 유저의 사용성 관점에서는 필요함  

▫ Routing이 없다면,
- 유저가 URL을 통한 페이지의 변화를 감지할 수 없음 
- 페이지가 무엇을 렌더링 중인지에 대한 상태를 알 수 없음
    - 새로고침 시 처음 페이지로 돌아감
    - 링크를 공유할 시 처음 페이지만 공유 가능
- 브라우저의 뒤로 가기 기능 사용 불가

<br><br>

## Vue Router
▫ Vue의 공식 라우터  
▫ SPA 상에서 라우팅을 쉽게 개발 O   
▫ 라우트에 컴토넌트를 매핑한 후, 어떤 URL에서 렌더링할지 알려줌  
➡ 즉, SPA를 MPA처럼 URL을 이동하면서 사용 가능  
> 하지만 실제로 페이지가 이동하는 것은 아니고, 보여지는 컴포넌트만 교체되는 것  
> 컴포넌트가 교체될 때마다 URL을 바꿔주는 것  

<br>

> MPA   
> ▫ 여러 개의 페이지로 구성된 애플리케이션  
> ▫ SSR 방식으로 렌더링   

<br><br>

### Vue Router 설치 및 반영  
``` 
$ vue add router
```
기존에 프로젝트를 진행하고 있던 도중에 router를 추가하게 되면 App.vue를 덮어쓰므로 필요한 경우 명령을 실행하기 전에 파일을 백업해두어야 함  

▫ history mode 사용여부 ➡ Yes

<br>

### 🔹 History mode
▫ 브라우저의 History API를 활용한 방식 - 새로고침 없이 URL 이동 기록을 남길 수 있음   
▫ 우리에게 익숙한 URL 구조로 사용 가능  

> History mode를 사용하지 않으면 hash mode로 설정됨  ('#'을 통해 URL을 구분하는 방식)

<br>

▫ App.vue 가 바뀜
``` vue
<template>
  <div id="app">
    <nav>
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </nav>
    <router-view/>
  </div>
</template>
``` 
<br>

▫ router, views 폴더가 생김   
![image](https://user-images.githubusercontent.com/93974908/200710441-759b01b5-0192-491e-913f-a6299effb77f.png)

<br>

▫ 페이지가 이동하는 것이 아니라 router-link가 바뀜  
![image](https://user-images.githubusercontent.com/93974908/200711379-ad93ca2e-aff9-45c3-8d50-a35cd2ec8ed7.png)

![image](https://user-images.githubusercontent.com/93974908/200711436-e0ae9dd0-8299-47db-9321-51695ac1b663.png)

<br>

### 🔹 router-link
▫ a 태그와 비슷한 기능 ➡ URL을 이동시킴  
▫ routes에 등록된 컴포넌트와 매핑됨  
▫ 히스토리 모드에서 router-link는 클릭 이벤트를 차단하여 a태그와 달리 브라우저가 페이지를 다시 로드하지 않도록 함   
▫ 목표 경로는 'to' 속성으로 지정됨  
▫ 기능에 맞게 HTML에서 a태그로 렌더링되지만, 필요에 따라 다른 태그로 바꿀 수 있음     

![image](https://user-images.githubusercontent.com/93974908/200711824-845d31f9-e0cf-42cc-ab45-d34dc86ab856.png)

<br>

### 🔹 router-view
▫ 주어진 URL에 대해 일치하는 컴포넌트를 렌더링 하는 컴포넌트  
▫ 실제 컴포넌트가 DOM에 부착되어 보이는 자리  
▫ router-link를 클릭하면 routes에 매핑된 컴포넌트를 렌더링  

▫ 장고의 block tag과 비슷 
- App.vue == base.html
- router-view는 block 태그로 감싼 부분

<br>

### 🔹 src/router/index.js
▫ 라우터에 관련된 정보 및 설정이 작성되는 곳  
▫ 장고의 urls.py에 해당  
▫ routes에 URL과 컴포넌트 매핑  

``` js
const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  }
]
```
<br>

### 🔹 src/Views
▫ router-view에 들어갈 컴포넌트 작성  
▫ 기존 컴포넌트를 작성하던 곳은 components 폴더 뿐이었지만 이제 두 폴더로 나뉨  
▫ 각 폴더 안의 .vue 파일들 기능적으로 다르지는 X  

▶ **views/**   
▫ routes에 매핑되는 컴포넌트   
▫ 다른 컴포넌트와 구분하기 위해 View로 끝나도록 만드는 것 권장 

▶ **components/**   
▫ routes에 매핑된 컴포넌트의 하위 컴포넌트  

<br><br>

## 실습

▫ 주소를 이동하는 2가지 방법  
1. 선언적 방식 네비게이션
2. 프로그래밍 방식 네비게이션 


<br><br>

### 1️⃣ 선언적 방식 네비게이션 
▫ router-link의 'to' 속성으로 주소 전달  

▫ routes에 등록된 주소와 매핑된 컴포넌트로 이동  


``` vue
<router-link to="/">Home</router-link> |
<router-link to="/about">About</router-link>
```

▫ Named Routes  : 이름을 가지는 routes   
``` vue
<router-link :to="{ name: 'home' }">Home</router-link> |
<router-link :to="{ name: 'about' }">About</router-link>
```
> 동적인 값을 사용하기 때문에 v-bind를 사용해야 정상적으로 작동  

<br><br>

### 2️⃣ 프로그래밍 방식 네비게이션  

▫ Vue 인스턴스 내부에서 라우터 인스턴스에 `$router`로 접근 O  

▫ 다른 URL로 이동하려면 `this.$router.push` 사용   
➡ history stack에 이동할 URL을 넣는 방식   
➡ history stack에 기록이 남기 때문에 뒤로가기 가능  

▫ `<router-link :to="...">` == `$router.push(...)`

``` vue
<!-- AboutView.vue -->

<template>
  <div class="about">
    <h1>This is an about page</h1>
    <button @click="toHome">홈으로</button>
  </div>
</template>

<script>
export default {
  name: 'AboutView',
  methods: {
    toHome() {
      this.$router.push({ name: 'home' })
    }
  }
}
</script>
```

``` vue
<router-link :to="{ name: 'home' }">Home</router-link>
``` 
⬆ 위의 두 가지는 기능이 같음

<br><br>

### Dynamic Route Matching
▫ 동적 인자 전달  (URL의 특정 값을 변수처럼 사용 O)    


▫ route를 추가할 때 동적 인자 명시   
> userName이라는 인자가 변수로 계속해서 바뀜  

``` js
import HelloView from '@/views/HelloView'

const routes = [
      {
    path: '/hello/:userName',
    name: 'hello',
    component: HelloView
  }
]
```


▫ `$route.params` 로 변수 접근 가능  

``` vue
<template>
  <div>
      <h1>hello, {{ $route.params.userName }}</h1>
  </div>
</template>
```

![image](https://user-images.githubusercontent.com/93974908/200715946-430d3586-4152-45a3-958b-0889f459a3c0.png)

▫ **BUT**, HTML 직접 사용보다는 data에 넣어서 사용하는 것 권장  
``` vue
<template>
  <div>
    <h1>hello, {{ userName }}</h1>
  </div>
</template>

<script>
export default {
  name: 'HelloView',
  data() {
    return {
      userName: this.$route.params.userName
    }
  }
}
</script>
```
<br><br>

### 1️⃣ Dynamic Route Matching - 선언적 방식 네비게이션 
▫ params 이용하여 동적 인자 전달 O  

``` vue
<router-link :to="{ name: 'hello', params: { userName: 'yong' }}">Hello</router-link>
```

![image](https://user-images.githubusercontent.com/93974908/200716576-59cd8cc6-fe6b-40fc-a89b-2c3834a7e6bd.png)

<br><br>

### 2️⃣ Dynamic Route Matching - 프로그래밍 방식 네비게이션 

▫ 입력받은 변수값으로 이동하기  
1. input 태그
2. data
3. 선언적으로 이동 X ➡ 프로그래밍적 이동  

``` vue
<template>
  <div class="about">
    ...
    <input 
      type="text"
      @keyup.enter="goToHello"
      v-model="inputData"
    >
  </div>
</template>

<script>
export default {
  name: 'AboutView',
  data() {
    return {
      inputData: null,
    }
  },
  methods: {
    ...,
    goToHello() {
      this.$router.push({ name: 'hello', params: { userName: this.inputData}})
    }
  }
}
</script>
```
<br><br>

### ✔ route에 컴포넌트를 등록하는 또 다른 방법 

``` js
const routes = [
  // 기존 방식 
  {
    path: '/',
    name: 'home',
    component: HomeView
  },

  // lazy-loading (첫 로딩에 렌더링 하지않고 해당 라우터가 동작할 때 컴포넌트를 렌더링 함)
  {
    path: '/about',
    name: 'about',
    component: () => import('../views/AboutView.vue')
  },
]
```
<br>

**lazy-loading**   

▫ 모든 파일을 한 번에 로드하려고 하면 모든 걸 다 읽는 시간이 매우 오래 걸림  
▫ 미리 로드를 하지 않고 특정 라우트에 방문할 때 매핑된 컴포넌트의 코드를 로드하는 방식 활용 O  
▫ 최초 로드 시간이 빨라짐  
▫ 당장 사용하지 않을 컴포넌트를 먼저 로드하지 않는 것이 핵심  


<br><br> 

---

# Navigation Guard
▫ Vue Router를 통해 특정 URL에 접근할 때 다른 URL로 redirect 하거나 해당 URL로의 접근을 막는 방법  

1️⃣ 전역 가드 ➡ 애플리케이션 전역에서 동작  

2️⃣ 라우터 가드 ➡ 특정 URL에서만 동작

3️⃣ 컴포넌트 가드 ➡ 라우터 컴포넌트 안에 정의 

<br><br>

## 1️⃣ 전역 가드 (Global Before Guard)
▫ 다른 URL로 이동할 때 항상 실행  

### router.beforeEach()
- to : 이동할 URL 정보가 담긴 route 객체
- from : 현재 URL 정보가 담긴 route 객체
- next : 지정한 URL로 이동하기 위해 호출하는 함수  
> 콜백 함수 내부에서 반드시 한 번만 호출되어야 함   
> 기본적으로 to에 해당하는 URL 로 이동 

<br>

▫ URL 이 변경되어 화면이 전환되기 전 router.beforeEach()가 호출됨 - 화면이 전환되지 않고 대기 상태  
▫ 변경된 URL로 라우팅하기 위해서는 next()를 호출해줘야 함  
> next()가 호출되기 전까지 화면 전환 X

<br>

▫ HelloView에 로그인을 해야만 접근할 수 있도록 만들어 보기  

``` js
router.beforeEach((to, from, next) => {
  // 로그인 여부
  const isLoggedIn = true

  // 로그인이 필요한 페이지 
  const authPages = ['hello']

  // 앞으로 이동할 페이지가 로그인이 필요한 페이지인지 확인 
  const isAuthRequired = authPages.includes(to.name)

  if (isAuthRequired && !isLoggedIn) {
    next({ name: 'login' })
  } else {
    next()
  }
```
▫ isAuthRequired 값에 따라 로그인이 필요한 페이지 + 로그인이 되어있지 않다면 ➡ Login 페이지 이동  
▫ 그렇지 않으면 ➡ 기존 루트로 이동  

▫ next() 인자가 없을 경우 to로 이동  

<br>

▫ 반대로 Login하지 않아도 되는 페이지들을 모아 둘 수도 있음  
``` js
const allowAllPages = ['login']
const isAuthRequired = !allowAllPages.includes(to.name)
```

<br><br>

## 2️⃣ 라우터 가드
▫ 전체 route가 아닌 특정 route에 대해서만 가드를 설정하고 싶을 때 사용  
> 다른 경로에서 특정 route로 탐색할 때만 실행됨  

### beforeEnter()
▫ route에 진입했을 때 실행됨  
▫ 라우터를 등록한 위치에 추가  
▫ 단 매개변수, 쿼리, 해시 값이 변경될 때는 실행되지 않고 다른 경로에서 탐색할 때만 실행됨  
- to
- from
- next

<br>

▫ 이미 로그인 되어있는 경우 HomeView로 이동하기

``` js
  {
    path: '/login',
    name: 'login',
    component: LoginView,
    beforeEnter(to, from, next) {
      if (isLoggedIn === true) {
        console.log('이미 로그인 되어있음')
        next({ name: 'home' })
      } else {
        next()
      }
    }
  }
```


<br><br>

## 3️⃣ 컴포넌트 가드 
▫ 특정 컴포넌트 내에서 가드를 지정하고 싶을 때 사용  

### beforeRouteUpdate()
▫ 해당 컴포넌트를 렌더링하는 **경로가 변경될 때** 실행  

▫ input으로 userName을 받고 나서 Hello를 다시 눌렀을 때, URL은 변하지만 페이지는 변화하지 않음  
![image](https://user-images.githubusercontent.com/93974908/200748868-2386627b-3398-4407-8114-ecadcec87c98.png)


▫ 변화하지 않는 이유  
➡ 컴포넌트가 재사용됨  
➡ 기존 컴포넌트를 지우고 새로 만드는 것보다 효율적  
- But, lifecycle hook이 호출되지 않음  
- 따라서 $route.params에 있는 데이터를 새로 가져오지 않음  

``` js
// HelloView.vue

export default {
  name: 'HelloView',
  data() {
    return {
      userName: this.$route.params.userName
    }
  },
  beforeRouteUpdate(to, from, next) {
    this.userName = to.params.userName
    next()
  }
}
```


<br><br>

## 404 Not Found
▫ 사용자가 요청한 리소스가 존재하지 않을 때 응답  
``` js
  {
    path: '/404',
    name: 'NotFound404',
    component: NotFound404
  },
```

### 1️⃣ 모든 경로에 대해 404로 redirect 
▫ 기존에 명시한 경로가 아닌 모든 경로가 404 page로 redirect  
▫ **routes 최하단부**에 작성해야 함  

주소 전체 * 로 표현  
``` js
  {
    path: '*',
    redirect: '/404'
  }
```

### 2️⃣ 형식은 유효하지만 특정 리소스를 찾을 수 없는 경우  
▫ 데이터가 존재하지 않기 때문에 정상적으로 렌더링 X   
➡ 데이터가 없음을 명시하고 404 page로 이동해야 함  

``` vue
<template>
  <div>
    <p v-if="!imgSrc">{{ message }}</p>
    <img :src="imgSrc" alt="">
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'DogView',
  data() {
    return {
      imgSrc: null,
      message: "로딩중..."
    }
  },
  methods: {
    getDogImage() {
      const breed = this.$route.params.breed
      const dogImageUrl = `https://dog.ceo/api/breed/${breed}/images/random`

      axios({
        method: 'get',
        url: dogImageUrl,
      })
        .then((response) => {
          console.log(response)
          const imgSrc = response.data.message
          this.imgSrc = imgSrc
        })
        .catch((error) => {
          this.message = `${this.$route.params.breed}은 없는 품종입니다.`
          console.log(error)
        })
    }
  },
  created() {
    this.getDogImage()
  }
}
</script>
```

![image](https://user-images.githubusercontent.com/93974908/200754624-44566e35-1351-4e89-9e2c-658a2346da61.png)

주소가 유효하지만 데이터가 없는 경우도 404로 보내줘야 함  


``` js
.catch((error) => {
    // this.message = `${this.$route.params.breed}은 없는 품종입니다.`
    this.$router.push('/404')
    console.log(error)
})
```
<br><br>

# Articles with Vue
