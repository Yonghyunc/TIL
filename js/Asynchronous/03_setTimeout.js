// 03. 동기, 비동기, 실행 컨텍스트 종합 

function sleep(sec) {
  const delayUntil = Date.now() + sec
  while (Date.now() < delayUntil) { }
}

for (let i = 1; i <= 10; i++) {
  console.log(`${i}번째 반복`)
  sleep(1000)
}

setTimeout(function () {
  console.log("5초 뒤 실행 !")
}, 5000)



// "10번째 반복" 문구 이후로 5초가 흐른 다음 "5초 뒤 실행 !"이 나온다

