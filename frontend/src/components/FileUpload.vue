<template>
  <div>
    <router-view />
    <h1>MetaExploreX</h1>
    <div id="loader" class="loader"></div>
    <div v-for="message in messages" :key="message.id" class="alert" :class="'alert-' + message.tags">
      <span class="close" @click="dismissAlert(message)">&times;</span>
      {{ message.text }}
    </div>

    <div class="main" id="main">
      <form @submit.prevent="submitForm" enctype="multipart/form-data" id="upload-form" ref="uploadForm">
        <!-- <input type="hidden" name="csrfmiddlewaretoken" :value="csrfToken"> -->
        <label for="file">Choose Log file</label>
        <input type="file" name="file" id="file" accept=".csv" @change="onFileChange">
        <router-link :to="{ path: '/dashboard', query: { selectedFile: 'C:/Users/Murad/Desktop/Django_apps/metaexplorex/' + selectedFile } }">
          <button type="submit" id="upload-button" @click="submitForm">Upload and Process</button>
        </router-link>

      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  data() {
    return {
      selectedFile: null,
      numMRs: this.$route.query.numMRs,
      fileType: this.$route.query.fileType,
    };
},

  methods: {
    submitForm() {
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
      // Navigate to the new route here if needed
      this.$router.push({ path: '/dashboard', query: { selectedFile: this.selectedFile } });
    })
    .catch(error => {
      console.error(error);
    });
},
    onFileChange(event) {
      this.selectedFile = event.target.files[0].name;
  },
  },
  created() {
    console.log("Values: ", this.numMRs, this.fileType, this.selectedFile);
    this.numMRs = this.$route.params.numMRs;
    this.fileType = this.$route.params.fileType;
    this.selectedFile = this.$route.query.selectedFile;
  },
};
</script>

<style scoped>
h1 {
    text-align: center;
    margin: 20px 0;
    color: #333;
    font-family: Georgia, 'Times New Roman', Times, serif;
}

form {
    max-width: 400px;
    padding: 20px;
    background-color: #fff;
    border: 1px solid #ccc;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    border-radius: 5px;
    margin-left: 20px;
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
}

button[type="submit"] {
    background-color: #007BFF;
    color: #fff;
    border: none;
    padding: 10px 20px;
    margin-top: 10px;
    cursor: pointer;
    border-radius: 3px;
}

button[type="submit"]:hover {
    background-color: #0056b3;
}

p {
    margin-top: 20px;
    color: #333;
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