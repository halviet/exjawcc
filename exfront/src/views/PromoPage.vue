<template>
  <div class="promo__wrapper">
    <div class="share__wrapper">
      <share-link @popupCopied="triggerPopup" />
    </div>

    <base-release :release="release"/>

    <platform-list :link="link"/>

    <shared-msg v-if="showPopup" />
  </div>
</template>

<script>
import axios from 'axios';

import ShareLink from '../components/ShareLink';
import BaseRelease from '../components/BaseRelease';
import PlatformLink from '../components/PlatformLink';
import PlatformList from '../components/PlatformList';
import SharedMsg from '../components/SharedMsg';

export default {
  components: { SharedMsg, PlatformList, PlatformLink, BaseRelease, ShareLink },
  data() {
    return {
      release: {
        cover: '',
        cover_resized: '',
        id: '',
        name: '',
        title: '',
        url: '',
        user: '',
        version: '',
      },
      link: [],
      url: (window.location.pathname).substring(1).toLowerCase(),
      showPopup: false,
    };
  },
  methods: {
    async fetchRelease() {
      try {
        const rel = await axios.get(`http://127.0.0.1:8000/api/release/${this.url}`);
        this.release = rel.data;

        const lin = await axios.get(`http://127.0.0.1:8000/api/link/all?release=${this.release.id}`);
        this.link = lin.data;
      } catch (e) {
        throw e;
      }
    },
    triggerPopup() {
      this.showPopup = true;
      setTimeout(() => {
        this.showPopup = false;
      }, 3000);
    },
  },
  mounted() {
    this.fetchRelease();
  },
};
</script>

<style scoped>
.promo__wrapper {
  margin: 25px auto;
  width: 326px;
}

.share__wrapper {
  width: 100%;
  display: flex;
  justify-content: flex-end;
}
</style>
