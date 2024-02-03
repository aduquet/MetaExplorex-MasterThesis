<template>
  <div class="page-wrapper" id="main-wrapper" data-layout="vertical" data-navbarbg="skin6" data-sidebartype="full"
       data-sidebar-position="fixed" data-header-position="fixed">
        <aside class="left-sidebar">
      <div>
        <div class="brand-logo d-flex align-items-center justify-content-between">
          <a href="#" class="text-nowrap">
            <!-- <h4>MetaExploreX</h4> -->
            <img src="frontend\src\assets\logo.png" alt="" width="220px" height="80px">
          </a>
          <div class="close-btn d-xl-none d-block sidebartoggler cursor-pointer" id="sidebarCollapse">
            <i class="ti ti-x fs-8"></i>
          </div>
        </div>
        <nav class="sidebar-nav scroll-sidebar" data-simplebar="">
          <ul id="sidebarnav">
            <li class="sidebar-item">
              <a class="sidebar-link" href="#" aria-expanded="false" method="GET" enctype="multipart/form-data" >
                <span>
                  <i class="fa-solid fa-chart-simple"></i>
                </span>
                <span class="hide-menu">Dashboard</span>
              </a>
            </li>
            <br>
            <li class="sidebar-item">
              <a class="sidebar-link" href="" aria-expanded="false">
                <span>
                  <i class="fa-solid fa-chart-line"></i>
                </span>
                <span class="hide-menu">Insights</span>
              </a>
            </li>
            <br>
            <li class="sidebar-item">
              <form action="" class="" method="GET" enctype="multipart/form-data" id="upload-form">
                <a class="sidebar-link" id="cancel-button" onclick="cancelUpload()" value="Back" aria-expanded="false">
                  <span>
                    <i class="fa-solid fa-backward"></i>
                  </span>
                  <span class="hide-menu">Back</span>
                </a>
              </form>
            </li>
          </ul>
        </nav>
      </div>
    </aside>
    <div class="body-wrapper">
      <header class="app-header">
        <nav class="navbar navbar-expand-lg navbar-light">
          <ul class="navbar-nav">
            <li class="nav-item d-block d-xl-none">
              <a class="nav-link sidebartoggler nav-icon-hover" id="headerCollapse" href="javascript:void(0)">
                <i class="ti ti-menu-2"></i>
              </a>
            </li>
          </ul>
          <div class="navbar-collapse justify-content-end px-0" id="navbarNav">
            <div id="cancel-section">
                <form action="/" class="navbar-nav flex-row ms-auto align-items-center justify-content-end" method="GET" enctype="multipart/form-data" id="upload-form">
                    <input type="submit" class="btn" id="cancel-button" onclick="cancelUpload()" value="Back"/>
                </form>
            </div>
          </div>
        </nav>
      </header>
      <div class="container-fluid">
        <div class="row">
            <div class="col-lg-8 d-flex align-items-strech">
                <div class="card w-100">
                  <div class="card-body chart-container">
                    <div class="d-sm-flex d-block align-items-center justify-content-between mb-9">
                      <div class="mb-3 mb-sm-0">
                        <h5 class="card-title fw-semibold text-center">Distribution of Not-Crashed Values in MR Checker Columns</h5>
                      </div>
                    </div>
                    <div class="chart-type-dropdown">
                            <select id="chart-type-select4" v-model="selectedChart4Type" @change="createChart4()">
                                <option value="bar">Bar Chart</option>
                                <option value="doughnut">Doughnut Chart</option>
                                <option value="line">Line Chart</option>
                                <option value="pie">Pie Chart</option>
                            </select>
                    </div>
                    <div class="chart-container" id="" style="height: 400px!important;">
                        <canvas ref="myChart4" id="chart4"></canvas>
                    </div>
                  </div>
                </div>
                
              </div>
          <div class="col-lg-4">
            <div class="row">
              <div class="col-lg-12">
                <div class="card overflow-hidden">
                  <div class="card-body p-4">
                    <h5 class="card-title  fw-semibold">MR Violations</h5>
                    <div class="row align-items-center">
                      <div class="">
                        <div class="chart-container">
                            <canvas ref="myChart7" id="chart7"></canvas>
                        </div>
                      </div>
                     
                      <div class="">
                        <h4 class="fw-semibold mb-3" id="total_rows" ref="totalRows"> </h4>
                        <div class="d-flex align-items-center ">
                            <h6 id="violated_rows" class="fw-semibold" ref="violatedRows"></h6>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="row">
              <div class="col-lg-6 d-flex align-items-strech">
                <div class="card w-100">
                  <div class="card-body chart-container">
                    <div class="d-sm-flex d-block align-items-center justify-content-between mb-9">
                      <div class="mb-3 mb-sm-0">
                        <h5 class="card-title fw-semibold text-center">Distribution of Violations by Metamorphic Rule</h5>
                        <div class="chart-type-dropdown">
                            <select id="chart-type-select1" v-model="selectedChart1Type" @change="createChart1()">
                                <option value="doughnut">Doughnut Chart</option>
                                <option value="bar">Bar Chart</option>
                                <option value="line">Line Chart</option>
                                <option value="pie">Pie Chart</option>
                            </select>
                        </div>
                      </div>
                    </div>
                    
                    <div class="chart-container" id="" width="100%" height="100%">
                        <canvas ref="myChart1" id="chart1"></canvas>
                    </div>
                  </div>
                </div>
              </div>

              <div class="col-lg-6 d-flex align-items-strech">
                <div class="card w-100">
                  <div class="card-body chart-container">
                    <div class="d-sm-flex d-block align-items-center justify-content-between mb-9">
                      <div class="mb-3 mb-sm-0">
                        <h5 class="card-title fw-semibold text-center">Distribution of Non-Violations by Metamorphic Rule</h5>
                        <div class="chart-type-dropdown">
                        <select id="chart-type-select2" v-model="selectedChart2Type" @change="createChart2()">

                            <option value="doughnut">Doughnut Chart</option>
                            <option value="bar">Bar Chart</option>
                            <option value="line">Line Chart</option>
                            <option value="pie">Pie Chart</option>
                        </select>
                    </div>
                        </div>
                    </div>
                    <div class="chart-container" id="">
                      <canvas ref="myChart2" id="chart2"></canvas>                    
                    </div>
                  </div>
                </div>
              </div>

              <div class="col-lg-12 d-flex align-items-strech">
                <div class="card w-100">
                  <div class="card-body chart-container">
                    <div class="d-sm-flex d-block align-items-center justify-content-between mb-9">
                      <div class="mb-3 mb-sm-0">
                        <h5 class="card-title fw-semibold text-center">Distribution Crashed Values in MR Checker Columns</h5>
                      </div>
                    </div>
                    <div class="chart-type-dropdown">
                        <select id="chart-type-select3"  v-model="selectedChart3Type" @change="createChart3()">
                            <option value="doughnut">Doughnut Chart</option>
                            <option value="bar">Bar Chart</option>
                            <option value="line">Line Chart</option>
                            <option value="pie">Pie Chart</option>
                        </select>
                    </div>
                    <div class="chart-container" id="" style="height: 400px!important;">
                        <canvas ref="myChart3" id="chart3"></canvas>
                    </div>
                  </div>
                </div>
              </div>

              <div class="col-lg-12 d-flex align-items-strech">
                <div class="card w-100">
                  <div class="card-body chart-container">
                    <div class="d-sm-flex d-block align-items-center justify-content-between mb-9">
                      <div class="mb-3 mb-sm-0">
                        <h5 class="card-title fw-semibold text-center">Distribution of Output Values for MR Violations</h5>
                      </div>
                    </div>
                    <div class="chart-type-dropdown">
                        <select id="chart-type-select5" v-model="selectedChart5Type" @change="createChart5()">
                            <option value="doughnut">Doughnut Chart</option>
                            <option value="bar">Bar Chart</option>
                            <option value="line">Line Chart</option>
                            <option value="pie">Pie Chart</option>
                        </select>
                    </div>
                    <div class="chart-container" id="" style="height: 400px!important;">
                        <canvas ref="myChart5" id="chart5"></canvas>
                    </div>
                  </div>
                </div>
              </div>

              <div class="col-lg-12 d-flex align-items-strech">
                <div class="card w-100">
                  <div class="card-body chart-container">
                    <div class="d-sm-flex d-block align-items-center justify-content-between mb-9">
                      <div class="mb-3 mb-sm-0">
                        <h5 class="card-title fw-semibold text-center">Distribution of Output Values for MR Non-Violations</h5>
                      </div>
                    </div>
                    <div class="chart-type-dropdown">
                        <select id="chart-type-select6" v-model="selectedChart6Type" @change="createChart6()">
                            <option value="doughnut">Doughnut Chart</option>
                            <option value="bar">Bar Chart</option>
                            <option value="line">Line Chart</option>
                            <option value="pie">Pie Chart</option>
                        </select>
                    </div>
                    <div class="chart-container" id="" style="height: 400px!important;">
                        <canvas ref="myChart6" id="chart6"></canvas>
                    </div>
                  </div>
                </div>
              </div>
              </div>
      </div>
    </div>
    <!-- <h5>Info section</h5>
    <div id="overlay" v-show="overlayVisible"></div>
    <div id="info-box" v-show="infoBoxVisible">
      <div id="info-content">
        <h5>Info section</h5>
      </div>
    </div> -->
  </div>
