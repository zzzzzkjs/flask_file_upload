<template>
  <div id="imageClassification">
    <form @submit.prevent="imgClassificationByCNN()">
      <input type="file" multiple ref="file" @change="onFileChange($event)" />
      <input type="submit" style="margin-bottom: 20px" value="이미지 분석" />
    </form>
  </div>
</template>

<script>
export default {
  name: "ImageClassification",
  data() {
    return {
      data: "",
    };
  },
  methods: {
    onFileChange(e) {
      console.log(e);
      var files = e.target.files || e.dataTransfer.files;
      if (!files.length) return;
      console.log("==onFileChange==");
    },
    imgClassificationByCNN() {
      let formData = new FormData();

      for (var i = 0; i < this.$refs.file.files.length; i++) {
        let file = this.$refs.file.files[i];
        formData.append("file", file);
      }

      this.$dispatch("imgClassificationByCNN", formData).then((res) => {
        console.log(res);
      });
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
