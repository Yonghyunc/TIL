// 01. 콜스택과 실행 컨텍스트

// 자바스크립트는 Single Thread
// 가장 먼저 콜스택에 쌓이는 것 - 전역코드 (코드 전체)

/*
[Call Stack]

console.log ➡ 3) 출력 후 pop
bar() ➡ 4) 끝나면 pop
console.log ➡ 1) 출력 후 pop
foo() ➡ 2) 끝나면 pop
전역 ➡ 5) call stack이 비었으면 pop

함수가 호출될 때마다 콜스택에 쌓이는데, 이것을 컨텍스트가 실행되었다고 함 
각각을 실행 컨텍스트라고 함

*/

const foo = function () {
  console.log('foo')
}

const bar = function () {
  console.log('bar')
}

foo()
bar()