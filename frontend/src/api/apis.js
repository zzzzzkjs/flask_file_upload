import Vue from "vue";
import { URLS } from "@/api/urls.js";

const Apis = {
  async fileUpload(files, callBackFunction) {
    console.log("apis fileUpload!");
    const { data } = await Vue.axios.post(URLS.file.upload, files, {
      headers: { "Content-Type": "multipart/form-data" },
    });
    console.log("@@@@@@@@@@@")
    return callBackFunction(data);
  },
};

export default Apis;
