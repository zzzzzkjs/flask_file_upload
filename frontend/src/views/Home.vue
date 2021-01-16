<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png" />
    <FileUpload></FileUpload>
  </div>
</template>

<script>
import FileUpload from "../components/FileUpload.vue";

export default {
  name: "Home",
  components: {
    FileUpload,
  },
};
</script>
