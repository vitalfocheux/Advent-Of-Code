<template>
    <button @click="$router.push({name: '2015'})">2015</button>
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