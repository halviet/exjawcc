<template>
  <div class="promo__wrapper">
    <div class="share__wrapper">
      <share-link @popupCopied="triggerPopup" :url="url" />
    </div>

    <base-release :release="release"/>

    <platform-list :link="link"/>

    <shared-msg v-if="showPopup" />
  </div>
</template>

<script>
// import axios from 'axios';

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
      url: this.$route.params.slug.toLowerCase(),
      showPopup: false,
    };
  },
  async fetch() {
    try {
      const rel = await this.$axios.$get(`/api/release/${this.url}`);
      this.release = rel;

      const lin = await this.$axios.$get(`/api/link/all?release=${this.release.id}`);
      this.link = lin;
    } catch (e) {
      throw e;
    }
  },
  fetchOnServer: true,
  methods: {
    triggerPopup() {
      this.showPopup = true;
      setTimeout(() => {
        this.showPopup = false;
      }, 3000);
    },
  },
  head() {
    return {
      title: `${this.release.name} - ${this.release.title}`,
      meta: [
        { vmid: 'og:title', property: 'og:title', content: `${this.release.name} - ${this.release.title}` },
        { vmid: 'og:type', property: 'og:type', content: 'website' },
        { vmid: 'og:locale', property: 'og:locale', content: 'ru_RU' },
        {
          vmid: 'og:description',
          property: 'og:description',
          content: `Слушать "${this.release.title}" от ${this.release.name} на всех площадках`,
        },
        { vmid: 'og:image', property: 'og:image', content: this.release.cover_resized },
        { vmid: 'og:url', property: 'og:url', content: this.url },
        { vmid: 'og:site_name', property: 'og:site_name', content: 'Exjaw Links' },
      ],
    };
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
