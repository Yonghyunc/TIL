// 1. numbers 배열중 50보다 큰 값들만 모은 배열 filteredNumbers 을 만드시오.
const numbers = [15, 25, 35, 45, 55, 65, 75, 85, 95]

// answer
const filteredNumbers = numbers.filter((number) => {
  return number > 50
})
console.log(filteredNumbers)


// 2. users 배열에서 admin user만 가진 filteredUsers 배열을 만드세요.
const users = [
  { id: 1, admin: false, name: 'harry' },
  { id: 2, admin: false, name: 'aiden' },
  { id: 3, admin: true, name: 'jun' },
  { id: 4, admin: false, name: 'viktor' },
  { id: 5, admin: true, name: 'isaac' },
]

// answer
const filteredUsers = users.filter((user) => {
  return user.admin
})
console.log(filteredUsers)