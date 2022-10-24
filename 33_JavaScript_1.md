# TIL 
[JavaScript 시작](#javascript-시작)

[기초 문법](#javascript-기초-문법)

[함수](#함수)

[Array & Object](#array--object)

<br></br>

---


# JavaScript 시작
### ❓ JavaScript를 배워야 하는 이유 
▫ Web 기술의 기반이 되는 언어
- HTML 문서의 콘텐츠를 **동적**으로 변경할 수 있는 언어


▫ 다양한 분야로 확장이 가능한 언어
- 단순히 Web 조작을 넘어서 서버 프로그래밍, 모바일 서비스, 컴퓨터 응용프로그램 등 다양한 분야에서 활용 가능

▫ 2022년 현재, 가장 인기있는 언어

<br>

### 🔹 JavaScript 역사
▫ Web Browser와 깊은 연관 관계   
<br>

▶ 웹 브라우저의 역할   
▫ URL을 통해 Web 탐색  
▫ HTML / CSS / JavaScript를 이해한 뒤 해석해서 사용자에게 하나의 화면으로 보여줌  
▫ 클라이언트 역할  
즉, 웹 페이지 코드를 이해하고, 보여주는 역할

<br>

▶ 웹 브라우저와 스크립트 언어  
▫ 1993, Mosaic Web Browser  
▫ 1994, Netscape Navigator  
> Mocha -> LiveScript -> JavaScript   

▫ 1995, Internet Explorer  
▫ 1996-2000, ECMA 표준 발의  
▫ 2001-2004, 다양한 웹 브라우저 등장  
▫ jQeury 등의 라이브러리 등장  
▫ 2008, Google의 Chrome 등장과 대통합의 시대 
- 2015, ECMAScript6 (ES6) 표준안 제정



<br><br>

## JavaScript 실행환경 구성  
### 1. Web Browser로 실행 
▫ 웹 브라우저에는 JavaScript를 해석할 수 있는 엔진 O  
▫ HTML 파일에 직접 JavaScript를 작성 후 웹 브라우저로 파일 열기 

> open in browser - 단축 키 : ali + b

자바스크립트는 console 에 작성

![image](https://user-images.githubusercontent.com/93974908/196570566-cf35820f-318f-4e98-bf00-7855001dbb11.png)

1️⃣ html에 직접 작성  

2️⃣ js에 작성 후 html에 불러오기  

3️⃣ console에서 바로 작성  
> Node.js

▫ **Vanilla JavaScript** : 웹 브라우저에서 바로 실행할 수 있는 JavaScript 문법들  

<br>

### 2. Node.js로 실행  


<br></br>

---


# JavaScript 기초 문법

## 코드 작성법 
<br>

### 🔸 세미콜론 (;)  
▫ 선택 사항  
▫ 세미콜론이 없으면 ASI에 의해 자동으로 삽입됨  
> ASI : 자동 세미콜론 삽입 규칙 

<br>

### 🔸 들여쓰기 / 코드 블럭
▫ 2칸 들여쓰기 (필수 X, 디자인 가이드)   
▫ 블럭 = 중괄호 { } 내부
- 파이썬은 들여쓰기를 이용하여 코드 블럭 구분
- 자바스크립트는 중괄호 {}를 사용해 코드 블럭 구분

<br>

### 🔸 코드 스타일 가이드
▫ 종류가 다양함  
▫ 코딩 스타일의 핵심은 합의된 원칙과 일관성  
- Airbnb Style Guide 참고

<br>

### 🔸 주석
▫ 한 줄 주석 : //   
▫ 여러 줄 주석 : /* */

<br><br>

## 변수 & 식별자

### 🔹 식별자
▫ 변수를 구분할 수 있는 변수명  
▫ 반드시 문자, 달러($), 밑줄(_)로 시작  
▫ 대소문자 구분  
▫ 클래스명 외에는 모두 소문자로 시작  
▫ 예약어 사용 X (for, if, function 등)

<br>

▫ 카멜 케이스 (camelCase)
- 변수, 객체, 함수에 사용
``` js
// 변수
let dog
let variableName

// 객체
const userInfo = { name: 'Tom', age: 20 }

// 함수
function add() {}
function getName() {}
```

▫ 파스칼 케이스 (PascalCase)
- 클래스, 생성자에 사용
``` js
// 클래스
class User {
  constructor(options) {
    this.name = options.name
  }
}

// 생성자 함수
function User(options) {
  this.name = options.name
}
```

▫ 대문자 스네이크 케이스(SNAKE_CASE)
- 상수에 사용 
> 상수 : 개발자의 의도와 상관없이 변경될 가능성이 없는 값
``` js
// 값이 바뀌지 않을 상수
const API_KEY = 'my-key'
const PI = Math.PI

// 재할당이 일어나지 않는 변수
const NUMBERS = [1, 2, 3]
```



<br>

### 🔹 변수 선언 키워드
▫ let  
- 블록 스코프 지역 변수 선언 (동시에 값을 초기화)

▫ const
- 블록 스코프 읽기 전용 상수 선언 (동시에 값을 초기화)

▫ var
- 변수 선언 (동시에 값을 초기화)

> **선언** (Declaration)  
> ▫ 변수를 생성하는 행위 또는 시점
> 
> **할당** (Assignment)   
> ▫ 선언된 변수에 값을 저장하는 행위 또는 시점
> 
> **초기화** (Initialization)  
> ▫ 선언된 변수에 처음으로 값을 저장하는 행위 또는 시점

> 📌 블록 스코프  
> = 이름공간  
> 
> ▫ if, for, 함수 등의 중괄호 내부  
> ▫ 블록 스코프를 가지는 변수는 블록 바깥에서 접근 불가능
> ``` js
> let x = 1
> if (x === 1) {
>   let x = 2
>   console.log(x)    // 2
> }
> console.log(x)      // 1
> ```




<br>

1️⃣ let  
▫ 재할당 가능 & 재선언 불가능  
▫ 블록 스코프를 갖는 지역 변수 선언  
▫ 선언과 동시에 원하는 값으로 초기화 가능  
``` js
let number = 10   // 1. 선언 및 초기값 할당
number = 20       // 2. 재할당 ⭕

let number = 10   // 1. 선언 및 초기값 할당
let number = 20   // 2. 재선언 ❌
```
<br>


2️⃣ const  
> 상수 선언  

▫ 재할당 불가능 & 재선언 불가능    
▫ 선언 시 반드시 초기값 설정 해야 하며, 이후 값 변경 불가  
▫ let과 동일하게 블록 스코프를 가짐  
``` js
const number = 10   // 1. 선언 및 초기값 할당
number = 20       // 2. 재할당 ❌

const number = 10   // 1. 선언 및 초기값 할당
const number = 20   // 2. 재선언 ❌
```
<br>


3️⃣ var  
> 에어비앤비 스타일 가이드에서 쓰지 말라 함

▫ 재할당 가능 & 재선언 가능  
▫ ES6 이전 사용  
▫ "**호이스팅**" 되는 특성으로 인해 발생하는 문제 多  
➡ const, let 사용 권장  

▫ 함수 스코프를 가짐  
 

> 📌 함수 스코프
> 
> ▫ 함수 중괄호 내부  
> ▫ 함수 스코프를 가지는 변수는 함수 바깥에서 접근 불가
> ``` js
> function foo() {
>   var x = 5
>   console.log(x)    // 5
> }
> 
> // ReferenceError: x is not defined
> console.log(x)
> ```

⭐ **호이스팅**  

▫ 변수를 선언 이전에 참조할 수 있는 현상  
▫ 변수 선언 이전의 위치에서 접근 시, undefined 반환   
```js
console.log(name)     // undefined -> 선언 이전 참조

var name = '홍길동'   // 선언
```
``` js 
// 위 코드를 암묵적으로 아래와 같이 이해함
var name              // undefined 로 초기화
console.log(name)

var name = '홍길동'
```

▫ 즉, JavaScript에서 변수들은 실제 실행 시에 코드의 최상단으로 끌어 올려지게 되며 (hoisted) 이러한 이유때문에 var로 선언된 변수는 선언 시에 undefined로 값이 초기화되는 과정이 동시에 일어남 

▫ let, const 는 호이스팅이 일어나면 에러를 발생시킴


> 에어비앤비 스타일 가이드에서는 기본적으로 const 사용 권장  
재할당해야 하는 경우만 let  

<br></br>

## 데이터 타입
![image](https://user-images.githubusercontent.com/93974908/196595201-0b6ed5b3-a737-425d-9b4b-bf5b5fe17fe8.png)

<br>

### 원시 타입 
1️⃣ Number  
▫ 정수 / 실수  
``` js
const a = 13
const b = -5
const c = 3.14
const d = 2.998e8
const e = Infinity
const f = -Infinity
const g = NaN
```

▫ **NaN** : Not-A-Number (숫자가 아님)
- Number.isNaN()의 경우 주어진 값의 유형이 Number이고 값이 NaN이면 True, 아니면 False 반환  

▫ NaN을 반환하는 경우 
1. 숫자로서 읽을 수 없음 
2. 결과가 허수인 수학 계산식
3. 피연산자가 NaN
4. 정의할 수 없는 계산식 
5. 문자열을 포함하면서 덧셈이 아닌 계산식 

<br>

2️⃣ String   
▫ 문자열  
▫ 작은 따옴표 / 큰 따옴표 O  
▫ 곱셈, 나눗셈, 뺄셈 X  
▫ 덧셈 O - 문자열 붙일 수 있음  

▫ Quote를 사용하면 선언 시 줄바꿈 X  
▫ 대신 escape sequence 사용 (\n)  

▫ **Template Literal**
- 줄 바꿈 O
- 문자열 사이 변수 삽입 O - $ + 중괄호
  > 파이썬의 f-string
- 백틱(`)

``` js
const word = `안녕
들 하세요`
console.log(word)

const age = 10
const message = `홍길동은 ${age}세입니다`
console.log(message)
```

<br>

3️⃣ Empty Value  
▫ 값이 존재하지 않음  
▫ **null**
- 변수에 값이 없음을 의도적으로 표현  

``` js
let lastName = null
console.log(lastName)   // null - 의도적으로 값이 없음 표현
```

▫ **undifined**
- 값이 정의되어 있지 않음을 표현
- 변수 선언 이후 직접 값을 할당하지 않으면 자동으로 할당됨

``` js
let firstName     // 선언만 하고 할당 X
console.log(firstName)    // undefined
```

▫ typeof 연산자를 통해 타입 확인  
``` js
typeof null           // "object"
typeof undefined      // "undefined"
```

> null이 원시 타입임에도 불구하고 object로 출력되는 이유는 JavaScript 설계 당시의 버그를 지금까지 해결하지 못한 것 

<br>

4️⃣ Boolean  
▫ true / false  
▫ 조건문, 반복문에서 유용  
- 조건문, 반복문에서 boolean이 아닌 데이터 타입은 자동 형변환 규칙에 따라 true 또는 false로 변환됨  

> 자동 형변환    
> ![image](https://user-images.githubusercontent.com/93974908/196596238-ad39eab8-0365-49fa-af31-96bd96611167.png)


<br></br>

## 연산자

### 할당 연산자
▫ 오른쪽에 있는 피연산자의 평가 결과를 왼쪽 피연산자에 할당하는 연산자  
▫ 다양한 연산에 대한 단축 연산자 지원  

▫ Increment(++) : 피연산자 값 + 1  
▫ Decrement(--) : 피연산자 값 - 1  

> +=, -= 과 같은 더 분명한 표현 사용 권장  

<br>

### 비교 연산자  
▫ 피연산자들을 비교하고 결과값을 boolean으로 반환  
▫ 문자열은 유니코드 값을 사용하며 표준 사전 순서를 기반으로 비교

<br>

### 동등 연산자 (==)
▫ 두 피연산자가 같은 값으로 평가되는지 비교 후 boolean 값 반환  
▫ 비교할 때 **암묵적 타입 변환**을 통해 타입을 일치시킨 후 비교  
``` js
const a = 1
const b = '1'

console.log(a == b)       // true
console.log(a == true)    // true
```
``` js
// 자동 형변환 

console.log(8 * null)     // 0 (null이 0으로 변환됨)
console.log('5' - 1)      // 4
console.log('5' + 1)      // '51'
console.log('five' * 2)   // NaN
```
**▫ 예상치 못한 결과가 발생할 수 있으므로, 특별한 경우를 제외하고는 사용하지 않음 ‼**

<br>

### 일치 연산자 (===)
▫ 두 피연산자의 값과 타입이 모두 같은 경우 true 반환 
> 암묵적 타입 변환 X  

▫ 같은 객체를 가리키거나, 같은 타입이면서 같은 값인지  
▫ 엄격한 비교

``` js
const a = 1
const b = '1'

console.log(a === b)            // false
console.log(a === Number(b))    // true
```

<br>

### 논리 연산자
▫ and : &&  
▫ or : ||  
▫ not : !  

▫ 단축 평가 지원 
- false && true => false
- true || false => true

<br>

### 삼항 연산자
▫ 3개의 피연산자를 사용하여 조건에 따라 값 반환  
▫ 가장 앞의 조건식이 참이면: 앞의 값 반환  
▫ 그 반대일 경우 : 뒤의 값 반환  
``` js
true ? 1 : 2    // 1
false ? 1 : 2   // 2
```
<br><br>

## 조건문

### 1️⃣ if statement
▫ 조건 표현식의 결과값을 boolean 타입으로 변환 후 참/거짓 판단  
▫ if, else if, else
- 조건은 소괄호 안에 작성
- 실행할 코드는 중괄호 안에 작성
- 블록 스코프 생성 

``` js
const name = 'manager'

if (name === 'admin') {
  console.log('관리자님 환영합니다.')
} else if (name === 'manager') {
  console.log('매니저님 환영합니다.')
} else {
  console.log(`${name}님 환영합니다.`)
}
```


<br>

### 2️⃣ switch statement
▫ 조건 표현식의 결과값이 어느 값에 해당하는지 판별  

▫ 표현식의 결과값을 이용한 조건문  
▫ 표현식의 결과값과 case문의 오른쪽 값 비교  
▫ break, defalut 문은 [선택적]으로 사용 가능  
▫ break문이 없는 경우 break문을 만나거나 defalut문을 실행할 때까지 다음 조건문 실행  
▫ 블록 스코프 생성  
``` js
const name = 'manager'

switch(name) {
  case 'admin' : {
    console.log('관리자님 환영합니다.')
    break
  }
  case 'manager' : {
    console.log('매니저님 환영합니다.')
    break
  }
  default : {
    console.log(`${name}님 환영합니다.`)
  }
}
```
<br>

> 조건이 많은 경우 if문보다는 switch문이 가독성이 좋음 
> 
> 일반적으로 중첩 else if문은 유지보수 힘듦  

<br><br>

## 반복문 

### 1️⃣ while
▫ 조건문이 참이기만 하면 문장을 계속해서 수행 
``` js
let i = 0

while (i < 6) {
  console.log(i)
  i += 1
}

// 0, 1, 2, 3, 4, 5
```
<br>

### 2️⃣ for 
▫ 특정한 조건이 거짓으로 판별될 때까지 반복  

``` js
for (let i = 0; i < 6; i++) {
  console.log(i)
}

// 0, 1, 2, 3, 4, 5
```
> 초기문 : let i = 0  
> 조건문 : i < 6  
> 증감문 : i++  


1. 반복문 진입 및 변수 i 선언
2. 조건문 평가 후 코드 블럭 실행
3. 코드 블록 실행 이후 i 값 증가

<br>

### 3️⃣ for ... in
▫ 객체의 속성을 순회
> 배열 사용 가능, BUT 순서보장 X -> 권장 X

``` js 
const fruits = { a: 'apple', b: 'banana' }

for (const key in fruits) {
  console.log(key)            // a, b
  console.log(fruits[key])    // apple, banana
}
```

<br>

### 4️⃣ for ... of
▫ 반복 가능한 객체를 순회
- array, set, string 등

``` js
const numbers = [0, 1, 2, 3]

for (const number of numbers) {
  console.log(number)       // 0, 1, 2, 3
}
```

<br>

> for ... in 은 속성 이름을 통해 반복  ➡ 객체 순회 적합  
> for ... of 는 속성 값을 통해 반복  ➡ iterable 순회 적합  

> 일반적인 for문의 경우에는 최초 정의한 i를 재할당하면서 사용하기 때문에 const 사용 시 에러 발생  
> 
> 다만 for ... in, for ... of 의 경우에는 재할당이 아니라, 매 반복 시 해당 변수를 새로 정의하여 사용하므로 에러 발생 X 

<br>

![image](https://user-images.githubusercontent.com/93974908/196601066-4c766da6-8350-4fd1-a173-5b1a9fdf72e7.png)

<br><br>

---

# 함수
## 함수 정의

### 1️⃣ 함수 선언식  
▫ 일반적
``` js
function add(num1, num2) {
  return num1 + num2
}

console.log(add(2, 7))      // 9
```
<br>

### 2️⃣ 함수 표현식   
▫ 표현식 안에서 정의  
▫ 익명 함수로 정의 가능  

``` js
const sub = function (num1, num2) {
  return num1 - num2
}

console.log(sub(2, 7))      // -5
```
> 이름 명시 가능  
> BUT, 함수 이름은 호출 사용 X, 디버깅 용 

<br>

### 기본 인자  
▫ 인자 작성 시 '=' 문자 뒤 기본 인자 선언 가능 
``` js
const greeting = function (name = 'Anonymous') {
  return `Hi ${name}`
}

console.log(greeting())     // Hi Anonymous
```

▫ 매개변수와 인자의 개수 불일치 허용  

- 매개변수 < 인자 개수 : 필요한 개수만큼만 
- 매개변수 > 인자 개수 : 모자란 개수만큼 undefined

<br>

### Spread syntax(...)
▫ 전개 구문  
▫ iterable 객체를 요소 / 인자로 확장 가능 

1. 배열과의 사용
2. 함수와의 사용
     - 정해지지 않은 수의 매개변수를 배열로 받을 수 있음


<br><br>

## 선언식 & 표현식
▫ 타입은 function으로 동일  
<br>

### 호이스팅

▫ 함수 선언식 : 호이스팅 발생 (함수 호출 이후 선언해도 동작)

▫ 함수 표현식 : 호이스팅 X (함수 정의 전 호출 시 에러)

![image](https://user-images.githubusercontent.com/93974908/196603124-86535d61-c8bc-4c01-9c19-7ad142177170.png)

<br><br>

## 화살표 함수 (Arrow Function)

▫ "함수를 비교적 간결하게 정의할 수 있는 문법"  

1️⃣ function 키워드 생략 가능  
2️⃣ 함수의 매개변수가 하나라면, ( )도 생략 가능   
3️⃣ 함수의 내용이 한 줄이라면, { } 와 return 도 생략 가능 

``` js
// 기존 함수
const greeting = function (name = 'Anonymous') {
  return `Hi ${name}`
}

// 화살표 함수
// 1단계
const greeting = (name) => {
  return `Hi ${name}`
}

// 2단계
const greeting = name => {
  return `Hi ${name}`
}

// 3단계
const greeting = name => `Hi ${name}`
```
> 에어비앤비 스타일 가이드는 2단계 권장 X  (1단계, 3단계 O)
> 
> 소괄호 사용 : 명확성 & 일관성

▫ 항상 익명 함수 (== 함수 표현식에서만 사용 가능)
> 선언식에서는 사용 불가

``` js
// 인자가 없다면, () or _로 표시 가능
let noArgs = () => 'No args'

// object를 return 한다면, return 을 명시적으로 적어줌
let returnObject = () => { return { key: 'value' } } 

// return을 적지 않으려면, 괄호를 붙여야 함
returnObject = () => ({ key: 'value' })
```


<br>

### 즉시 실행 함수 (IIFE)
▫ 선언과 동시에 실행  
▫ 함수의 선언 끝에 ( ) 추가  
▫ ()에 값을 넣어 인자로 넘겨줄 수 있음  
▫ 일회성 함수 ➡ 익명함수로 사용  
> 초기화 부분에 많이 사용 

``` js
function (num) {return num ** 3}

(num) => { return num ** 3 }

((num) => num ** 3)(2)
```

<br></br>

---

# Array & Object
▫ 참조 타입  
<br>

## 배열 (Array)
▫ 키와 속성들을 담고 있는 참조 타입의 객체  
▫ 순서 보장  
▫ 대괄호 이용하여 생성  
▫ 0을 포함한 양의 정수 인덱스로 특정 값에 접근 가능  
> 음의 정수 인덱싱 불가 

▫ 배열의 길이는 array.length 형태로 접근 가능  
> 배열의 마지막 원소 array.length - 1 로 접근


``` js
const numbers = [1, 2, 3, 4, 5]

console.log(numbers[0])             // 1
console.log(numbers[-1])            // undefined

console.log(numbers.length)               // 5
console.log(numbers.length - 1)           // 4
console.log(numbers[numbers.length - 1])  // 5
```

<br><br>

## 배열 메서드 기초

![image](https://user-images.githubusercontent.com/93974908/196605712-b96fb569-be7c-4513-bba9-db366d0ad8b9.png)

<br>

### .reverse()
▫ 순서 반대로 정렬 

``` js
const numbers = [1, 2, 3, 4, 5]

numbers.reverse()
console.log(numbers)      // [ 5, 4, 3, 2, 1 ]
```
<br>

### .push()
▫ 배열 가장 뒤에 요소 추가

``` js
numbers.push(100)
console.log(numbers)      // [ 5, 4, 3, 2, 1, 100 ]
```
<br>

### .pop()
▫ 배열 마지막 요소 제거

```js
numbers.pop()
console.log(numbers)      // [ 5, 4, 3, 2, 1 ]
```
<br>

### .includs(value)
▫ 배열에 특정 값이 존재하는지 판별 후, true/false 반환

```js
console.log(numbers.includes(1))      // true
console.log(numbers.includes(100))    // false
```
<br>

### .indexOf(value)
▫ 배열에 특정 값이 존재하는지 확인 후, 가장 첫 번째로 찾은 요소의 인덱스 반환  
▫ 해당 값이 없을 경우 -1 반환

``` js
console.log(numbers.indexOf(3))       // 2
console.log(numbers.indexOf(100))     // -1
```
<br>

### .join([separator])
▫ 배열의 모든 요소 연결하여 반환  
▫ 구분자는 선택적으로 지정 가능  
▫ 구분자 생략 시, 쉼표를 기본 값으로 사용  

``` js
console.log(numbers.join())           // 5,4,3,2,1
console.log(numbers.join(''))         // 54321
console.log(numbers.join(' '))        // 5 4 3 2 1
console.log(numbers.join('-'))        // 5-4-3-2-1
```

<br><br>

## 배열 메서드 심화 
**Array Helper Methods**

▫ 배열을 순회하며 특정 로직 수행  
▫ 메서드 호출 시 인자로 collback 함수를 받음  
> **collback** 함수  
> ▫ 어떤 함수의 내부에서 실행될 목적으로 인자로 넘겨받는 함수

![image](https://user-images.githubusercontent.com/93974908/196606995-a8789d11-779e-4d9a-9e1e-5c018b9d3045.png)

<br>

### forEach
▫ 인자로 주어지는 함수를 배열의 각 요소에 대해 한 번씩  실행  
▫ 반환 값 없음
``` js
// 1.
const colors = ['red', 'blue', 'green']

const printClr = function (color) {
  console.log(color)
}

colors.forEach(printClr)


// 2. 
colors.forEach(function (color) {
  console.log(color)
})

// 3.
colors.forEach((color) => {
  console.log(color)
})
```


<br>

### map
▫ forEach + return    
▫ 기존 배열 전체를 다른 형태로 바꿀 때 유용 
``` js
const numbers = [1, 2, 3, 4, 5]

// 1.
const doubleEle = function (number) {
  return number * 2
}

const newArry = numbers.map(doubleEle)
console.log(newArry)            // [ 2, 4, 6, 8, 10 ]

// 2.
const newArry = numbers.map(function (number) {
  return number * 2
})

// 3.
const newArry = numbers.map((number) => {
  return number * 2
})

// 4. 
const newArry = numbers.map((number) => numbers * 2)
```

<br>

### filter
▫ map + 특정 조건 true  
▫ 콜백 함수의 반환 값이 참인 요소들만 모아서 새로운 배열 반환  
``` js
const products = [
  { name: 'cucumber', type: 'vegatable' },
  { name: 'banana', type: 'fruit' },
  { name: 'carrot', type: 'vegatable' },
  { name: 'apple', type: 'fruit' },
]

// 1.
const fruitFilter = function (product) {
  return product.type === 'fruit'
}

const newArry = products.filter(fruitFilter)

console.log(newArry)

// [ { name: 'banana', type: 'fruit' }, { name: 'apple', type: 'fruit' } ]

// 2. 
const newArry2 = products.filter(function (product) {
  return product.type === 'fruit'
})

// 3.
const newArry3 = products.filter((product) => {
  return product.type === 'fruit'
})
```

<br>

### reduce
▫ 인자로 주어지는 함수를 배열의 각 요소에 대해 한 번씩 실행해서, 하나의 결과 값 반환 (누적)   
▫ 총합, 평균 등 계산  
▫ map, filter 등 여러 배열 메서드 동작을 대부분 대체 가능  

▫ 주요 매개변수
- acc : 이전 콜백 함수의 반환 값이 누적되는 변수
- initialValue(optional) : 최초 콜백 함수 호출 시 acc에 할당되는 값, default 값은 배열의 첫번째 값
  > 빈 배열이면 error -> 초기값 써주는 것을 권장

``` js
const numbers = [90, 80, 70, 100]

// 총합

const sumNum = numbers.reduce(function (result, number) {
  return result + number
}, 0)

console.log(sumNum)

const sumNum = numbers.reduce((result, number) => {
  return result + number
}, 0)

// 평균
const avgNum = numbers.reduce((result, number) => result + number, 0) / numbers.length
```


<br>

### find
▫ 콜백 함수의 반환 값이 참이면, 조건을 만족하는 첫번째 요소 반환  
▫ 찾는 값이 배열에 없으면 undefined 반환  
``` js
const avengers = [
  { name: 'Tony Stark', age: 45 },
  { name: 'Steve Rogers', age: 32 },
  { name: 'Thor', age: 40 },
]

const avenger = avengers.find((avenger) => {
  return avenger.name === 'Tony Stark'
})

console.log(avenger)          // { name: 'Tony Stark', age: 45 }

const avenger = avengers.find((avenger) => avenger.name === 'Tony Stark')
```

<br>

### some
▫ 배열의 요소 중 하나라도 주어진 판별 함수를 통과하면 참 반환  
▫ 빈 배열은 항상 false 반환 
``` js
const arr = [1, 2, 3, 4, 5]


// 1.
const result = arr.some(function (elem) {
  return elem % 2 === 0
})

// 2.
const result = arr.some((elem) => {
  return elem % 2 === 0
})


// 4. 
const result = arr.some((elem) => elem % 2 === 0)

console.log(result)
```

<br>

### every
▫ some 의 반대
▫ 배열의 모든 요소가 주어진 판별 함수를 통과하면 참 반환   
▫ 빈 배열은 항상 true 반환  
``` js
const arr = [1, 2, 3, 4, 5]


const result = arr.every((elem) => elem % 2 === 0)

console.log(result)
```

<br><br>

### 배열 순회 비교

▫ for loop   
▫ for ... of   
▫ forEach 

``` js
const chars = ['A', 'B', 'C', 'D']

// for loop
for (let idx = 0; idx < chars.length; idx++) {
  console.log(idx, chars[idx])
}

// for ... of 
for (const char of chars) {
  console.log(char)
}

// forEach
chars.forEach((char, idx) => {
  console.log(idx, char)
})

chars.forEach(char => {
  console.log(char)
})
```

![image](https://user-images.githubusercontent.com/93974908/196662478-085eeebc-4509-400d-9566-4c3a90098fbb.png)

<br><br>

## 객체 (Object)
▫ 속성의 집합  
▫ 중괄호 내부에 key 와 value의 쌍으로 표현  
▫ key는 문자열 타입만 가능  
- key 이름에 띄어쓰기 등의 구분자가 있으면 따옴표로 묶어서 표현

▫ value는 모든 타입 가능  
▫ 객체 요소 접근은 점(.) 또는 대괄호([])로 가능
- key 이름에 띄어쓰기 같은 구분자가 있으면 대괄호 접근만 가능 

<br><br>

## 객체 관련 ES6 문법
### 1️⃣ 속성명 축약
▫ 객체를 정의할 때 key에 할당하는 변수의 이름이 같으면 축약 가능 
``` js
var books = ['Learning JavaScript', 'Learning Python']
var magazines = ['Vogue', 'Science']

// ES5
var bookShop = {
  books: books,
  magazines: magazines,
}

// ES6+
var bookShop = {
  books, 
  magazines,
}

console.log(bookShop)
```


<br>

### 2️⃣ 메서드명 축약
▫ 메서드 선언 시 function 키워드 생략 가능  
``` js
// ES5
var obj = {
  greeting: function () {
    console.log('Hi!')
  }
}

// ES6+
const obj = {
  greeting() {
    console.log('Hi!')
  }
}
```

<br>

### 3️⃣ 계산된 속성명 사용
▫ 객체를 정의할 때 key의 이름을 표현식을 이용하여 동적으로 생성 가능  

``` js
const key = 'country'
const value = ['한국', '미국', '일본', '중국']

const myObj = {
  [key]: value,
}

console.log(myObj)              // { country: [ '한국', '미국', '일본', '중국' ] }
console.log(myObj.country)      // [ '한국', '미국', '일본', '중국' ]
``` 

<br>

### 4️⃣ 구조 분해 할당 ✔ 
▫ 배열 또는 객체를 분해하여 속성을 변수에 쉽게 할당할 수 있는 문법  

> 함수에서 유용하게 사용 

``` js
const userInfo = {
  name: 'yonghyun cho',
  userId: 'yong12',
  phoneNumber: '010-1234-1234',
  email: 'yong12@naver.com'
}

const name = userInfo.name
const userId = userInfo.userId
const phoneNumber = userInfo.phoneNumber
const email = userInfo.email

// 구조 분해 할당
const { name } = userInfo
const { userId } = userInfo
const { phoneNumber } = userInfo
const { email } = userInfo

// 여러 개도 가능
const { name, userId } = userInfo
```

<br>

### 5️⃣ 객체 전개 구문
▫ 전개구문을 사용해 객체 내부에서 객체 전개 가능 
> 얕은 복사에 활용 가능 

``` js
const obj = { b: 2, c: 3, d: 4 }
const newObj = { a: 1, ...obj, e: 5 }

console.log(newObj)           // { a: 1, b: 2, c: 3, d: 4, e: 5 }
```

<br><br>

### JSON (JavaScriptON) 
▫ Key-Value 형태로 이루어진 자료 표기법  
▫ 형식이 있는 "문자열"  
▫ JSON을 JavaScript에서 사용하려면 Object로 바꿔줘야 함  
▫ JSON을 Object로 사용하기 위해서는 변환 작업 필요

<br>

✔ 배열은 객체  
▫ 키와 속성들을 담고 있는 참조 타입의 객체  
▫ 배열은 인덱스를 키로 갖으며 length 프로퍼티를 갖는 특수한 객체

