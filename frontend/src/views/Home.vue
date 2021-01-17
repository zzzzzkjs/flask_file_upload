<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png" />
    <FileUpload></FileUpload>
    <ImageClassification></ImageClassification>
  </div>
</template>

<script>
import FileUpload from "../components/FileUpload.vue";
import ImageClassification from "../components/ImageClassification.vue";

export default {
  name: "Home",
  components: {
    FileUpload,
    ImageClassification,
  },
};
</script>
