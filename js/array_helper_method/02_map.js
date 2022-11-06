// 1. 숫자가 담긴 배열로 각 숫자들의 제곱근이 들어있는 새로운 배열을 만드시오.
const newNumbers = [4, 9, 16]

// answer
const newNums = newNumbers.map((number) => {
  return number ** 2
})
console.log(newNums)

// 2. images의 요소들의 height 값만 저장되어 있는 배열 heights 를 만드시오.
const images = [
  { height: '34px', width: '39px' },
  { height: '54px', width: '19px' },
  { height: '83px', width: '75px' },
]

// answer
const heights = images.map((image) => {
  return image.height
})
console.log(heights)