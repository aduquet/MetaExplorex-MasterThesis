<template>
  <div>
    <h1>MetaExploreX</h1>
    <router-view />
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
     <router-link :to="{ path: '/fileupload', query: { numMRs, fileType } }">
      <button type="submit" class="btn btn-primary pt-3" id="upload-button">Next</button>
    </router-link>
    </form>
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
    };
  },
  methods: {
    submitForm() {
      axios.post('http://127.0.0.1:8000/process_chart_data/', {
      num_mrs: this.numMRs,
      file_type: this.fileType,
    })
      .then(response => {
        this.$router.push({ path: '/fileupload', query: { numMRs: this.numMRs, fileType: this.fileType } });
        console.log(response.data.message);
      })
      .catch(error => {
        console.error(error);
      });
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
    transform: translate(-50%, 30%);
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
</style>