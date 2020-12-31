<template> 
  <div id="app" class='bkimage'>

   <router-view></router-view>
  </div>
 </template>

<script>
export default {
  name: 'App',
}
</script>

<style >
  html,body {
        width:100% ;
        height:100%;
        top: 0px;

    }
  #app {
      width:100% ;
      height:100%;
    }

</style>
