// API

async function fetchLedsValues() {
  const resp = await fetch('/leds')
  const data = await resp.json()
  return data
}

async function turnOffLed(n) {
  await fetch(`/leds/${n}/off`, { method: 'POST' })
}

async function turnOnLed(n) {
  await fetch(`/leds/${n}/on`, { method: 'POST' })
}

// UI

function createLedItem(n, isOn) {
  const li = document.createElement('li')
  li.className = 'leds-list__item'

  const p = document.createElement('p')
  p.innerText = `Led ${n}`
  li.appendChild(p)

  const div = document.createElement('div')
  li.appendChild(div)

  const check = document.createElement('input')
  check.type = 'checkbox'
  check.id = `led-${n}`
  check.checked = isOn
  check.className = 'tgl tgl-ios'
  div.appendChild(check)

  const label = document.createElement('label')
  label.htmlFor = `led-${n}`
  label.className = 'tgl-btn'
  div.appendChild(label)

  check.addEventListener('input', async (e) => {
    e.target.disabled = true

    if (e.target.checked) {
      turnOnLed(n)
    } else {
      turnOffLed(n)
    }

    e.target.disabled = false
  })

  return li
}

function updateCheckboxState(ledsValues) {
  const checks = document.querySelectorAll('#leds-list input[type="checkbox"]')
  checks.forEach((check, i) => (check.checked = ledsValues[i]))
}

// Main

document.addEventListener('DOMContentLoaded', async () => {
  const ledsValues = await fetchLedsValues()

  ledsValues.forEach((value, i) => {
    document.querySelector('#leds-list').appendChild(createLedItem(i, value))
  })
})

setInterval(async () => {
  const data = await fetchLedsValues()
  updateCheckboxState(data)
}, 5000)
