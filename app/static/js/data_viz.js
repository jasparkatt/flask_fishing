
    function mycntyFunc() {
        return county
    }
    
    function mytotalFunc() {
        return total
    }


// Bar chart
new Chart(document.getElementById("myCanvas"), {
    type: 'bar',
    data: {
      labels: mycntyFunc(),
      datasets: [
        {
          label: "County Name",
          backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850"],
          data: mytotalFunc()
        }
      ]
    },
    options: {
      legend: { display: false },
      title: {
        display: true,
        text: 'Most Visited County by Total Spots'
      }
    }
});