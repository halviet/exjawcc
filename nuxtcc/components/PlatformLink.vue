<template>
  <div class="platform__wrapper" @click="redirect" v-if="vision">
    <div class="platform__info">
      <img :src="icon" :alt="title" class="platform__icon">
      <span class="platform__name">{{ title }}</span>
    </div>

    <div class="platform__btn">
      <img src="../assets/arrow-right.svg" :alt="'Слушать на ' + title ">
    </div>
  </div>
</template>

<script>
export default {
  name: 'platform-link',
  props: {
    title: {
      type: String,
      required: true,
    },
    icon: {
      type: String,
      required: true,
    },
    url: {
      type: String,
      required: true,
    },
    vision: {
      type: Boolean,
      required: true,
    },
  },
  methods: {
    redirect() {
      window.location.href = this.url;
    },
  },
};
</script>

<style scoped>
.platform__wrapper {
  padding: 10px;
  margin-bottom: 12px;

  display: flex;
  justify-content: space-between;
  align-items: center;

  border-radius: 16px;
  cursor: pointer;
}
.platform__info {
  display: flex;
  align-items: center;
}
.platform__icon {
  width: 40px;
  height: 40px;
}
.platform__name {
  margin-left: 16px;

  font-family: Nunito-Regular, sans-serif;
  font-size: 18px;
  color: #eee;
}
.platform__btn {
  width: 45px;
  height: 45px;

  display: flex;
  align-items: center;
  justify-content: center;

  background-color: #333;
  border-radius: 12px;
  pointer-events: none;
}

.platform__wrapper:hover {
  background: #1F1E1F;
  transition: ease .3s;
}
.platform__wrapper:hover .platform__btn {
  background: #414141;
  transition: ease .3s;
}

.platform__wrapper:active {
  background: #333;
  transition: ease .3s;
}
.platform__wrapper:active .platform__btn {
  background: #474747;
  transition: ease .3s;
}
</style>
