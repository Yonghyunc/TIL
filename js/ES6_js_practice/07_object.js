/*
  {key: value}  => Object === 객체 
  python dict 와 다른점
  1. key 문자열의 따옴표 삭제 가능(띄어쓰기 없을 때)
  2. 접근할 때, ['key'] 와 .key 모두 가능
 */

// Object (객체 데이터) -> key : value 형태 저장

const myself = {
  name: 'Alex',
  alive: true,
  age: 1,
  friends: ['hk', 'mj', 'dc'],
  home: {
    address: 'Seoul',
  }
}

// 체이닝 접근
console.log(myself.home.address)
// 실제로 const 로 obj를 할당해둬도, 안에 내용을 체이닝 접근으로 수정하는건 가능함.


// ES6 축약 문법 정리
/*  ES6+ 축약 문법 */
// 1. key - value 가 같은 이름일 경우
// Old
var books = ['LearningJS', 'EloquentJS']
var magazines = ['GQ', 'esquire']

var bookshop = {
  books: books,
  magazines: magazines,
}

// New
const books = ['LearningJS', 'EloquentJS']
const magazines = ['GQ', 'esquire']

const bookshop = {
  books,
  magazines,
}

// 2. Object 안의 함수(메서드) 정의
// Old 
var dooly = {
  name: 'dooly',
  greeting: function () {
    console.log('어서 오고')
  }
}

// New
const dooly = {
  name: 'dooly',
  // Arrow
  greeting1: () => console.log('도우너,'),
  // Function 키워드 대체용
  greeting2 () {
    console.log('어서오고')
  },
}


// 3. (minor) computed property name
const key = 'regions'
const value = ['서울', '경기', '인천', '대전', '부산']
const korea = {
  [key]: value
}
korea.regions


// 4. Object Destructuring (비구조화)
// Old
var userInfo = {
  name: 'alex',
  email: 'alex@gmail.com',
  phone: '0101234567',
}

var name = userInfo.name
var email = userInfo.email
var phone = userInfo.phone

// New  변수명과 key값이 같다면, 아래와 같이 작성 가능
const userInfo = {
  name: 'alex',
  email: 'alex@gmail.com',
  phone: '0101234567',
}

// const { name } = userInfo
// const { email } = userInfo
// const { phone } = userInfo
const { name, email, phone } = userInfo

function printInfo({ name, email, phone }) {
  console.log(`안녕 나는 ${name} ${email} ${phone} `)
}

printInfo(userInfo)
