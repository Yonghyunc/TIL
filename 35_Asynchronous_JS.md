# TIL

[동기 / 비동기](#동기--비동기)

[Axios](#axios)

[Callback & Promise](#callback--promise)

<br><br>

---
# 동기 / 비동기

##  동기 (Synchronous)
▫ 모든 일을 순서대로 하나씩 처리하는 것  
▫ 순서대로 처리 == 이전 작업이 끝나면 다음 작업을 시작   

▫ 요청과 응답을 동기식으로 처리한다면 ➡ 요청을 보내고 응답이 올 때까지 기다렸다가 다음 로직을 처리   

<br><br>

## 비동기 (Asynchronous)
▫ 작업을 시작한 후 결과를 기다리지 않고 다음 작업을 처리  (병렬적 수행)   
▫ 시간이 필요한 작업들은 요청을 보낸 뒤 응답이 빨리 오는 작업부터 처리   
ex) 메일 전송 후 답장을 기다리지 않고 다른 작업 수행  

<br>

### 비동기를 사용하는 이유
**사용자 경험**  

▫ 동기식 처리는 특정 로직이 실행되는 동안 다른 로직 실행을 차단하기 때문에 마치 프로그램이 응답하지 않는 듯한 사용자 경험을 만들게 됨   

▫ 비동기로 처리한다면 먼저 처리하는 부분부터 보여줄 수 있으므로, 사용자 경험에 긍정적인 효과 O  

<br><br>

## JS의 비동기 처리 

▫ JS는 한 번에 하나의 일만 수행할 수 있는 Single Thread 언어  
➡ 즉, JS는 하나의 작업을 요청한 순서대로 처리할 수 밖에 없다 ! 그렇다면 HOW❓   


### JavaScript Runtime 
▫ 런타임 : 특정 언어가 동작할 수 있는 환경   
▫ JS에서 비동기와 관련한 작업은 브라우저 또는 Node 환경에서 처리 

1. JavaScript Engine의 Call Stack  
   - 요청이 들어올 때마다 순차적으로 처리하는 스택
   - 기본적인 JS의 Single Thread 작업 처리
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
1️⃣ 모든 작업은 **Call Stack**(LIFO)으로 들어간 후 처리됨 

2️⃣ 오래 걸리는 작업이 **Call Stack**으로 들어오면 **Web API**로 보내서 처리하도록 함  

3️⃣ Web API에서 처리가 끝난 작업들은 **Task Queue**(FIFO)에 순서대로 들어감 

4️⃣ **Event Loop**가 **Call Stack**이 비어 있는 것을 체크하고, **Task Queue**에서 가장 오래된 작업을 **Call Stack**으로 보냄  


> 지연이 3초여도 call stack에서 처리해야 할 양이 많으면 더 지연됨 

> 3초 지연은 3초 후에 queue에 들어간다는 뜻 - stack의 모든 일이 끝날 때까지 대기해야 함  


<br><br>

---

# Axios
▫ 비동기로 데이터 통신을 가능하게 하는 라이브러리  
▫ Django REST API로 요청을 보내서 데이터를 받아온 후 처리할 때 사용 

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


> axios -> vue.js -> Django



<br><br>

---

# Callback & Promise

비동기 처리는 작업이 완료되는 순서에 따라 처리!! ➡ 실행 결과를 예상하면서 코드 작성 X  

