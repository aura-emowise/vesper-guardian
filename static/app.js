#### 


```javascript
// 

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
        const { analysis, vitals, patient_info, log } = data; // 
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
        
        // 
        
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