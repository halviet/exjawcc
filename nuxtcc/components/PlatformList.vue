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
    <div class="skelet__wraper" v-if="!link[0]">
      <div class="skelet__load link__load"></div>
      <div class="skelet__load link__load"></div>
    </div>
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
.link__load {
  padding: 10px;
  margin-bottom: 12px;
  height: 65px;

  display: flex;
  justify-content: space-between;
  align-items: center;

  border-radius: 16px;
  cursor: pointer;
}
</style>
