<template>
    <h1>d01</h1>
    <br>
    <button @click="$router.push({name: '2015'})">Go to 2015</button>
    <br>
  <button @click="$router.push({name: 'Home'})">Go to Home</button>
</template>

<script>
  import { useRouter } from 'vue-router'

  export default {
    setup() {
      const router = useRouter()
      return { router }
    }
  }
</script>