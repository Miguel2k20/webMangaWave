<template>
  <div class="content" id="mangaInfo">
      <SpinnerMain :show="showSpinner" text="Buscando os capítulos..."/>
      <ul class="list">
        <li v-for="(volumes, index) in chapterList" :key="index" class="volume-item">
          <div class="title-space">
            <h4 class="volume-title">
              <b>V</b>olume: {{ index }}
            </h4>
            <div class="buttons">
              <a href="">
                <i class="pi pi-file-pdf"></i>
              </a>
              <a href="">
                <i class="pi pi-amazon"></i>
              </a>
            </div>
          </div>
          <div href="" class="chapter-item" v-for="chapter in volumes" :key="chapter" >
            <div class="manga-info">
              <h5 class="chapter-sub-title">
                Capitulo: {{ chapter.attributes.chapter }}
              </h5>
              <h5 class="chapter-title">
                {{ chapter.attributes.title }}
              </h5>
              <span class="moreinfo">
                Paginas: {{ chapter.attributes.pages }}
              </span>
            </div>
            <div class="buttons">
              <a :href="chapter.id">
                <i class="pi pi-file-pdf"></i>
              </a>
              <a :href="chapter.id">
                <i class="pi pi-amazon"></i>
              </a>
            </div>
          </div>
        </li>
      </ul>
   </div>
</template>
<script>
import axios from 'axios'
import SpinnerMain from '@/components/SpinnerMain.vue';

export default {
  name: 'AboutUs',
  data() {
    return {
      chapterList: [],
      showSpinner: false
    }
  },
  components: {
    SpinnerMain
  },
  props: {
    mangaId: String
  },
  methods:{
    async searchMangaCharacters(){
      if(this.mangaId){
        this.showSpinner = true
        try {
          const response = await axios.get('http://localhost:5000/get-manga-chapters', {
            params:{
              idManga: this.mangaId,
              offset: 0,
            }
          });
          this.chapterList = response.data.data
        } catch (error) {
          console.error(error);
        } finally {
          this.showSpinner = false
        }
      }
    }
  },
  mounted() {
    this.searchMangaCharacters()
	}
}
</script>

<style>
#mangaInfo {
  padding-top: 5%;
}
#mangaInfo .list .volume-item {
  margin-bottom: 1rem;
  border: 2px solid #ccc;
  padding: 1rem;
  border-radius: 5px;
}
#mangaInfo .list .volume-item .title-space {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
#mangaInfo .list .volume-item .title-space .buttons a {
  margin-left: 1rem;
  font-size: 1.5rem;
  color: #ccc;
}
#mangaInfo .list .volume-item .title-space .buttons a:hover {
  color: #dc5d51;
}
#mangaInfo .list .volume-item .title-space .volume-title {
  font-size: 2rem;
  margin-bottom: 1rem;
  font-weight: bold;
}
#mangaInfo .list .volume-item .title-space .volume-title b {
  color: #dc5d51;
}
#mangaInfo .list .chapter-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
  border: 1px solid #ccc;
  border-radius: 5px;
  margin-bottom: 1rem;
}
#mangaInfo .list .chapter-item .chapter-sub-title, #mangaInfo .list .chapter-item .moreinfo {
  font-size: 0.8em;
}
#mangaInfo .list .chapter-item .chapter-title {
  font-size: 1.5rem;
  font-weight: bold;
}
#mangaInfo .list .chapter-item .buttons a {
  margin-left: 0.5rem;
  font-size: 1.3rem;
  color: #ccc;
}
#mangaInfo .list .chapter-item .buttons a:hover {
  color: #dc5d51;
}
</style>
