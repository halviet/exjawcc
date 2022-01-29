<template>
  <div class="release">
    <img class="cover" :src="release.cover_resized" :alt="release.title">
    <div class="release__info">
      <h3 class="name">{{ release.title }}</h3>
      <p class="artist">{{ release.name }}</p>
    </div>
  </div>
</template>


<script>
export default {
  name: 'base-release',
  props: {
    release: {
      type: Object,
      required: true,
    },
  },
};
</script>


<style scoped>
.release {
  margin-top: 30px;
  width: 100%;
}
.cover {
  width: 326px;
  height: 326px;

  border-radius: 20px;
}
.release__info {
  margin-top: 30px;
}
.name {
  font-family: Nunito-SemiBold, sans-serif;
  font-size: 24px;

  color: #fcfcfc;
}
.artist {
  margin-top: 8px;

  color: #999;
}

</style>
