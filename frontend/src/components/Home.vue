<template>
    <h1>Bem vindo ao mangaWave</h1>
    <form class="form">
        <input 
            type="text"
            v-model="form.name"
            placeholder="O que você está procurando?">
            <button> <i class="fa-brands fa-searchengin"></i>aaa</button>
    </form>
    <div class="links">
        <a href="#">Créditos</a>
    </div>
</template>
<script>
export default {
  name: 'HelloWorld',
  data() {
    return {
      form: {
        name: ""
      } 
    }
  }
}
</script>
