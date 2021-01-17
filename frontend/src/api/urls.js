// const config = {
//   mode : "dev"
// }

const SERVER = "http://127.0.0.1:5000/";
// const ROOT_PATH = "api/";

export const URLS = {
  file: {
    upload: SERVER + "file/upload",
  },
  deeplearning: {
    imgClassificationByCNN: SERVER + "dl/imgClassificationByCNN",
  },
};

export default URLS;
