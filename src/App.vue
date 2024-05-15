<script setup>
import HelloWorld from './components/HelloWorld.vue'
import TheWelcome from './components/TheWelcome.vue'
</script>

<template>
    <!-- <header>
      <img alt="Vue logo" class="logo" src="./assets/logo.svg" width="125" height="125" />

      <div class="wrapper">
        <HelloWorld msg="You did it!" />
      </div>
    </header>

    <main>
      <TheWelcome />
      <button @click="$router.push({name: 'd01'}); console.log('Méthode push exécutée');">Go to d01</button>
    </main> -->
    <router-view/>
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

<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>
