const $counters = document.querySelectorAll('#counters-list .counter')
const $counterButtons = document.querySelectorAll('#counters-list .btn-counter')

function updateCounters(data) {
  $counters.forEach((counter, i) => {
    counter.innerHTML = data[i].value
  })
}

async function getCounters() {
  const resp = await fetch('/counters')
  const data = await resp.json()
  updateCounters(data)
}

async function incrementCounter(id) {
  const resp = await fetch(`/counters/${id}/increment`, { method: 'POST'})
  const data = await resp.json()
  updateCounters(data)
}


$counterButtons.forEach((btn, i) => {
  btn.addEventListener('click', async (e) => {
    e.target.disabled = true
    await incrementCounter(i)
    e.target.disabled = false
  })
})

document.addEventListener('DOMContentLoaded', getCounters)
setInterval(getCounters, 3000)
