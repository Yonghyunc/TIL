/*
  Operands
  1. unary (단항 연산자)
  -, typeof, ++, --, !
  2. binary (이항 연산자)
  +, -, *, /, +=, -=, *=, /=, >, >=, <, <=
  &&, ||
  3. ternary (삼항 연산자)
  ? :

  1. 산술연산자
  2. 수 비교연산자
  3. 동등/일치 연산자
  4. 논리연산자
*/

let i = 1
// i에 대한 평가가 끝난 후, 1을 더한다.
console.log(i++)
// i에 대한 평가 전에 1을 더한다.
console.log(++i)

// ! => not 과 같다
console.log(!true)

// 동등 ==  => 안 씀
0 == '0'   // true
0 == []    // true
'0' == []  // false


// 일치 === => 우리가 원래 아는 바로 그 연산자
1 === 1
1 !== 2


// and => &&, or => ||
console.log(true && true && false)
console.log(false || true || true)


// 가치평가 ? true일 경우 : false 일 경우
console.log(1 > 2 ? '크다' : '작다')

let a = 1
const even_or_odd = a % 2 ? 'odd' : 'even'
console.log(even_or_odd)
