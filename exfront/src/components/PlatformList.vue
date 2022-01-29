<template>
  <div class="list__wrapper">
    <platform-link
      v-for="item in link"
      :title="item.platform.title"
      :icon="item.platform.icon"
      :url="item.url"
      :vision="item.vision"
      :key="item.id"
    />
  </div>
</template>

<script>
import PlatformLink from '../components/PlatformLink';

export default {
  components: { PlatformLink },
  props: {
    link: {
      type: Array,
      required: true,
    },
  },
};
</script>

<style scoped>
.list__wrapper {
  margin-top: 30px;
}
</style>
