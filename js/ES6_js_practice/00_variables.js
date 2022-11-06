/*
1. dash-case(kebab-case)
-> HTML, CSS에서 활용

2. snake_case
-> HTML, CSS에서 활용

3. camelCase === lowerCamelCase
-> JS에서 주로 활용

4. PascalCase === UpperCamelCase
-> 생성자 함수, class 명 JS에서 활용

5. UPPER_SNAKE_CASE
-> 절대 변하면 안되는 상수값에 활용
*/

// let => 변수, 재할당 가능
let x = 1
x = 2

// 세미콜론 빼도 js 엔진이 어차피 넣어서 해석해줌.
let myName = 'Alex';

// const => 상수, *재할당* 불가능
const y = 1
y = 2 // TypeError : Assignment to constant variable.

// var -> hoisting 이슈로 쓰지 않음.

// Reserved Words 
// let this => SyntaxError
// let if
// let break

console.log(foo) // undefined
var foo;

console.log(bar) // Error: Uncaught ReferenceError: bar is not defined
let bar;