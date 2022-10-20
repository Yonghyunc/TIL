// 1. 해당 코드를 template string 을 활용하여 리팩토링하시오.

/*
const name = 'Tom'
console.log('Hi, my name is' + name)
*/

// Template Literal
const name = 'Tom'
console.log(`Hi, my name is ${name}`)




// 2. 해당 코드를 arrow function 으로 리팩토링하시오.

/*
function add(x, y) {
  return x + y
}
 */

const add = (x, y) => x + y
console.log(add(1, 2))




// 3. 해당 코드의 메서드 introduce 를 function 키워드 없이 리팩토링하시오.

/*
const tom = {
  name: 'Tom',
  introduce: function () {
    console.log('Hi, my name is' + this.name)
  }
}
*/

// 메서드명 축약 : 메서드 선언 시 function 키워드 생략 가능
const tom = {
  name: 'Tom',
  introduce() {
    console.log('Hi, my name is ' + this.name)
  }
}
console.log(tom.introduce())




// 4. 해당 코드를 key, value를 한번씩만 작성하도록 리팩토링하시오.

/*
const url = 'https://test.com'
const data = { message: 'Hello World!' }

const request = { url: url, data: data }
*/

// 속성명 축약 : 객체를 정의할 때 key에 할당하는 변수의 이름이 같으면 축약 가능
const url = 'https://test.com'
const data = { message: 'Hello World!' }

const request = { url, data, }
console.log(request)