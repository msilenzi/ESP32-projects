let rgbColor = { red: 128, green: 128, blue: 128 }

const $inputsNumber = document.querySelectorAll('input[type="number"]')
const $inputsRange = document.querySelectorAll('input[type="range"]')

function updateBodyBackground() {
  const rgb = `rgb(${rgbColor.red}, ${rgbColor.green}, ${rgbColor.blue})`
  document.body.style.backgroundColor = rgb
}

function updateInputValues() {
  $inputsNumber.forEach((i) => (i.value = rgbColor[i.dataset.channel]))
  $inputsRange.forEach((i) => (i.value = rgbColor[i.dataset.channel]))
}

async function getColor() {
  const resp = await fetch('/led_rgb')
  const data = await resp.json()
  return data
}

async function updateColor() {
  rgbColor = await getColor()
  updateBodyBackground()
  updateInputValues()
}

$inputsRange.forEach((input) => {
  input.addEventListener('input', (e) => {
    const parsedValue = parseInt(e.target.value, 10)
    rgbColor[e.target.dataset.channel] = parsedValue
    e.target.parentNode.querySelector('.range-item__value').value = parsedValue
    updateBodyBackground()
  })
})

$inputsNumber.forEach((input) => {
  input.addEventListener('input', (e) => {
    const parsedValue = parseInt(e.target.value, 10)
    rgbColor[e.target.dataset.channel] = parsedValue
    e.target.parentNode.querySelector('input[type="range"]').value = parsedValue
    updateBodyBackground()
  })
})

document.querySelector('#btn-submit').addEventListener('click', async (e) => {
  e.preventDefault()
  e.target.disabled = true
  await fetch('/led_rgb', {
    method: 'POST',
    body: JSON.stringify(rgbColor),
    headers: { 'Content-Type': 'application/json' },
  })
  e.target.disabled = false
})

document.querySelector('#btn-update').addEventListener('click', async (e) => {
  e.preventDefault()
  e.target.disabled = true
  await updateColor()
  e.target.disabled = false
})

document.addEventListener('DOMContentLoaded', updateColor)
