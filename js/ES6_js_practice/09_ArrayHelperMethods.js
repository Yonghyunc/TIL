const arr = [1, 2, 3]

/* 
array helper methods 의 생김새
.forEach, .map, .find, .filter
arr.helperMethod(callbackFunction)
arr.helperMethod(function (arg) {})

*/

// .forEach(cb)  => return 되는 값 없음 === 콜백 함수에 return 필요 없음
  arr.forEach(function (num) {
    console.log(num)
  })

  // for - of 의 대체제 느낌
  for (const num of arr) {
    console.log(num)
  }

// .map(cb) => 콜백함수의 리턴값으로 만든 배열을 리턴
  arr.map(num => num  * 2)

  // 사용 예시
  // 1.
  const contents = ['hello', 'world']
  const tags = contents.map(function (content) {
    return `<h2>${content}</h2>`
  })
  tags.forEach(tag => document.write(tag))
  // 2.
  contents.map(content => `<h2>${content}</h2>`).forEach(tag => document.write(tag))


// .find(cb) => 콜백 함수의 리턴값이 true(혹은 true로 평가되는)
// 첫번째 요소만 리턴
  arr.find(function (num) {
    return num === 2
  })

  arr.find(num => num === 2)

  const articles = [
    {pk: 1, title: 'hi'},
    {pk: 2, title: 'hello'},
    {pk: 3, title: 'great'},
  ]

  articles.find(article => article.pk === 3)


// .filter(cb) => 콜백함수의 리턴값이 true(혹은 true 로 평가되는)
// 요소만 모아서 배열로 리턴
  arr.filter(num => num % 2)

  // 사용 예시
  const movies = [
    {title: 'matrix', isAdult: false},
    {title: 'kingsman', isAdult: true}
  ]

  const adultMovies = movies.filter(function (movie) {
    return movie.isAdult
  })

  // const adultMovies = movies.filter(movie => movie.isAdult)


// .some(cb), .every(cb) => 배열 안의 하나라도 / 전부 콜백에서 return 하는 조건을 만족하면 t/f 를 리턴
  arr.every(num => num > 0)  // [1, 2, 3]  => true, true, true => true
  arr.every(num => num > 1)  // [1, 2, 3]  => false, true, true => false

  arr.some(num => num > 100)   // [1, 2, 3]  => false, false, false => false
  arr.some(num => num > 2)   // [1, 2, 3]  => false, false, true => true

/* 
  - 배열의 각 요소에 대해 주어진 `reduce` 함수를 실행하고, 하나의 결과 값을 반환
  - reduce는 map, filter 등 여러 배열 메서드의 동작을 대부분 대체 가능
  - 첫번째 매개변수인 콜백함수의 첫번째 매개변수(acc)는 `누적 값(전 단계의 결과)`
  - 두번째 매개변수인 `initialValue`는 반환할 누적 값의 초기 값이고 없을 시 첫번째 요소 값이 누적 값
*/
  arr.reduce(function (acc, num) {
    console.log(num, acc)
  }, 0)

  // 총 합 구하기
  arr.reduce(function (acc, num) {
    return acc + num
  }, 0)

  // 2씩 곱하기(map)
  arr.reduce(function (acc, num) {
    acc.push(num * 2)
    return acc
  }, [])
