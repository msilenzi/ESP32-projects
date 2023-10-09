let counter1 = 0
let counter2 = 0

document.querySelector('#btn-counter1').addEventListener('click', () => {
  document.querySelector('#counter1').innerHTML = ++counter1
})

document.querySelector('#btn-counter2').addEventListener('click', () => {
  document.querySelector('#counter2').innerHTML = ++counter2
})