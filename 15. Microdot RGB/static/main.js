let rgbColor = { red: 128, green: 128, blue: 128 }

const $inputsNumber = document.querySelectorAll('input[type="number"]')
const $inputsRange = document.querySelectorAll('input[type="range"]')

async function fetchColor() {
  const resp = await fetch('/led_rgb')
  const data = await resp.json()
  rgbColor = data
  updateColor()
}

async function submitColor() {
  fetch('/led_rgb', {
    method: 'POST',
    body: JSON.stringify(rgbColor),
    headers: { 'Content-Type': 'application/json' },
  })
}

function updateBodyBackground() {
  const rgb = `rgb(${rgbColor.red}, ${rgbColor.green}, ${rgbColor.blue})`
  document.body.style.backgroundColor = rgb
}

function updateInputValues() {
  $inputsNumber.forEach((i) => (i.value = rgbColor[i.dataset.channel]))
  $inputsRange.forEach((i) => (i.value = rgbColor[i.dataset.channel]))
}

function updateColor() {
  updateBodyBackground()
  updateInputValues()
}

function inputHandler(e) {
  const parsedValue = parseInt(e.target.value, 10)
  rgbColor[e.target.dataset.channel] = parsedValue
  updateColor()
}

$inputsRange.forEach((input) => input.addEventListener('input', inputHandler))
$inputsNumber.forEach((input) => input.addEventListener('input', inputHandler))

document.querySelector('#btn-submit').addEventListener('click', async (e) => {
  e.preventDefault()
  e.target.disabled = true
  await submitColor()
  e.target.disabled = false
})

document.querySelector('#btn-update').addEventListener('click', async (e) => {
  e.preventDefault()
  e.target.disabled = true
  await fetchColor()
  e.target.disabled = false
})

document.addEventListener('DOMContentLoaded', fetchColor)
