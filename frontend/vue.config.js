const path = require("path");

module.exports = {
  productionSourceMap: false, // 상용버전 소스맵 비활성화

  publicPath: "/static/",
  outputDir: path.resolve(__dirname, "../static"),
  chainWebpack: (config) => {
    if (process.env.NODE_ENV === "production") {
      config.plugin("html").tap((args) => {
        args[0].filename = path.resolve("../templates/index.html");
        return args;
      });
    }
  },
};
