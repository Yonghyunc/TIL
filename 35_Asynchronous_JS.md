# TIL

[동기 / 비동기](#동기--비동기)

[Callback & Promise](#callback--promise)

[Axios](#axios)

[AJAX]


<br><br>


---
# 동기 / 비동기


##  동기 (Synchronous)
▫ 모든 일을 **순서대로** 하나씩 처리하는 것  
▫ 순서대로 처리 == 이전 작업이 끝나면 다음 작업을 시작   

▫ 요청과 응답을 동기식으로 처리한다면 ➡ 요청을 보내고 응답이 올 때까지 기다렸다가 다음 로직을 처리   

<br><br>

## 비동기 (Asynchronous)
> 순서가 없이 여러 가지를 동시에 처리하는 것 

▫ 작업을 시작한 후 결과를 기다리지 않고 다음 작업을 처리  (병렬적 수행)   
▫ 시간이 필요한 작업들은 요청을 보낸 뒤 응답이 빨리 오는 작업부터 처리   
ex) 메일 전송 후 답장을 기다리지 않고 다른 작업 수행  

<br>

### 비동기를 사용하는 이유
**사용자 경험**  

▫ 동기식 처리는 특정 로직이 실행되는 동안 다른 로직 실행을 차단하기 때문에 마치 프로그램이 응답하지 않는 듯한 사용자 경험을 만들게 됨   
> 웹 페이지는 각각의 url(각 요소)을 받아 요청을 처리함  
> 웹 페이지 로딩 시 오래 걸리는 정보가 있다면, 해당 정보가 로딩될 때까지 그 다음 정보 또한 출력되지 않음

▫ 비동기로 처리한다면 먼저 처리하는 부분부터 보여줄 수 있으므로, 사용자 경험에 긍정적인 효과 O  


<br><br>

## JS의 비동기 처리 

▫ JS는 한 번에 하나의 일만 수행할 수 있는 Single Thread 언어  
➡ 즉, JS는 하나의 작업을 요청한 순서대로 처리할 수 밖에 없다 ! 그렇다면 HOW❓   
> 자바스크립트의 동시성 

> ▫ 동시성 : 하나가 여러 개를 동시에 처리하는 것처럼 보임  
> ▫ 병렬성 : 여러 개가 실제로 동시에 여러가지 일을 처리

<br>

### JavaScript Runtime 
▫ 런타임 : 특정 언어가 동작할 수 있는 환경   
▫ JS에서 비동기와 관련한 작업은 브라우저 또는 Node 환경에서 처리 

> ▫ V8 (JS 엔진) ➡ 힙, 콜 스택    
> ▫ Chrome (브라우저) ➡ Web API, 테스크 큐  

1. JavaScript Engine의 Call Stack  
   - 요청이 들어올 때마다 순차적으로 처리하는 스택
   - 기본적인 JS의 Single Thread 작업 처리
[01_callstack.js](js/Asynchronous/01_callstack.js)

2. Web API  
   - 브라우저에서 제공하는 런타임 환경
   - 시간이 소요되는 작업 처리


3. Task Queue  
   - 비동기 처리된 콜백함수가 대기하는 큐


4. Event Loop  
   - Call Stack과 Task Queue를 지속적으로 모니터링 
   - Call Stack이 비어 있는지 확인 후 비어있다면 Task Queue에서 대기 중인 오래된 작업을 Call Stack으로 Push

<br>

### 비동기 처리 동작 방식
[02_sync_async.js](js/Asynchronous/02_sync_async.js)
1️⃣ 모든 작업은 **Call Stack**(LIFO)으로 들어간 후 처리됨 
> 함수가 호출될 때마다 콜스택에 쌓이는데, 이것을 컨텍스트가 실행되었다고 함 

2️⃣ 오래 걸리는 작업이 **Call Stack**으로 들어오면 **Web API**로 보내서 처리하도록 함  

3️⃣ Web API에서 처리가 끝난 작업들은 **Task Queue**(FIFO)에 순서대로 들어감 

4️⃣ **Event Loop**가 **Call Stack**이 비어 있는 것을 체크하고, **Task Queue**에서 가장 오래된 작업을 **Call Stack**으로 보냄  

[03_setTimeout.js](js/Asynchronous/03_setTimeout.js)
> 지연이 3초여도 call stack에서 처리해야 할 양이 많으면 더 지연됨 

> 3초 지연은 3초 후에 queue에 들어간다는 뜻 - stack의 모든 일이 끝날 때까지 대기해야 함  


<br><br>

---
# Callback & Promise

비동기 처리는 작업이 완료되는 순서에 따라 처리!! ➡ 실행 결과를 예상하면서 코드 작성 X  

<br>

## 콜백 함수 
▫ 다른 함수의 인자로 전달되는 함수  
▫ 동기, 비동기 상관없이 사용 가능  
▫ **비동기 콜백** : 비동기 작업이 완료된 후 실행할 작업을 명시하는 데 사용되는 콜백 함수

### 콜백 함수를 사용하는 이유
▫ 명시적인 호출이 아닌 특정한 조건 혹은 행동에 의해 호출되도록 작성 O  
> "요청이 들어오면", "이벤트가 발생하면", "데이터를 받아오면" 등  

▫ **비동기 처리를 순차적으로 동작할 수 있게 함**  

### 콜백 지옥
[06_callback_hell.html](js/Asynchronous/06_callback_hell.html)
▫ 콜백 함수는 연쇄적으로 발생하는 비동기 작업을 순차적으로 동작할 수 있게 함  
▫ 비슷한 패턴 발생  
▫ 콜백 지옥 == 비동기 처리를 위해 콜백을 작성할 때 마주하는 문제   
== 파멸의 피라미드

▫ 코드 가독성 떨어짐  
▫ 유지 보수 어려워짐  

<br><br>


> response가 오기 전에 전역 컨텍스트 실행  ➡ undefined
>
> 순서 보장을 위해 콜백을 계속 넣을 수 밖에 없음 ➡ 콜백 지옥


## Promise
[07_promise.html](js/Asynchronous/07_promise.html)
▫ 콜백 지옥 문제를 해결하기 위해 등장한 비동기 처리를 위한 객체   
▫ "작업이 끝나면 실행 시켜줄게"   
▫ 비동기 작업의 완료 또는 실패를 나타내는 객체   

▫ 성공에 대한 약속 **then()**   
- 요청한 작업이 성공하면 콜백 실행
- 콜백은 이전 작업의 성공 결과를 인자로 전달 받음 

▫ 실패에 대한 약속 **catch()**  
- then()이 하나라도 실패하면 콜백 실행
- 콜백은 이전 작업의 실패 객체를 인자로 전달 받음 

<br><br>

---
# Axios
▫ 비동기로 데이터 통신을 가능하게 하는 라이브러리  
▫ Django REST API로 요청을 보내서 데이터를 받아온 후 처리할 때 사용   
▫ **axios로 처리한 비동기 로직이 항상 promise 객체를 반환**  
➡ then을 계속 이어 나가면서 작성 O  


> cdn 꼭 사용!

``` js
<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
<script>
  axios.get('요청할 URL')
    .then(성공하면 수행할 콜백함수)
    .catch(실패하면 수행할 콜백함수)
</script>
```
▫ then : 성공하면 수행할 로직 작성  
▫ catch : 실패하면 수행할 로직 작성 

[08_axios.html](js/Asynchronous/08_axios.html)

> axios -> vue.js -> Django

> ? WHY 비동기 ? 
> 
> axios는 요청 하나 (동기)   
> axios가 여러개가 있으면 동시다발적으로 요청을 보냄 => cat & dog 

[09_cat_dog.html](js/Asynchronous/09_cat_dog.html)

<br><br>

---

# AJAX
> 프로그래밍의 방법론 

▫ **비동기** 통신 웹 개발 기술  

▫ 특징
1. 페이지 **새로고침 없이** 서버에 요청
2. 서버로부터 응답(데이터)를 받아 작업 수행



base.html에 cdn, block

<int:user_pk>는 장고 문법 -> JS에서는 어떻게 쓸까?
[js dataset](https://developer.mozilla.org/ko/docs/Learn/HTML/Howto/Use_data_attributes)

csrf_token은 어떻게 사용? -> [공식문서](https://docs.djangoproject.com/en/4.1/howto/csrf/) 참고

[name=csrfmiddlewaretoken] 는 CSS 문법


data-user-id="{{ person.pk }}"  
event.target.dataset.userId


data-user-pk="{{ person.pk }}"  
event.target.dataset.userPk


data-user-pk-number="{{ person.pk }}"  
event.target.dataset.userPkNumber


then

views 함수에서 json 반환하도록 변경

json
1. boolean (팔로우, 언팔로우 여부)
2. 숫자 (팔로워 결과값)


from django.http import JsonResponse