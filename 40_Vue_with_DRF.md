# TIL

[Vue with DRF]

[CORS]



<br><br>

---

# Vue with DRF

## Server & Client
### 서버 - DRF
▫ 클라이언트에게 **정보**와 **서비스**를 제공하는 컴퓨터 시스템  
▫ DB와 통신하며 데이터 생성, 조회, 수정 삭제  
▫ 요청을 보낸 Client에게 정상적인 요청이었다면 처리한 결과 응답  

▫ 서비스 전체를 제공 (Django Web Service)  
- Django를 통해 전달받은 HTML에는 하나의 웹 페이지를 구성할 수 있는 모든 데이터 포함 O
- 즉, 서버에서 모든 내용을 렌더링하여 하나의 HTML 파일로 제공
- 정보를 포함한 Web 서비스를 구성하는 모든 내용을 서버 측에서 제공 

▫ 정보를 제공 (DRF API Service)   
- Django를 통해 관리하는 정보만을 클라이언트에게 제공
- DRF를 사용하여 JSON으로 변환

<br>

### 클라이언트 - vue
▫ **서버가 제공하는 서비스에 적절한 요청**을 통해 **서버로부터 반환 받은 응답을 사용자에게 표현**하는 기능을 가진 프로그램 / 시스템  

▫ 서버가 제공하는 서비스에 적절한 요청
- 서버가 정의한 방식대로 요청 인자를 넘겨 요청
- 서버는 정상적인 요청에 적합한 응답 제공

▫ 서버로부터 반환 받은 응답을 사용자에게 표현  
- 사용자의 요청에 적합한 data를 서버에 요청하여 응답 받은 결과로 적절한 화면 구성  

<br><br>


## Vue with DRF

1️⃣ AJAX 요청   

> 비동기 - actions

``` 
npm install axios
```

``` js
// store/index.js

import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default new Vuex.Store({
  actions: {
    getArticles(context) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/articles/`
      })
        .then((response) => {
          console.log(response, context)
        })
        .catch((error) => {
          console.log(error)
        })
    }
  },
})
```

``` js
// ArticleView.vue

export default {
  name: 'ArticleView',
  components: {
    ArticleList,
  },
  computed:{
  },
  created() {
    this.getArticles()
  },
  methods: {
    getArticles() {
      this.$store.dispatch('getArticles')
    }
  }
}
```

> 서버는 정상적으로 200 반환   
> but, 클라이언트는 에러

![image](https://user-images.githubusercontent.com/93974908/201560262-0cc3ffe3-fe44-4c12-816d-2a8d938db4ee.png)

> CORS Policy에 의해 blocked 됨

<br><br>

# CORS
Cross-Origin Resource Sharing

▫ 브라우저가 요청을 보내고 서버의 응답이 브라우저에 도착   
- 서버의 로그는 200 반환 ➡ 서버는 정상적 / 브라우저가 막은 것  


▫ 보안상의 이유로 브라우저는 **동일 출처 정책 (SOP)**에 의해 다른 출처의 리소스와 상호작용 하는 것을 제한 함   
> 크롬 =/= vue


## SOP (Same - Origin Policy)
▫ "동일 출처 정책"   

▫ 불러온 문서나 스크립트가 다른 출처에서 가져온 리소스와 상호작용 하는 것을 제한하는 보안방식    
▫ 잠재적으로 해로울 수 있는 문서를 분리함으로써 공격받을 수 있는 경로를 줄임   

### Origin - 출처
▫ URL의 protocol + host + port  
▫ 세 영역이 모두 동일해야만 same origin   
![image](https://user-images.githubusercontent.com/93974908/201560794-c1a1a57c-1d4a-470e-81c4-1aeecf860370.png)

> 장고 8000 =/= vue 8080

## CORS
▫ 추가 **HTTP Header**를 사용하여, 특정 출처에서 실행 중인 웹 어플리케이션이 **다른 출처의 자원에 접근할 수 있는 권한**을 부여하도록 브라우저에 알려주는 체제   
➡ 어떤 출처에서 자신의 컨텐츠를 불러갈 수 있는지 서버에 지정할 수 있는 방법   

▫ 리소스가 자신의 출처와 다를 때, 교차 출처 HTTP 요청 실행   
➡ 만약 다른 출처의 리소스를 가져오기 위해서는 이를 제공하는 서버가 브라우저에게 다른 출처지만 접근해도 된다는 사실을 알려야 함  

### "교차 출처 리소스 공유 정책"  

▫ CORS policy에 위배되는 경우 브라우저에서 해당 응답 결과 사용 X   
➡ 서버에서 응답을 주더라도 브라우저에서 거절  

▫ 다른 출처의 리소스를 불러오려면 그 출처에서 **올바른 CORS header**를 포함한 응답을 반환해야 함  
> 교차 출처에 대한 응답 : 응답 + 헤더  -> 브라우저  

### CORS 세팅  

▫ HTTP Response Header로 통제 가능  

▫ Access-Control-Allow-Origin   
: 단일 출처를 지정하여 브라우저가 해당 출처가 리소스에 접근하도록 허용  

> Vue --------- 요청 ---------> DRF    
> Vue <--- 응답 + CORS 헤더 --- DRF    


▫ django-cors-headers 라이브러리 사용  
> 응답에 CORS 헤더를 알아서 추가해줌  

[django-cors-headers 깃허브](https://github.com/adamchainz/django-cors-headers)


``` 
pip install django-cors-headers
```
1️⃣ settings.py에 앱 추가    

2️⃣ MIDDLEWARE   
> CorsMiddleware는 가능한  ommonMiddleware 보다 먼저 정의 되어야 함

3️⃣ CORS_ALLOWED_ORIGINS에 교차 출처 자우너 공유를 허용할 Domain 등록    

``` python
INSTALLED_APPS = [
    ...
    # CORS policy
    "corsheaders",
    ...
]

