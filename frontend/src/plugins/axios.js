"use strict";

import Vue from "vue";
import axios from "axios";

// Full config:  https://github.com/axios/axios#request-config
let config = {
  // baseURL: process.env.baseURL || process.env.apiUrl || ""
  timeout: 30 * 1000, // Timeout - 딥러닝 api쪽이 오래걸리는경우가 있어서 30초로 걸어놈(TODO: 로딩바 추가해야될듯)
  // withCredentials: true, // Check cross-site Access-Control
  method: "post",
  headers: { "content-type": "application/json" },
};

const _axios = axios.create(config);

_axios.interceptors.request.use(
  function(config) {
    console.log("==before==", config);
    // Do something before request is sent
    return config;
  },
  function(error) {
    console.log("==error==", error);
    // Do something with request error
    return Promise.reject(error);
  }
);

// Add a response interceptor
_axios.interceptors.response.use(
  function(response) {
    // Do something with response data
    return response;
  },
  function(error) {
    // Do something with response error
    return Promise.reject(error);
  }
);

Plugin.install = function(Vue) {
  Vue.axios = _axios;
  // window.axios = _axios; // 전역으로 노출 안시키게 주석처리
  Object.defineProperties(Vue.prototype, {
    axios: {
      get() {
        return _axios;
      },
    },
    $axios: {
      get() {
        return _axios;
      },
    },
  });
};

Vue.use(Plugin);

export default Plugin;
