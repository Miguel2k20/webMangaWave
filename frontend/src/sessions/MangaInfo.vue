<template>
  <div class="content" id="mangaInfo">
    <SpinnerMain :show="showSpinner" text="Buscando os capítulos..." />
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
        <div href="" class="chapter-item" v-for="chapter in volumes" :key="chapter.id">
          <div class="manga-info">
            <h5 class="chapter-sub-title">
              Título: {{ chapter.attributes.title ?? 'Sem título' }}
            </h5>
            <h5 class="chapter-title">
              Capítulo: {{ chapter.attributes.chapter }}
            </h5>
            <span class="moreinfo"> Páginas: {{ chapter.attributes.pages }} </span>
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
    <Pagination
      :total="total"
      :limit="limit"
      :current-page="currentPage"
      @change-page="handlePageChange"
    />
  </div>
</template>
<script>
import axios from 'axios';
import SpinnerMain from '@/components/SpinnerMain.vue';
import Pagination from '@/components/Pagination.vue'; 

export default {
  name: 'MangaInfo',
  props: {
    mangaId: String,
  },
  components: {
    SpinnerMain,
    Pagination, 
  },
  data() {
    return {
      chapterList: [],
      showSpinner: false,
      limit: 100,
      offset: 0, 
      currentPage: 1, 
    };
  },
  mounted() {
    this.searchMangaChapters();
  },
  methods: {
    async searchMangaChapters() {
      if (this.mangaId) {
        this.showSpinner = true;
        try {
          const response = await axios.get('http://localhost:5000/get-manga-chapters', {
            params: {
              idManga: this.mangaId,
              offset: this.offset,
              limit: this.limit,
            },
          });
          this.chapterList = response.data.data; 
          this.total = response.data.total || 0; 
        } catch (error) {
          console.error(error);
        } finally {
          this.showSpinner = false;
        }
      }
    },
    handlePageChange(page) {
      this.currentPage = page;
      this.offset = (this.currentPage - 1) * this.limit;
      this.searchMangaChapters();
    },
  },
};
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
