<script setup>
    import ButtonDay from '../components/ButtonDay.vue'
    import Navbar from '@/components/Navbar.vue';
</script>

<template>
    <Navbar />

    <ButtonDay year="2020" />

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