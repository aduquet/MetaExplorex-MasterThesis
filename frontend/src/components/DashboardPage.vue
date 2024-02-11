<template>
  <div class="page-wrapper" id="main-wrapper" data-layout="vertical" data-navbarbg="skin6" data-sidebartype="full"
    data-sidebar-position="fixed" data-header-position="fixed" @click="showSecondPopup = false, showFirstPopup = false, showColumnPopup = false">
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
              <a class="sidebar-link" href="#" aria-expanded="false" method="GET" enctype="multipart/form-data">
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
              <form action="/" class="navbar-nav flex-row ms-auto align-items-center justify-content-end" method="GET"
                enctype="multipart/form-data" id="upload-form">
                <input type="submit" class="btn" id="cancel-button" onclick="cancelUpload()" value="Back" />
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
                    <h5 class="card-title fw-semibold text-center">Distribution of Not-Crashed Values in MR Checker
                      Columns</h5>
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
                  <select id="chart-type-select3" v-model="selectedChart3Type" @change="createChart3()">
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
                    <h5 class="card-title fw-semibold text-center">Distribution of Output Values for MR Non-Violations
                    </h5>
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
  </div>
  <div v-if="showFirstPopup" class="popup">
    <div style="display: flex;">

      <div>

        <button @click="showColumnPopup = true" style="height: 50px;">MR Selection</button>
        <p>Check file type</p>
      </div>
      <button v-if="isViolated == 'Both'" @click="isViolated = 'Violated'" style="height: 50px;">Both</button>
      <button v-if="isViolated == 'Violated'" @click="isViolated = 'Not-violated'" style="height: 50px;">Violated</button>
      <button v-if="isViolated == 'Not-violated'" @click="isViolated = 'Both'" style="height: 50px;">Not-violated</button>

    </div>
    <button class="bottom-right" @click="onProceedClick">Proceed</button>
  </div>
  <div v-if="showSecondPopup" class="popup">
    <div class="table-container">

      <table>
        <tr>
          <th>
            Input Test Data
          </th>
          <th v-for="columnName in columnsNames" :key="columnName">
            {{ columnName }}_Transformed
          </th>
          <th>
            Output Test Data
          </th>
          <th v-for="columnName in columnsNames" :key="columnName">
            output_{{ columnName }}
          </th>
          <th v-for="columnName in columnsNames" :key="columnName">
            {{ columnName }}_checker
          </th>
        </tr>
        <tr v-for="(item, index) in randomData" :key="index">
          <td>
            {{ item.input_testData }}
          </td>
          <td v-for="columnName in columnsNames" :key="columnName">
            {{ item[columnName+'_Transformed'] }}
          </td>
          <td>
            {{ item.output_testInput }}
          </td>
          <td v-for="columnName in columnsNames" :key="columnName">
            {{ item['output_'+columnName] }}
          </td>
          <td v-for="columnName in columnsNames" :key="columnName">
            <span v-if="isViolated == 'Both'">
              {{ item[columnName+'_checker'] }}
            </span>
            <span v-if="isViolated == 'Violated'">
              <span v-if="item[columnName+'_checker'] == 'Violated'">

                {{ item[columnName+'_checker'] }}
              </span>
            </span>
            <span v-if="isViolated == 'Not-violated'">
              <span v-if="item[columnName+'_checker'] == 'Not-violated'">

                {{ item[columnName+'_checker'] }}
              </span>
            </span>

          </td>
         

        </tr>
      </table>

    </div>
    <button @click="loadMore">Load More</button>

  </div>
  <div v-if="showColumnPopup" class="popup">
    <div class="popup-inner">
      <button @click="showPopup = false">Close</button>
      <ul>
        <li v-for="(columnName, index) in allColumns" :key="index">
          <input type="checkbox" :id="columnName" :value="columnName" v-model="selectedColumns">
          <label :for="columnName">{{ columnName }}</label>
        </li>
      </ul>
      <button @click="updateColumns">Update</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import Chart from 'chart.js/auto';

