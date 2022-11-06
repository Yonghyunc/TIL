// if, else, else if === truthy, falsy 값에 따라 실행

let age = 10

if (age > 19) {
  console.log('성인')
} else if ( age > 10 ) {
  console.log('어린이')
} else {
  console.log('유아')
}

// switch & case
// break로 끊어주지 않으면 계속 내려감

const id = 'admin'

switch (id) {
  case 'admin': {
    console.log('관리자님, 환영합니다.')
    break
  }
  case 'manager': {
    console.log('매니저님 환영합니다.')
    break
  }
  default: {
    console.log(`${id} 님, 환영합니다`)
  }
}
