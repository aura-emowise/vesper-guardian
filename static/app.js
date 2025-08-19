
// static/app.js - Final Version

const chartCtx = document.getElementById('trend-chart').getContext('2d');
const trendChart = new Chart(chartCtx, {
    type: 'line',
    data: { labels: Array(60).fill(''), datasets: [{ label: 'Well-being Index', data: Array(60).fill(0), borderColor: 'rgba(75, 192, 192, 1)', backgroundColor: 'rgba(75, 192, 192, 0.2)', borderWidth: 2, pointRadius: 0, tension: 0.4, fill: true }] },
    options: { scales: { y: { min: 0, max: 10, ticks: { color: '#aaa' } }, x: { ticks: { display: false } } }, plugins: { legend: { display: false } }, responsive: true, maintainAspectRatio: false }
});

let isFirstLoad = true;

function toggleModal() { document.getElementById('log-modal').classList.toggle('visible'); }

function logManualEvent(message) {
    fetch('/log_manual_event', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ message: message }) })
    .then(() => {
        updateDashboard();
        if(document.getElementById('log-modal').classList.contains('visible')) toggleModal();
    });
}

function updateDashboard() {
    fetch('/data').then(response => response.json()).then(data => {
        const { analysis, vitals, patient_info, log, history } = data;
        const card = document.getElementById('status-card');
        document.getElementById('status-text').textContent = analysis.status;
        document.getElementById('index-value').textContent = `${analysis.index.toFixed(1)} / 10.0`;
        document.getElementById('progress-bar').style.width = `${analysis.index * 10}%`;
        card.className = 'card';
        const acknowledgeButton = document.getElementById('acknowledge-button');
        if (analysis.status === 'Unease') { card.classList.add('unease'); acknowledgeButton.style.display = 'inline-block'; } 
        else if (analysis.status === 'Distress Alert!') { card.classList.add('distress'); acknowledgeButton.style.display = 'inline-block'; } 
        else { card.classList.add('calm'); acknowledgeButton.style.display = 'none'; }
        document.getElementById('hr-value').textContent = `${vitals.hr.toFixed(1)} bpm`;
        document.getElementById('eda-value').textContent = `${vitals.eda.toFixed(2)} µS`;
        document.getElementById('bp-value').textContent = `${vitals.bp} mmHg`;
        const logList = document.getElementById('log-list');
        logList.innerHTML = '';
        log.forEach(event => { const li = document.createElement('li'); li.className = `log-${event.type}`; li.innerHTML = `<span>${event.timestamp}</span> - ${event.message}`; logList.appendChild(li); });
        trendChart.data.datasets[0].data = history; trendChart.update('none');
        if (isFirstLoad) {
            document.getElementById('patient-name').textContent = patient_info.name;
            document.getElementById('patient-yob').textContent = patient_info.year_of_birth;
            document.getElementById('patient-height').textContent = patient_info.height_cm;
            document.getElementById('patient-weight').textContent = patient_info.weight_kg;
            document.getElementById('patient-anamnesis').textContent = patient_info.anamnesis;
            isFirstLoad = false;
        }
    }).catch(error => console.error('Error fetching data:', error));
}
setInterval(updateDashboard, 3000);
window.onload = updateDashboard;

const canvas = document.getElementById('matrix-canvas'); const ctx = canvas.getContext('2d');
canvas.width = window.innerWidth; canvas.height = window.innerHeight;
const characters = '01'; const charactersArray = characters.split('');
const fontSize = 16; const columns = canvas.width / fontSize;
const drops = []; for (let x = 0; x < columns; x++) drops[x] = 1;
function drawMatrix() {
    ctx.fillStyle = 'rgba(18, 18, 18, 0.05)'; ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.fillStyle = '#0F0'; ctx.font = fontSize + 'px Share Tech Mono';
    for (let i = 0; i < drops.length; i++) {
        const text = charactersArray[Math.floor(Math.random() * charactersArray.length)];
        ctx.fillText(text, i * fontSize, drops[i] * fontSize);
        if (drops[i] * fontSize > canvas.height && Math.random() > 0.975) drops[i] = 0;
        drops[i]++;
    }
}
setInterval(drawMatrix, 50);