<template>
  <div class="content" id="search-mangas">
    <div class="session search">
      <div class="logo">
        <img src="../assets/imagens/logo.png" alt="">
      </div>
      <form action="" class="form-space">
        <input 
          v-model="formData.name"
          placeholder="O que você está procurando"
          type="text">
        <button>
          <span class="pi pi-search"></span>
        </button>
      </form>
    </div>
    <div class="session list">
      <div class="title-spance">
        <h2 class="title"><b>R</b>esultado para: <span>{{ actualTitle }}</span></h2>
        <h4 class="sub-title">{{ resultCount }} resultados encontrados</h4>
      </div>
    </div>

  </div>
</template>
<script>
export default {
name: 'SearchMangas',
props: {
  mangaName: String
},
data() {
  return {
    formData: {
      name: ""
    },
    actualTitle: "",
    resultCount: 0
  }
},
mounted() {
  if (this.mangaName) {
    this.formData.name = this.mangaName;
    this.actualTitle = this.mangaName;
  }
}
}
</script>

<style>
#search-mangas .search {
display: flex;
align-items: center;
padding-top: 2%;
}
#search-mangas .search .form-space {
width: 100%;
max-width: 450px;
position: relative;
}
#search-mangas .search .form-space input {
padding: 15px 10px;
width: calc(100% - 22px);
border: 1px solid #555;
background: #f1efe3;
border-radius: 10px;
outline: none;
color: #555;
}
#search-mangas .search .form-space button {
position: absolute;
right: 1px;
top: 1px;
border: none;
width: 50px;
height: calc(100% - 2px);
display: block;
border-radius: 9px;
padding: 0;
background: #f1efe3;
cursor: pointer;
transition: all 0.5s ease;
}
#search-mangas .search .form-space button:hover {
background: #dc5d51;
color: #fff;
}
#search-mangas .search .logo {
width: 100px;
}
#search-mangas .search .logo img {
width: 100%;
}
#search-mangas .list {
margin-top: 1%;
}
#search-mangas .list .title {
font-size: clamp(1.5rem, 5vw, 2rem);
font-weight: bold;
}
#search-mangas .list .title span {
text-transform: uppercase;
}
#search-mangas .list .title b {
color: #dc5d51;
}
#search-mangas .list .sub-title {
font-size: clamp(0.8rem, 5vw, 1rem);
margin-top: 5px;
}
</style>
