<template>
  <nav>
        <button @click="$router.push({name: 'Home'})">Home</button>
        <button @click="$router.push({name: '2015'})">2015</button>
        <button @click="$router.push({name: '2016'})">2016</button>
        <button @click="$router.push({name: '2017'})">2017</button>
        <button @click="$router.push({name: '2018'})">2018</button>
        <button @click="$router.push({name: '2019'})">2019</button>
        <button @click="$router.push({name: '2020'})">2020</button>
        <button @click="$router.push({name: '2021'})">2021</button>
        <button @click="$router.push({name: '2022'})">2022</button>
        <button @click="$router.push({name: '2023'})">2023</button>
    </nav>
    <h1>2021</h1>
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