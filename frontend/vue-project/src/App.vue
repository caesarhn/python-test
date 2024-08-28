<script setup>
  import {ref} from 'vue'
  import axios from 'axios'

  const input = ref()
  const data = ref()

  function GenerateSegitiga(){
    axios("http://localhost:5000/segitiga", {
      params: {
        data: input.value
      }
    }).then(res => {
      console.log(res)
    })
  }

  async function GenerateGanjil(){
    await axios("http://localhost:5000/ganjil", {
      params: {
        data: input.value
      }
    }).then(res => {
      console.log(res)
      data.value = res.data
    })
  }

  async function GeneratePrime(){
    await axios("http://localhost:5000/prima", {
      params: {
        data: input.value
      }
    }).then(res => {
      console.log(res)
      data.value = res.data
    })
  }
</script>

<template>
  <header>
  </header>

  <main>
    <input v-model="input" type="text"/>
    <button @click="GenerateSegitiga" type="button">Generate Segitiga</button>
    <button @click="GenerateGanjil" type="button">Generate Bilangan Ganjil</button>
    <button @click="GeneratePrime" type="button">Generate bilangan Prima</button>
    <br/>
    <p>{{ data }}</p>
  </main>
</template>

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
