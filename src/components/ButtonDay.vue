<script setup>
    import { useRouter } from 'vue-router'
    
    
    defineProps({
        year: {
            type: String,
            required: true
        }
    })

    const router = useRouter()
</script>

<template>
    <div class="button-container">
      <button v-for="i in 25" :key="i" class="my-button" @click="router.push({name: (year)+'-'+i})">
        Button {{ i }}
      </button>
    </div>
  </template>
  
  <script>
    

  export default {
    name: 'ButtonDay',
    // setup() {
    //   const router = useRouter()
    //   return { router }
    // }
  }
  </script>
  
  <style scoped>
    .button-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
    align-items: center;
    }

    .my-button {
    flex: 1 0 auto;
    margin: 10px;
    width: 100px; /* Define a fixed width */
    height: 100px; /* Define a fixed height */
    border-radius: 50%;
    text-align: center;
    }
  </style>