// 데이터 종류 (자료형) -> JS는 데이터 기준으로 사고.

/*
  Primitive Types
  1. Number
  2. String
  3. Empty
  4. Booelan
*/

// String, Interpolation
let myName = "Alex"
let greeting = `Hello ${myName}`
console.log(greeting)

console.log(
  'String Type: ',
  'hello', "world!", 'Alex' + 'Kwon',
  `1 + 1 = ${1 + 1}`  // Template Literal
)

// Number
let number = 1

console.log(
  'Number Type: ', 
  1, -1, 3.14, 2.998e3,
  Infinity, -Infinity, 10 / 0, 
  NaN, // Not a Number => 산술연산자 좌우의 타입이 맞지 않을 때
)

// Empty values
let undef; 
console.log(undef) // undefined 값이 할당되지 않은 상태

console.log(
  'Empty Values: ',
  undefined, null  
  // null === 어떤 값이 '의도적으로' 비어있음을 의미
)

// Boolean -> 딱 두개만 존재!
console.log(
  'Boolean Type: ',
  true, false
)
