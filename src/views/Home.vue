<script setup>
    import AboutHome from '../components/AboutHome.vue'
    import Navbar from '../components/Navbar.vue'
</script>

<template>
    <Navbar />

    <AboutHome />
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