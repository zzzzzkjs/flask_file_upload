<template>
  <div id="fileUpload">
    <form @submit.prevent="uploadImages()">
      <input type="file" multiple ref="file" @change="onFileChange($event)" />
      <input type="submit" />
    </form>
  </div>
</template>

<script>
export default {
  name: "FileUpload",
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
    uploadImages() {
      let formData = new FormData();

      for (var i = 0; i < this.$refs.file.files.length; i++) {
        let file = this.$refs.file.files[i];
        formData.append("file", file);
      }

      this.$dispatch("fileUpload", formData).then((res) => {
        console.log(res);
      });
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
