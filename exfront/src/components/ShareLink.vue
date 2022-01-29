<template>
  <div class="share" @click="copyPromo">
    <img src="../assets/share-link.svg" alt="Share">
  </div>
</template>

<script>
export default {
  name: 'share-link',
  methods: {
    copyPromo() {
      try {
        navigator.clipboard.writeText(window.location.href);
        this.triggerPopup();
      } catch (e) {
        throw e;
      }
    },
    triggerPopup() {
      this.$emit('popupCopied');
    },
  },
};
</script>

<style scoped>
.share {
  width: 45px;
  height: 45px;

  display: flex;
  align-items: center;
  justify-content: center;

  background-color: #333;
  border-radius: 45px;
  cursor: pointer;
}

.share img {
  pointer-events: none;
}

.share:hover {
  background: #383838;
  transition: ease .3s;
}

.share:active {
  background: #474747;
  transition: ease-out .3ms;
}
</style>
