<template>
  <div>
    <h1>MetaExploreX</h1>
    <router-view />
    <!-- <div v-if="!fileSelected"> -->
      <form @submit.prevent="submitForm" class="analysis-options" id="upload-form">
        <div>
          <label>Choose your log file type!</label>
          <select v-model="fileType" class="form-control" required>
            <option disabled value="">Choose file type!</option>
            <option value="single">All MRs in a single file</option>
            <option value="multiple">All MRs in multiple files</option>
          </select>
        </div>
        <br>
        <label>How many MRs will be in the log file?</label>
        <input v-model="numMRs" type="number" placeholder="Enter the number of MRs" class="form-control" required>
        <br>
          <label for="file">Choose Log file</label>
          <input type="file" name="file" id="file" accept=".csv" @change="onFileChange">
          <router-link :to="{ path: '/dashboard', query: { numMRs: this.numMRs, fileType: this.fileType, selectedFile: this.selectedFile } }">
            <button type="submit" class="btn btn-primary float-right" id="upload-button">Proceed</button>
          </router-link>
      </form>
    <div id="loader" class="loader" v-show="loading"></div>
    <div v-for="message in messages" :key="message.id" class="alert" :class="'alert-' + message.tags">
      <span class="close" @click="dismissAlert(message)">&times;</span>
      {{ message.text }}
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  data() {
    return {
      name: 'HomePage',
      fileType: '',
      numMRs: null,
      selectedFile: null,
      loading: false,
      fileSelected: false,
    };
  },
  methods: {
   submitForm() {
    if (!this.fileSelected) {
        this.fileSelected = true;
    } else {
        this.loading = true;
        const formData = new FormData();
        formData.append('file', this.selectedFile);
        formData.append('num_mrs', this.numMRs);
        formData.append('file_type', this.fileType);
        axios.post('http://127.0.0.1:8000/process_chart_data/', formData, {
            headers: {
                'Content-Type': 'multipart/form-data',
            },
        })
        .then(response => {
            console.log(response.data.message);
            this.loading = false;
            // Programmatic navigation with query parameters
            this.$router.push({ 
                path: '/dashboard', 
                query: { 
                    numMRs: this.numMRs, 
                    fileType: this.fileType, 
                    selectedFile: this.selectedFile.name // Assuming you want to send the file name
                } 
            });
        })
        .catch(error => {
            console.error(error);
            this.loading = false;
        });
    }
},
    onFileChange(event) {
      this.selectedFile = event.target.files[0];
    },
  },
};
</script>

<style>
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f7f7f7;
    /* display: flex; */
    /* justify-content: center; */
    align-items: center;
    min-height: 100vh;
}

.loader {
    position: absolute;
    left: 50%;
    top: 50%;
    z-index: 1;
    width: 120px;
    height: 120px;
    margin: -76px 0 0 -76px;
    border: 16px solid #f3f3f3;
    border-radius: 50%;
    border-top: 16px solid #3498db;
    -webkit-animation: spin 2s linear infinite;
    animation: spin 2s linear infinite;
    display: none;
    }

@-webkit-keyframes spin {
0% { -webkit-transform: rotate(0deg); }
100% { -webkit-transform: rotate(360deg); }  
}

@keyframes spin {
0% { transform: rotate(0deg); }
100% { transform: rotate(360deg); }
}

h1{
    text-align: center;
    font-family: Georgia, 'Times New Roman', Times, serif;
}

.analysis-options {
    display: flex;
    flex-direction: column;
    padding: 20px;
    background-color: #fff;
    border: 1px solid #ccc;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    border-radius: 5px;
    width: 40%;
    position: relative;
    top: 50%;
    left: 50%;
    transform: translate(-50%, 50%);
}

.analysis-options button {
    margin-top: 20px;
    width: 30%;
    text-align: center;
}

.analysis-options label {
    position: relative;
    cursor: pointer;
    font-size: 14px;
    font-family: Georgia, 'Times New Roman', Times, serif;
}
label {
    display: block;
    margin-bottom: 10px;
}

input[type="file"] {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 3px;
    background-color: #fff;
    border: 1px solid #ccc;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    border-radius: 5px;
}


img {
    width: 100%;
    height: 100%;
    display: block;
    margin-top: 20px;
}

.alert {
    padding: 15px;
    margin-bottom: 20px;
    border: 1px solid transparent;
    border-radius: 4px;
    width: 30%;
}

.alert-success {
    background-color: #d4edda;
    border-color: #c3e6cb;
    color: #155724;
}

.alert-info {
    background-color: #cce5ff;
    border-color: #b8daff;
    color: #004085;
}

.alert-warning {
    background-color: #fff3cd;
    border-color: #ffeeba;
    color: #856404;
}

.alert-error {
    background-color: #f8d7da;
    border-color: #f5c6cb;
    color: #721c24;
}

.close {
    float: right;
    font-size: 20px;
    font-weight: bold;
    line-height: 1;
    color: #000;
    text-shadow: 0 1px 0 #fff;
    opacity: .5;
}

.close:hover {
    color: #000;
    text-decoration: none;
    opacity: .75;
}

.alert p {
    margin: 0;
}

.custom-alert {
    background-color: #ffcccc;
    border-color: #ff9999;
    color: #ff0000;
}
.main {
    display: flex;
    justify-content: center;
    align-items: center;
    }
</style>