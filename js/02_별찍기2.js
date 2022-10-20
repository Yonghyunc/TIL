let star = (n) => {
  for (let i = 1; i <= n; i++) {
    for (let j = 1; j <= n - i; j++) {
      process.stdout.write(' ')
    }
    for (let l = 1; l < 2 * i; l++) {
      process.stdout.write('*')
    }
    console.log()
  }
}

star(5)
