<!-- HTMLを記述 -->
<template>
  <div id='app'>
    <p>Home</p>
    <button @click="getRandom">占う</button>
    <p>Random number from backend: {{ randomNum }}</p>
    <h1 v-if="randomNum%4==0">Awesome!!!</h1>
    <h2 v-if="randomNum%4==1">Good</h2>
    <h2 v-if="randomNum%4==2">Bad...</h2>
    <h1 v-if="randomNum%4==3">S〇〇ks!!!</h1>
  </div>
</template>

<!-- JavaScriptを記述 -->
<script>
import axios from 'axios'

export default {
  data () {
    return {
      randomNum: 0
    }
  },
  methods: {
    getRandom () {
      console.log(777)
      this.randomNum = this.getRandomNum()
    },
    getRandomNum () {
      console.log(888)
      const path = 'http://localhost:9000/account/search'
      axios.get(path)
        .then(response => {
          this.randomNum = response.data.randomNum
          console.log(this.randomNum)
        })
        .catch(error => {
          console.log(error)
        })
    }
  },
  created () {
    this.getRandom()
  }
}
</script>
