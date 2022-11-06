// while 문!
let i = 0
while (i < 5) {
  console.log('hi')
  i++
}


const numbers = [1, 2, 3, 4, 5]
// 전통적인 for
for (let j=0; j<numbers.length; j++) {
  console.log(numbers[j])
}

// Array용 => 요소를 꺼내는 for - of
for (const number of numbers) {
  console.log(number, typeof(number))
}

// Object => Key 를 꺼내는 for - in
const person = {name: 'neo', 'address': 'seoul'}
for (const key in person) {
  console.log(key, person[key])
}

// 이렇게 배열을 돌아버리면, 스트링으로 타입이 찍힘, typeof는 뒤에 한칸 띄고 붙여도 됨.
for (const number in numbers) {
  console.log(number, typeof number)
}