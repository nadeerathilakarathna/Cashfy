google.charts.load("current", { packages: ["corechart"] });
google.charts.setOnLoadCallback(drawChart);


function drawChart() {
    var data = google.visualization.arrayToDataTable([
        ['Task', 'Price'],
        ['Eating', 1500],
        ['Education', 300],
        ['Transport', 0],
        ['Others', 150],
    ]);

    var options = {

        pieHole: 0.5,
        legend: {
            position: 'labeled',
            textStyle: { color: 'black' } // Set text color for legend
        },
        pieSliceText: 'value',
        backgroundColor: {
            fill: 'transparent',   // Background fill color
            // Background stroke color
        },
        chartArea: { height: '100%', width: '100%' },
    };

    var chart = new google.visualization.PieChart(document.getElementById('donutchart'));
    chart.draw(data, options);
}