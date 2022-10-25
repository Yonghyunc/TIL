const star = '*'
const star_print = (n) => {
  let stars = ''
  for (let i = 1; i <= n; i++) {
    stars += star
    console.log(stars)
  }
}
star_print(5)