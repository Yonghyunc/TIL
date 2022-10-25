function palindrome(str) {
  if (str === str.split('').reverse().join('')) {
    return true
  } else {
    return false
  }
}



console.log(palindrome('level'))     // true
console.log(palindrome('hi'))        // false