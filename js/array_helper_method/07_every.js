// 1. users 배열에서 모두가 submmited 인지 여부를 hasSubmitted 에 저장하세요.
const users = [
  { id: 21, submmited: true },
  { id: 33, submmited: false },
  { id: 712, submmited: true },
]

// answer
const hasSubmitted = users.every((user) => {
  return user.submmited
})
console.log(hasSubmitted)