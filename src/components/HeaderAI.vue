<script setup>    
    
    defineProps({
        msg: {
            type: Array,
            required: true
        }
    })

</script>

<template>
    <div class="HeaderAI">
        <div v-for="(message, index) in msg" :key="index">
            {{ message }}
        </div>
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
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

</style>