MIDDLEWARE = [
    ...
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    ...
]

CORS_ALLOWED_ORIGINS = [
    'http://localhost:8080',
]


```

> 모든 Origin을 허용하고자 한다면   
> `CORS_ALLOWED_ORIGINS = True`

<br><br>

---

## Authentication & Authorization

### Authentication - 인증, 입증
▫ 자신이라고 주장하는 사용자가 누구인지 확인하는 행위  
▫ 모든 보안 프로세스의 첫 번째 단계   
▫ 즉, 내가 누구인지 확인하는 과정   
▫ 401 Unauthorized (비인증)   

### Authorization - 권한 부여, 허가
▫ 사용자에게 특정 리소스 또는 기능에 대한 엑세스 권한을 부여하는 과정 (절차)   
▫ 보안 환경에서 권한 부여는 항상 인증이 먼저 필요함  
▫ 서류의 등급, 웹 페이지에서 글 조회 / 삭제/ 수정할 수 있는 방법, 제한 구역 ➡ 인증이 되었어도 모든 권한을 부여 받는 것은 아님   
▫ 403 Forbidden (서버는 클라이언트가 누군지 알고 있음)    

### Authentication & Authorization
▫ 회원가입 후, 로그인 시 서비스를 이용할 수 있는 권한 생   
▫ 단, 모든 인증을 거쳐도 권한이 동일하게 부여되는 것은 아님   
▫ 세션, 토큰, 제 3자를 활용하는 등의 다양한 인증 방식 존재   


### 인증 여부 확인 방법
▫ TokenAuthentication  (DRF가 기본으로 제공해주는 인증 방식 중 하나)   
- 매우 간단하게 구현 O
- 기본적인 보안 기능 제공
- 다양한 외부 패키지 O


> view 함수마다 (각 요청마다) 다른 인증 방식을 설정하고자 한다면 decorator 활용  

``` python
INSTALLED_APPS = [
    ...
    # Auth
    'rest_framework.authtoken',
    ...
]

```


## dj-rest-auth

1️⃣ 패키지 설치   
``` 
pip install dj-rest-auth
```

2️⃣ App 등록   
``` python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework.authtoken',
    'dj_rest_auth',
    ...
]
```

3️⃣ url 등록   
``` python 
urlpatterns = [
    ...,
    path('accounts/', include('dj_rest_auth.urls')),
]
```

![image](https://user-images.githubusercontent.com/93974908/201589290-5cae48f0-58ed-4a98-99f1-cddd9b80a031.png)

> 회원가입이 없음   
> 이미 인증이 된 유저들이 갈 수 있는 곳만 있음   

> 회원가입은 토큰을 만드는 곳 -> 따로 해야할 일이 있음


### Registration (회원가입)
[공식문서](https://dj-rest-auth.readthedocs.io/en/latest/installation.html#registration-optional)

``` 
pip install 'dj-rest-auth[with_social]'
```

``` python
INSTALLED_APPS = [
    ...
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth.registration',
    ...
]

SITE_ID = 1
```

``` python
urlpatterns = [
    ...,
    path('accounts/signup/', include('dj_rest_auth.registration.urls'))
]
```