</template>

<script>
import axios from 'axios';
import Chart from 'chart.js/auto';

export default {
  data() {
    return {
      
      chartData1: {
        labels: [],
        datasets: [
          {
            label: 'Number of Violations',
            data: [],
            backgroundColor: [],
            borderWidth: 1,
          },
        ],
      },
      chartData2: {
        labels: [],
        datasets: [
          {
            label: 'Number of Non-Violations',
            data: [],
            backgroundColor: [],
            borderWidth: 1,
          },
        ],
      },
      chartData3: {
        labels: [],
        datasets: [
          {
            label: 'Crashed MRs',
            data: [],
            backgroundColor: [],
            borderWidth: 1,
          },
        ],
      },
      chartData4: {
        labels: [],
        datasets: [
          {
            label: 'Non-Crashed MRs',
            data: [],
            backgroundColor: [],
            borderWidth: 1,
          },
        ],
      },
      chartData5: {
        labels: [],
        datasets: [
          {
            // label: 'Number of Violations',
            data: [],
            backgroundColor: [],
            borderWidth: 1,
          },
        ],
      },
      chartData6: {
        labels: [],
        datasets: [
          {
            // label: 'Number of Violations',
            data: [],
            backgroundColor: [],
            borderWidth: 1,
          },
        ],
      },
      chartData7: {
        labels: [],
        datasets: [
          {
            label: ['Violations','Non-Violations'],
            data: [],
            backgroundColor: [],
            borderWidth: 1,
          },
        ],
      },

      myChart1: null,
      myChart2: null,
      myChart3: null,
      myChart4: null,
      myChart5: null,
      myChart6: null,
      myChart7: null,

      selectedChart1Type: 'doughnut',
      selectedChart2Type: 'doughnut',
      selectedChart3Type: 'bar',
      selectedChart4Type: 'bar',
      selectedChart5Type: 'bar',
      selectedChart6Type: 'bar',
      selectedChart7Type: 'doughnut',
    };
  },
mounted() {
  this.createChart1();
  this.createChart2();
  this.createChart3();
  this.createChart4();
  this.createChart5();
  this.createChart6();
  this.createChart7();
  this.fetchChart1Data();
  this.fetchChart2Data();
  this.fetchChart3Data();
  this.fetchChart4Data();
  this.fetchChart5Data();
  this.fetchChart6Data();
  this.fetchChart7Data();
},
  methods: {
    generateRandomColors(numColors) {
      var colors = [];
      for (var i = 0; i < numColors; i++) {
        var randomColor =
          'rgba(' +
          Math.floor(Math.random() * 256) +
          ',' +
          Math.floor(Math.random() * 256) +
          ',' +
          Math.floor(Math.random() * 256) +
          ', 0.8)';
        colors.push(randomColor);
      }
      return colors;
    },
    async fetchChart1Data() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/chart1/');
        const data = response.data;
        this.chartData1.labels = data.labels;
        this.chartData1.datasets[0].data = data.data;
        this.chartData1.datasets[0].backgroundColor = this.generateRandomColors(data.labels.length);
        this.createChart1();
      } catch (error) {
        console.error('Error fetching chart data:', error);
      }
    },

    async fetchChart2Data() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/chart2/');
        const data = response.data;
        this.chartData2.labels = data.labels;
        this.chartData2.datasets[0].data = data.data;
        this.chartData2.datasets[0].backgroundColor = this.generateRandomColors(data.labels.length);
        this.createChart2();
      } catch (error) {
        console.error('Error fetching chart data:', error);
      }
    },

    async fetchChart3Data() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/chart3/');
        const data = response.data;
        this.chartData3.labels = data.labels;
        this.chartData3.datasets[0].data = data.data;
        this.chartData3.datasets[0].backgroundColor = this.generateRandomColors(data.labels.length);
        this.createChart3();
      } catch (error) {
        console.error('Error fetching chart data:', error);
      }
    },

    async fetchChart4Data() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/chart4/');
        const data = response.data;
        this.chartData4.labels = data.labels;
        this.chartData4.datasets[0].data = data.data;
        this.chartData4.datasets[0].backgroundColor = this.generateRandomColors(data.labels.length);
        this.createChart4();
      } catch (error) {
        console.error('Error fetching chart data:', error);
      }
    },

    async fetchChart5Data() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/chart5/');
        const data = response.data;
        this.chartData5.labels = data.labels;
        this.chartData5.datasets[0].data = data.data;
        this.chartData5.datasets[0].backgroundColor = this.generateRandomColors(data.labels.length);
        this.createChart5();
      } catch (error) {
        console.error('Error fetching chart data:', error);
      }
    },

    async fetchChart6Data() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/chart6/');
        const data = response.data;
        this.chartData6.labels = data.labels;
        this.chartData6.datasets[0].data = data.data;
        this.chartData6.datasets[0].backgroundColor = this.generateRandomColors(data.labels.length);
        this.createChart6();
      } catch (error) {
        console.error('Error fetching chart data:', error);
      }
    },

 async fetchChart7Data() {
  try {
    const response = await axios.get('http://127.0.0.1:8000/chart7/');
    const data = response.data;

    // Calculate percentages
    const totalViolations = data.data[0];
    const totalNonViolations = data.data[1];
    const totalData = totalViolations + totalNonViolations;
    const percentViolations = (totalViolations / totalData) * 100;
    const percentNonViolations = 100 - percentViolations;

    // Update elements in the Vue component
    this.$refs.totalRows.innerText = "Total data: " + data.total_data_points;
    this.$refs.violatedRows.innerText = Math.round(percentViolations) + "% of data are violated.";

    // Create chart data
    this.chartData7.labels = ['Violations', 'Non-violations'];
    this.chartData7.datasets[0].data = [percentViolations, percentNonViolations];
    this.chartData7.datasets[0].backgroundColor = ['rgba(93, 125, 255, 0.5)', 'rgb(73, 135, 255)'];
    this.createChart7();
  } catch (error) {
    console.error('Error fetching chart data:', error);
  }
},



    
createChart1() {
  const ctx = this.$refs.myChart1.getContext('2d');
  if (this.myChart1) {
    this.myChart1.destroy();
  }
  
  const chartType = this.selectedChart1Type ? this.selectedChart1Type : 'doughnut';

  this.myChart1 = new Chart(ctx, {
    type: chartType,
    data: this.chartData1,
    options: {
      responsive: true,
      maintainAspectRatio: false,
      cutout: 50,
      scales: {
        y: {
          beginAtZero: true,
        },
      },
    },
  });
},


