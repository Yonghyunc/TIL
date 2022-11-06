/*
  함수를 정의하는 3가지 방법
  1. 선언식
  2. 표현식
    1. function
    2. => (arrow function)
*/


// 1. 선언식 : function funcName() {} == 기명 함수
// n1, n2 ==> 매개변수(Parameters)
function add(n1, n2) {
  return n1 + n2
}

let a = add(1, 2) // 1, 2는 인수(Arguments)

// 2-1 : const funcName = function () {}
// 익명 함수들은 sub 등과 같은 변수에 할당해 쓰거나 값으로 사용
const sub = function (n1, n2) {
  return n1 - n2
}

// 2-2 : () => {}  Arrow Function (~ES6)
/* 
1. function 키워드를 지운다.
2. () 와 {} 사이에 => 를 넣는다.
--
3. 인자가 딱 1개라면, 괄호 생략 가능
4. 블록 안에 return 구문만 있으면 {} 와 return 모두 삭제 가능

* function(){} vs () => {}
내부에 this 키워드가 있으면 다르게 동작. 이외에는 모두 같음
*/

// original
let cube = function (n) {
  return n ** 3
}

// 1, 2 번 적용시
cube = (n) => {
  return n ** 3
}

// 3, 4 번 적용시
cube = n => n ** 3

// 3번 적용 불가능 할 경우
mul = (n1, n2) => n1 * n2
printer = () => console.log('hi')


// Default Arguments
function withOutDefaultArg(a, b) {
  if (a === undefined) {
    a = 0
  }
  if (b === undefined) {
    b = 0
  }
  return a + b
}

function withDefaultArg(a=0, b=0) {
  return a + b
}
