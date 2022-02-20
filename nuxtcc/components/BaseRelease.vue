<template>
  <div class="release">
    <img class="cover"
         v-show="isLoaded"
         :src="release.cover_resized"
         :alt="release.title"
         @load="onImgLoad">
    <div class="skelet__load cover__load" v-if="!isLoaded"></div>
    <div class="release__info" v-show="release.title">
      <h3 class="name">{{ release.title }}</h3>
      <p class="artist">{{ release.name }}</p>
    </div>
    <div class="release__info" v-if="!release.title">
      <div class="skelet__load name__load"></div>
      <div class="skelet__load artist__load"></div>
    </div>
  </div>
</template>


<script>
export default {
  name: 'base-release',
  data() {
    return {
      isLoaded: false,
    };
  },
  props: {
    release: {
      type: Object,
      required: true,
    },
  },
  methods: {
    onImgLoad() {
      this.isLoaded = true;
    },
  },
};
</script>


<style scoped>
.release {
  margin-top: 30px;
  width: 100%;
}
.cover, .cover__load{
  width: 326px;
  height: 326px;

  border-radius: 20px;
}
.release__info {
  margin-top: 30px;
  text-align: center;
}
.name {
  font-family: Nunito-SemiBold, sans-serif;
  font-size: 24px;

  color: #fcfcfc;
}
.name__load {
  height: 24px;
  width: 75%;
  margin: 0 auto;
}
.artist {
  font-family: Nunito-Regular, sans-serif;
  margin-top: 8px;

  color: #999;
}
.artist__load {
  height: 16px;
  width: 50%;
  margin: 8px auto 0 auto;
}
.name__load, .artist__load {
  border-radius: 4px;
}

</style>
