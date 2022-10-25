/* 
player1과 player2의 가위바위보 경우의 수가 차례대로 배열로 주어질 때,
각 회차마다 어느 플레이어가 이겼는지 출력 

게임은 10회 진행
비긴 경우 0 출력
*/

const p1 = ['rock', 'paper', 'scissors', 'scissors', 'rock', 'rock', 'paper', 'paper', 'rock', 'scissors']
const p2 = ['paper', 'paper', 'rock', 'scissors', 'paper', 'scissors', 'scissors', 'rock', 'rock', 'rock']


const hand = {
  'scissors': 1,
  'rock': 2,
  'paper': 3,
}
console.log(hand)
const playGame = (p1_choice, p2_choice) => {
  num = hand[p1_choice] - hand[p2_choice]
  if (num === 0) {
    return 0
  } else if (num === 1 || num === -2) {
    return 1
  } else {
    return 2
  }
}


