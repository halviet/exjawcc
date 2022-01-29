<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App',
};
</script>

<style>
html {
    background-color: #171617;
}

* {
  padding: 0;
  margin: 0;
  box-sizing: border-box;
}

#app {
  font-family: Nunito-SemiBold, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}


@font-face {
  font-family: "Nunito-Regular";
  src: local("Nunito-Regular"),
  url("./assets/fonts/Nunito-Regular.ttf") format("truetype");
  font-weight: 400;
}
@font-face {
  font-family: "Nunito-SemiBold";
  src: local("Nunito-SemiBold"),
  url("./assets/fonts/Nunito-SemiBold.ttf") format("truetype");
  font-weight: 600;
}
@font-face {
  font-family: "Nunito-Bold";
  src: local("Nunito-Bold"),
  url("./assets/fonts/Nunito-Bold.ttf") format("truetype");
  font-weight: 700;
}
</style>
