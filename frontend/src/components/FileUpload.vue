<template>
  <div class="file_upload">
    <form
      action="http://127.0.0.1:5000/file/upload"
      method="POST"
      enctype="multipart/form-data"
    >
      <input type="file" multiple name="filename[]" />
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
    uploadImages() {
      this.$dispatch("fileUpload", {}).then((res) => {
        console.log(res);
      });
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
