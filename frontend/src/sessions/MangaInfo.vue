<template>
  <div class="content" id="mangaInfo">
      <ul class="list">
        <li v-for="(volumes, index) in chapterList" :key="index">
          <h4>
            Volumes : {{ index }}
          </h4>
          <div class="chapterList" v-for="chapter in volumes" :key="chapter">
             
            <h4>Capitulo : {{ chapter }}</h4>
            {{ chapter }}
          </div>
        </li>
      </ul>
   </div>
</template>
<script>
import axios from 'axios'
export default {
  name: 'AboutUs',
  data() {
    return {
      chapterList: []
    }
  },
  props: {
    mangaId: String
  },
  methods:{
    async searchMangaCharacters(){
      if(this.mangaId){
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
</style>
