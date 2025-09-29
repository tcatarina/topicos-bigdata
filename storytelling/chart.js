document.addEventListener('DOMContentLoaded', function () {
    const ctx = document.getElementById('horasChart').getContext('2d');

    const funcionarios = ["Ana", "Bruno", "Carlos", "Diana", "Eduardo"];
    const horas_trabalhadas = [40, 35, 30, 45, 38];

    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: funcionarios,
            datasets: [{
                label: 'Horas Trabalhadas na Semana',
                data: horas_trabalhadas,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            },
            responsive: true,
            maintainAspectRatio: false
        }
    });
});
