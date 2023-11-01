document.getElementById("upload-button").addEventListener("click", function() {
        showLoader();
    });

    function showLoader() {
        document.getElementById("main").style.display = "none";
        document.getElementById("loader").style.display = "block";

        setTimeout(function() {
            document.getElementById("loader").style.display = "none";
            document.getElementById("main").style.display = "block";
        }, 6000);
    }

 
    var chartData = {
        labels: {{chart_data.labels|safe}},
        datasets: [{
            label: 'Number of Violations',
            data:  {{chart_data.data|safe}},
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    };

    var ctx = document.getElementById('chart1').getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'doughnut',
        data: chartData,
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                y: {
                    beginAtZero: true
                }
            },
            title: {
                    display: true,
                    text: 'Distribution of Violations by Metamorphic Rule'
                }

        }
    });

    var chartData2 = {
        labels: {{chart_data2.labels|safe}} ,
        datasets: [{
            label: 'Crashed MRs',
            data: {{chart_data2.data|safe}},
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    };

    var ctx2 = document.getElementById('chart2').getContext('2d');
    let delayed;
    var myChart2 = new Chart(ctx2, {
        type: 'bar',
        data: chartData2,
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                y: {
                    beginAtZero: true
                }
            },
            animation: {
            onComplete: () => {
                delayed = true;
            },
            delay: (context) => {
                let delay = 0;
                if (context.type === 'data' && context.mode === 'default' && !delayed) {
                delay = context.dataIndex * 300 + context.datasetIndex * 100;
                }
                return delay;
            },
    },
            title: {
                    display: true,
                    text: 'Counts of Crashed Values in MR Checker Columns'
                }
        }
    });

    var chartData3 = {
        labels: {{chart_data3.labels|safe}},
        datasets: {{chart_data3.datasets|safe}} 
    };

    var ctx3 = document.getElementById('chart3').getContext('2d');
    var myChart3 = new Chart(ctx3, {
        type: 'bar',
        data: chartData3,
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'top',
                },
                title: {
                    display: true,
                    text: 'Distribution of Output Values for MR Violations'
                }
        },
    }                                                                      
})

