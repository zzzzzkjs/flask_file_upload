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
  props: {
    msg: String,
  },
  methods: {
    uploadImages() {
      this.$dispatch("comboData_names", {}).then((res) => {
        console.log(res);
        for (let i in res.data) {
          this.type_of_barometer.push({
            name: res.data[i].data_name,
            description: res.data[i].descrition,
          });
        }
      });
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