createChart2() {
  const ctx = this.$refs.myChart2.getContext('2d');
  if (this.myChart2) {
    this.myChart2.destroy();
  }
  const chartType = this.selectedChart2Type;
  this.myChart2 = new Chart(ctx, {
    type: chartType,
    data: this.chartData2,
    options: {
      responsive: true,
      maintainAspectRatio: false,
      scales: {
        y: {
          beginAtZero: true,
        },
      },
    },
  });
},

createChart3() {
  const ctx = this.$refs.myChart3.getContext('2d');
  let delayed;
  if (this.myChart3) {
    this.myChart3.destroy();
  }
  const chartType = this.selectedChart3Type;
  this.myChart3 = new Chart(ctx, {
    type: chartType,
    data: this.chartData3,
    options: {
    responsive: true,
    maintainAspectRatio: false,
    cutout: '75%',
    scales: {
        y: {
            beginAtZero: true
        }
    },
    elements: {
        arc: {
          borderWidth: 1,
          barThickness: 20, 
        },
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
}
  });
},

createChart4() {
  const ctx = this.$refs.myChart4.getContext('2d');
  let delayed;
  if (this.myChart4) {
    this.myChart4.destroy();
  }
  const chartType = this.selectedChart4Type;
  this.myChart4 = new Chart(ctx, {
    type: chartType,
    data: this.chartData4,
    options: {
    responsive: true,
    maintainAspectRatio: false,
    cutout: 10,
    scales: {
      y: {
        beginAtZero: true,
      },
    },
    legend: {
      display: true,
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
  },
  });
},

createChart5() {
  const ctx = this.$refs.myChart5.getContext('2d');
  if (this.myChart5) {
    this.myChart5.destroy();
  }
  const chartType = this.selectedChart5Type;
  this.myChart5 = new Chart(ctx, {
    type: chartType,
    data: this.chartData5,
    options: {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
        legend: {
            position: 'top',
        },
      },
    },
  });
},

createChart6() {
  const ctx = this.$refs.myChart6.getContext('2d');
  if (this.myChart6) {
    this.myChart6.destroy();
  }
  const chartType = this.selectedChart6Type;
  this.myChart6 = new Chart(ctx, {
    type: chartType,
    data: this.chartData6,
    options: {
    responsive: true,
    maintainAspectRatio: false,
    cutout: 85, 
    plugins: {
        legend: {
            position: 'top',
        },
      },
    }   
  });
},

createChart7() {
  const ctx = this.$refs.myChart7.getContext('2d');
  if (this.myChart7) {
    this.myChart7.destroy();
  }
  this.myChart7 = new Chart(ctx, {
    type: this.selectedChart7Type,
    data: this.chartData7,
    options: {
        responsive: true,
        maintainAspectRatio: false,
        cutout: 85, 
        plugins: {
            legend: {
                display: false
            }
        }
    },
  });
},




}
};
</script>

<style scoped>
  @import url('@/assets/css/styles.min.css');
  @import url('https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css');
  canvas {
    width: 100%;
    height: 400px;
}
.chart-container {
    width: 100%;
    height: auto 400px;
}

</style>
