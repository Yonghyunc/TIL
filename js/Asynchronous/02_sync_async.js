// 02. 동기와 비동기


// 동기
console.log('첫 번째')
console.log('두 번째')
console.log('세 번째')


// 비동기
console.log('첫 번째')
setTimeout(() => console.log('두 번째'), 2000)
console.log('세 번째')

/*
[Call Stack]

console.log ➡ 3) '세 번째' 출력 후 pop
setTimeout ➡ 2) web API에서 function을 넘김
console.log ➡ 1) '첫 번째' 출력 후 pop
전역

[Web API]
2초 타이머


*/

// setTimeout 뒤의 함수는 js 엔진과 web API가 동시에 진행 (주체가 다르기 때문에)