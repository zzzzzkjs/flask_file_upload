import Vue from "vue";
import Vuex from "vuex";
import apis from "@/api/apis.js";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {},
  mutations: {},
  actions: {
    fileUpload(commit, params) {
      console.log("actions fileUpload");
      return apis.fileUpload(params, (res) => {
        return res;
      });
    },
    imgClassificationByCNN(commit, params) {
      console.log("actions imgClassificationByCNN");
      return apis.imgClassificationByCNN(params, (res) => {
        return res;
      });
    },
  },
  modules: {},
});
