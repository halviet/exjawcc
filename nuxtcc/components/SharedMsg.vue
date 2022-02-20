<template>
  <div class="showmsg">
    <span>Ссылка скопирована!</span>
  </div>
</template>

<script>
export default {
  name: 'shared-msg',
};
</script>

<style scoped>
.showmsg {
  padding: 18px 0;
  width: 326px;

  position: fixed;
  bottom: 44px;
  left: auto;

  border-radius: 16px;
  background: #292929;
  color: #ccc;
  font-family: Nunito-Regular, sans-serif;
  text-align: center;

  transition: all .3s ease;
}
</style>
