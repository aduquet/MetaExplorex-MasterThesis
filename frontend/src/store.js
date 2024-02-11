import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    numMRs: null,
    fileType: '',
    selectedFile: null,
  },
  mutations: {
    setNumMRs(state, numMRs) {
      state.numMRs = numMRs;
    },
    setFileType(state, fileType) {
      state.fileType = fileType;
    },
    setSelectedFile(state, file) {
      state.selectedFile = file;
    },
  },
  actions: {
    updateNumMRs({ commit }, numMRs) {
      commit('setNumMRs', numMRs);
    },
    updateFileType({ commit }, fileType) {
      commit('setFileType', fileType);
    },
    updateSelectedFile({ commit }, file) {
      commit('setSelectedFile', file);
    },
  },
});
