/*
김해킹은 구슬치기 대회에 참가하였다.
모든 인원은 참가 번호를 부여받는데, 자신과 같은 참가 번호를 가진 사람과 구슬치기 게임을 진행하여야 한다. 
단, 반드시 짝이 없는 한 명의 깍두기가 존재한다.
각 시도별 참가자들의 참가 번호 정보가 배열로 주어질 때, 깍두기의 참가 번호를 출력하시오.

[제약 사항]
1. 깍두기 번호는 1번부터 시작
2. 깍두기는 1명만 존재
3. 깍두기를 제외한 모든 참가자는 자신의 짝이 존재
*/

const participantNums = [[1, 3, 2, 2, 1],
[3, 7, 100, 21, 13, 6, 5, 7, 5, 6, 3, 13, 21],
[9, 1, 8, 7, 71, 33, 62, 35, 11, 4, 7, 71, 33, 8, 9, 1, 4, 11, 35]
]


const find = (parti) => {
  let go = true
  while (true) {
    let n = parti[0]                  // 배열의 첫 값을 n으로 할당
    parti.splice(0, 1)                // 할당 후 삭제

    let cant = true
    for (let num of parti) {          // 배열에 남은 값을 탐색
      if (num === n) {                // 같은 값이 있다면
        parti = parti.filter((num) => num !== n)    // 그 값 또한 삭제
        cant = false                                // 삭제 표시
        break
      }
    }
    if (cant) {                       // 반복문을 돌 동안 같은 값을 못 찾았으면
      // go = false                      // while 문 종료
      return n                        // 해당 n 값 반환
    }
  }
}

for (participantNum of participantNums) {
  console.log(find(participantNum))
}
