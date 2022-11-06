// 1. images 배열안에 있는 정보(height, width)를 곱해 넓이를 구하여 areas 배열에 저장하시오.
const images = [
  { height: 10, width: 30 },
  { height: 20, width: 90 },
  { height: 54, width: 32 },
]

const areas = []

// answer
images.forEach((image) => {
  areas.push(image.height * image.width)
})
console.log(areas)


// 2. 아래 함수에서 for 를 forEach 로 바꾸시오.
// function handlePosts() {
//   const posts = [
//     { id: 23, title: 'Daily JS News' },
//     { id: 52, title: 'Code Refactor City' },
//     { id: 105, title: 'The Brightest Ruby' },
//   ]

//   for (let i = 0; i < posts.length; i++) {
//     console.log(posts[i])
//     console.log(posts[i].id)
//     console.log(posts[i].title)
//   }
// }

// handlePosts()

// answer
function handlePosts() {
  const posts = [
    { id: 23, title: 'Daily JS News' },
    { id: 52, title: 'Code Refactor City' },
    { id: 105, title: 'The Brightest Ruby' },
  ]

  posts.forEach((post) => {
    console.log(post)
    console.log(post.id)
    console.log(post.title)
  })
}
handlePosts()