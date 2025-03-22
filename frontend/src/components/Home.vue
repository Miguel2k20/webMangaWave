<template>
    <div class="content" id="home">
      <div class="session">
        <div class="imagem">
          <img alt="Vue logo" src="./../assets/imagens/logo.png">
        </div>
        <h1 class="title">Bem vindo ao <span>mangaWave</span></h1>
        <form class="form">
            <input 
                type="text"
                v-model="form.name"
                placeholder="O que você está procurando?">
                <button> <span class="pi pi-search"></span></button>
        </form>
      </div>
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

<style>
#home {
  display: flex;
  justify-content: center;
  padding-top: 5%;
}

#home .session .imagem {
  display: block;
  max-width: 50%;
  margin: 0 auto;
}
#home .session .imagem img {
  display: block;
  width: 100%;
}
#home .session .title {
  font-size: clamp(1.8rem, 5vw, 2.5rem);
  font-weight: bold;
  text-align: center;
  text-transform: uppercase;
}
#home .session .title span {
  color: #dc5d51;
}
#home .session form {
  margin-top: 5%;
  position: relative;
}
#home .session form input {
  width: calc(100% - 52px);
  max-width: 950px;
  font-size: clamp(1rem, 2vw, 1.3rem);
  padding: 15px 25px;
  border-radius: 10px;
  border: 1px solid #ccc;
  outline: none;
  background: #f1efe3;
  color: #555;
}
#home .session form button {
  position: absolute;
  right: 1px;
  top: 1px;
  border-radius: 10px;
  width: 60px;
  height: calc(100% - 2px);
  border: none;
  outline: none;
  font-size: 15px;
  cursor: pointer;
  background: #f5f5f5;
  transition: all 0.5s ease;
  background: #f1efe3;
  color: #555;
}
#home .session form button:hover {
  background:#dc5d51;
  color: #fff; 
}
</style>
