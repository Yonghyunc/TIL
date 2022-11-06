// JSON === JavaScript Object Notation

const obj = 
[
  {
    coffee: 'Americano',
    iceCream: 'Cookie&Cream',
  },
  {
    coffee: 'Americano',
    iceCream: 'Cookie&Cream',
  },
  {
    coffee: 'Americano',
    iceCream: 'Cookie&Cream',
  }
]


const jsonData = JSON.stringify(obj)
const backToObj = JSON.parse(jsonData)

console.log(jsonData)
