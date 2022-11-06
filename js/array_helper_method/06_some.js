// 1. requests 배열에서 status가 pending인 요청이 있는지 확인하세요.
const requests = [
  { url: '/photos', status: 'complete' },
  { url: '/albums', status: 'pending' },
  { url: '/users', status: 'failed' },
]

// answer
const request = requests.some((request) => {
  return request.status === 'pending'
})
console.log(request)