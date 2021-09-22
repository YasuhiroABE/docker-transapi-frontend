<template>
  <div id="app">
    <Translation />
  </div>
</template>

<script>
import Translation from './components/Translation.vue'

export default {
  name: 'App',
  components: {
    Translation
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
