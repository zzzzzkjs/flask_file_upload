<template>
  <div class="file_upload">
    <form
      action="http://localhost:9080/fileUpload"
      method="POST"
      enctype="multipart/form-data"
    >
      <input type="file" name="file" />
      <input type="submit" />
    </form>
  </div>
</template>

<script>
export default {
  name: "FileUpload",
  props: {
    msg: String,
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