export default {
  data() {
    return {
      showFirstPopup: false,
      showSecondPopup: false,
      showColumnPopup: false,
      isViolated: "Both",
      randomData: [],
      columnsNames: [],
      allColumns: [
        'MR1', 'MR2', 'MR3', 'MR4',
        'MR5', 'MR6', 'MR7', 'MR8'
      ],
      selectedColumns: [
        'MR1', 'MR2', 'MR3', 'MR4',
        'MR5', 'MR6', 'MR7', 'MR8'
      ],
      currentOffset: 0,
      selectedFile: this.$route.query.selectedFile,
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
            label: ['Violations', 'Non-Violations'],
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
    // this.showFirstPopup = true;
    // this.fetchRandomData();
    // this.showSecondPopup = true;
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
          onClick: () => {
            this.onChartClick({
              chartData: this.chartData1, isViolated: "Violated"
            })
          },
          // onClick: this.onChartClick(),
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
          onClick: () => {
            this.onChartClick({
              chartData: this.chartData2, isViolated: "Not-violated"
            })
          },
          // onClick: this.onChartClick(),
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
          // onClick: this.onChartClick(),

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
          onClick: () => {
            this.onChartClick({
              chartData: this.chartData4, isViolated: "Both"
            
            })
          },
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
          onClick: () => {
            this.onChartClick({
              chartData: "validation/non-validation", isViolated: 'Both'
            })
          },
          // onClick: this.onChartClick(),

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


    fetchRandomData() {
      axios.get(`http://127.0.0.1:8000/fetch_random_data/?isViolated=${this.isViolated}`)
        .then(response => {
          console.log('Random data:', response.data)
          this.randomData = response.data?.random_data || [];
        })
        .catch(error => {
          console.error('Error fetching random data:', error);
        });
    },

    loadMore() {
      // Example assumes you have a way to track which rows to fetch next, e.g., offset or page number
      this.currentOffset += 5; // Assuming 'currentOffset' keeps track of your position in the dataset

      axios.get(`http://127.0.0.1:8000/fetch_random_data/?offset=${this.currentOffset}&isViolated=${this.isViolated}`)
        .then(response => {
          // Concatenate the new rows with the existing rows
          this.randomData = this.randomData.concat(response.data?.random_data);
        })
        .catch(error => {
          console.error('Error fetching more data:', error);
        });
    },




    onChartClick(data) {
      console.log('Chart clicked', this.isViolated);
      this.isViolated = data.isViolated;
      if (data.chartData == "validation/non-validation") {
        this.columnsNames = [
          'MR1_checker', 'MR2_checker', 'MR3_checker', 'MR4_checker', 'MR5_checker', 'MR6_checker',
          'MR7_checker', 'MR8_checker'
        ];
      } else {


        this.columnsNames = data.chartData?.labels;
      }

      this.showFirstPopup = true; // Make sure you have a data property 'showFirstPopup' initialized as false
    },

    onProceedClick() {
      this.showFirstPopup = false; // Close the first popup
      this.fetchRandomData(); // Assume this method fetches random data and sets 'randomData'
      this.updateColumns(); // Update the columns
      this.showSecondPopup = true; // Make sure you have a data property 'showSecondPopup' initialized as false
    },
    updateColumns() {
      this.columnsNames = [...this.selectedColumns];
      this.showColumnPopup = false;
    }



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

.popup {
  background-color: #ffffff;
  /* Light background for better contrast */
  border-radius: 10px;
  /* Rounded corners */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1), 0 6px 20px rgba(0, 0, 0, 0.1);
  /* Soft shadow for depth */
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 80vh;
  width: 60vw;
  /* Adjusted for a more centered look */
  position: fixed;
  /* Fixed to stay in view on scroll */
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  /* Centering the popup */
  padding: 20px;
  overflow: hidden;
  /* Ensures no internal overflow */
  z-index: 1000;
  /* Ensure it's above other content */
}

.popup button,
.bottom-right {
  background-color: #007BFF;
  /* Primary button color */
  color: #ffffff;
  border: none;
  border-radius: 5px;
  padding: 10px 20px;
  margin: 10px;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.3s, color 0.3s, border-color 0.3s;
}

.popup button:hover,
.bottom-right:hover {
  background-color: #0056b3;
  /* Darker shade on hover */
  color: #ffffff;
  border: 1px solid #0056b3;
}

.table-container {
  overflow-y: auto;
  max-height: 50vh;
  /* Adjusted to take up half of the popup height */
  width: 100%;
  /* Utilize full width of the popup */
  margin-top: 20px;
  border: 1px solid #ddd;
  /* Light border for the container */
  border-radius: 5px;
  /* Consistent rounded corners */
}

.popup table {
  border-collapse: collapse;
  width: 100%;
  background-color: #f8f9fa;
  /* Slightly off-white background for the table */
}

.popup th,
.popup td {
  text-align: left;
  padding: 8px;
  border-bottom: 1px solid #ddd;
  /* Light borders for table rows */
}

.popup th {
  background-color: #007BFF;
  /* Header background */
  color: white;
  /* Light text for headers */
  font-weight: normal;
}

/* Scrollbar styles */
.table-container::-webkit-scrollbar {
  width: 5px;
  /* Scrollbar width */
}

.table-container::-webkit-scrollbar-track {
  background: #f1f1f1;
  /* Track color */
}

.table-container::-webkit-scrollbar-thumb {
  background: #888;
  /* Scrollbar handle color */
}

.table-container::-webkit-scrollbar-thumb:hover {
  background: #555;
  /* Handle hover color */
}</style>
