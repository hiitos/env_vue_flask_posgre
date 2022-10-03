<!-- HTMLを記述 -->
<template>
  <div id='app'>
    <p>Home</p>
    <button @click="getRandom">ランダムでデータ取得</button>
    <p>Random number from backend: {{ randomNum }}</p>
    <h2>DATA</h2>
    <p>account_name: {{ account_name }}</p>
    <p>id: {{ id }}</p>
    <p>start_on: {{ start_on }}</p>
  </div>
</template>

<!-- JavaScriptを記述 -->
<script>
import axios from 'axios'

export default {
  data () {
    return {
      randomNum: 0,
      account_name: '',
      id: 0,
      start_on: ''
    }
  },
  methods: {
    getRandom () {
      console.log('-----getRandom関数-----')
      this.randomNum = this.getRandomNum()
    },
    getRandomNum () {
      console.log('-----getRandomNum関数-----')
      const path = 'http://localhost:9000/rand'
      axios.get(path)
        .then(response => {
          this.randomNum = response.data.randomNum
          this.getAccountdata()
          console.log(this.randomNum)
        })
        .catch(error => {
          console.log(error)
        })
    },
    async getAccountdata () {
      console.log('AccountData取得')
      const path = 'http://localhost:9000/api/account/get/' + this.randomNum
      const response = await axios.get(path)
      console.log(response)
      axios.get(path)
        .then(response => {
          this.account_name = response.data.body.account_name
          this.id = response.data.body.id
          this.start_on = response.data.body.start_on
          console.log(this.account_name)
          console.log(this.id)
          console.log(this.start_on)
        })
        .catch(error => {
          console.log(error)
        })
    }
  },
  created () {
    this.getRandom()
    this.getAccountdata()
  }
}
</script>
