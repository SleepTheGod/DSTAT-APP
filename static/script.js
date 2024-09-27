document.getElementById('submit').addEventListener('click', function() {
    const ipAddress = document.getElementById('ip_address').value;

    fetch('/get_dstat_data', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `ip_address=${ipAddress}`
    })
    .then(response => response.json())
    .then(data => {
        updateChart(data);
    });
});

const ctx = document.getElementById('dstatChart').getContext('2d');
let dstatChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: [], // Will be filled dynamically
        datasets: [
            {
                label: 'CPU Usage',
                data: [],
                borderColor: 'rgba(75, 192, 192, 1)',
                fill: false,
            },
            {
                label: 'Disk Usage',
                data: [],
                borderColor: 'rgba(153, 102, 255, 1)',
                fill: false,
            }
        ]
    },
    options: {
        responsive: true,
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});

function updateChart(data) {
    dstatChart.data.labels = data.time;
    dstatChart.data.datasets[0].data = data.cpu;
    dstatChart.data.datasets[1].data = data.disk;
    dstatChart.update();
}
