import axios from 'axios';
import Chart from 'chart.js/auto';

export default {
  data() {
    return {
      currentView: 'dashboard', 
      numberOfRows: 0,
      numberOfViolatedRows: 0,
      numberOfNotViolatedRows: 0,
      numberOfCrashedRows: 0,
      showFirstPopup: false,
      showSecondPopup: false,
      showColumnPopup: false,
      isViolated: "Both",
      randomData: [],
      columnsNames: [],
      allColumns: [],
      selectedColumns: [],
      currentOffset: 0,
      mrDescriptions: [],
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
    this.fetchInsights();
    this.fetchMRDescriptions();
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
  
  fetchInsights() {
    axios.get('http://127.0.0.1:8000/fetch_insights') 
      .then(response => {
        const insights = response.data.insights;
        console.log("Data insighst:", insights );
        this.numberOfRows = insights.total_rows;
        this.numberOfViolatedRows = insights.violated_rows;
        this.numberOfNotViolatedRows = insights.not_violated_rows;
        this.numberOfCrashedRows = insights.crashed_rows;
        this.columnsNames = insights.mr_columns;
        this.allColumns = insights.mr_columns;
        this.selectedColumns = insights.mr_columns;
        console.log("numberofRows: ", this.numberOfRows);
      })
      .catch(error => {
        console.error('Error fetching insights:', error);
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
      this.currentOffset += 5; 

      axios.get(`http://127.0.0.1:8000/fetch_random_data/?offset=${this.currentOffset}&isViolated=${this.isViolated}`)
        .then(response => {
          this.randomData = this.randomData.concat(response.data?.random_data);
        })
        .catch(error => {
          console.error('Error fetching more data:', error);
        });
    },
    onChartClick(data) {
      console.log('Chart clicked', this.isViolated);
      this.isViolated = data.isViolated;
      this.columnsNames = data.chartData?.labels;
      this.showFirstPopup = true; 
    },

    onProceedClick() {
      this.showFirstPopup = false;
      this.fetchRandomData(); 
      this.updateColumns(); 
      this.showSecondPopup = true; 
    },
    updateColumns() {
      this.columnsNames = [...this.selectedColumns];
      this.showColumnPopup = false;
    },
    fetchMRDescriptions() {
      try {
        const descriptions = this.$route.query.mrDescriptions ? (this.$route.query.mrDescriptions) : [];
        this.mrDescriptions = descriptions;
        console.log('MR descriptions fetched: ', this.mrDescriptions); 
      } catch (error) {
        console.error('Error parsing MR descriptions:', error);
        this.mrDescriptions = [];
      }
},
  }
};
