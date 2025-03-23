<template>
    <div class="content" id="about-us">
      <div class="session about-me">
        <div class="imagem">
          <img src="../assets/imagens/photoProfile.jpeg" alt="">
        </div>
        <div class="info">
          <div class="item">
            <h1 class="title"><span>O</span>lá eu me chamo Miguel</h1>
            <p class="text">
              Sou desenvolvedor do MangaWave e atuo como programador há {{ year }} anos, 
              sempre buscando evoluir e aprimorar minhas habilidades. O MangaWave 
              nasceu como um projeto pessoal, criado com o propósito de aprendizado 
              e experimentação de novas tecnologias. Não possui fins lucrativos, 
              sendo desenvolvido unicamente para estudo e para aprimorar meus conhecimentos na área. 
              Acredito que projetos práticos são essenciais para o crescimento profissional, 
              permitindo explorar diferentes desafios e encontrar soluções inovadoras.
            </p>
          </div>
          <div class="item">
            <h1 class="title"><span>M</span>inhas redes sociais</h1>
            <div class="links">
              <a href="https://www.linkedin.com/in/jo%C3%A3o-miguel-mendon%C3%A7a-665334187/" target="_blank">
                <i class="pi pi-linkedin"></i>
              </a>
              <a href="https://github.com/Miguel2k20" target="_blank">
                <i class="pi pi-github"></i>
              </a>
              <a href="https://www.instagram.com/joao_miguel.mp3/" target="_blank">
                <i class="pi pi-instagram"></i>
              </a>
            </div>
          </div>
          <div class="item">
            <h1 class="title"><span>T</span>ecnologias usadas nesse projeto</h1>
            <ul class="list">
              <li>Node 16</li>
              <li>Python 3</li>
              <li>Docker</li>
              <li>Vue</li>
              <li>Api: <a href="https://api.mangadex.org/docs/" target="_blank">Mangadex</a></li>
            </ul>
          </div>
        </div>
      </div>
    </div>
</template>
<script>
export default {
  name: 'AboutUs',
  data() {
    return {
      year: 0
    }
  },
  mounted() {
    this.year = new Date().getFullYear() - 2020;
	}
}
</script>

<style>
#about-us .about-me {
  display: flex;
  width: 100%;
  padding-top: 5%;
}
#about-us .about-me .imagem {
  width: 20%;
  max-width: 300px;
  max-height: 300px;
  border: 2px solid #dc5d51;
  overflow: hidden;
  border-radius: 10px;
}
#about-us .about-me .imagem img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}
#about-us .about-me .info {
  padding-left: 2rem;
  flex: 1;
}
#about-us .about-me .info .item {
  margin-bottom: 2%;
}
#about-us .about-me .info .item .title {
  font-size: clamp(1.8rem, 5vw, 2.5rem);
  font-weight: bold;
}
#about-us .about-me .info .item .title span {
  color: #dc5d51;
}
#about-us .about-me .info .item .text {
  margin-top: 1%;
  text-align: justify;
  line-height: 1.5rem;
  font-size: clamp(0.8rem, 5vw, 1rem);
}
#about-us .about-me .info .item .links {
  margin-top: 1rem;
  display: flex;
}
#about-us .about-me .info .item .links a {
  display: block;
  margin-right: 1rem;
  color: #555;
  font-size: clamp(1rem, 5vw, 1.5rem);
  border: 1px solid #555;
  justify-content: center;
  padding: 10px;
  border-radius: 10px;
  transition: all 0.5s ease;
}
#about-us .about-me .info .item .links a:hover {
  color: #fff;
  background: #dc5d51;
  border: #dc5d51 1px solid;
}
#about-us .about-me .info .item .list {
  margin-top: 1rem;
  list-style: circle;
  padding-left: 20px;
}
#about-us .about-me .info .item .list li {
  margin-bottom: 5px;
  font-size: clamp(0.8rem, 5vw, 1rem);
}
#about-us .about-me .info .item .list li a {
  color: #555;
}
@media (max-width: 960px) {
  .about-me {
    display: block;
  }
  .about-me .imagem {
    width: 100%;
    max-width: 150px;
  }
  .about-me .info {
    padding: 5% 0 0 0 ;
  }
}
</style>
