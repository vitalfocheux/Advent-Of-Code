<script setup>    
    
    defineProps({
        msg: {
            type: String,
            required: true
        }
    })

</script>

<template>
    <div class="HeaderAI">
        {{ msg }}
    </div>
  </template>
  
  <script>
  export default {
    name: 'HeaderAI'
  }
  </script>

<style scoped>
.HeaderAI {
    border: 1px solid black;
    border-radius: 10px;
    background-color: lightgray;
    display: flex;
    justify-content: center;
    align-items: center;
}
</style>