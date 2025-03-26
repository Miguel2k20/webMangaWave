<template>
    <a :href="mangaObject.link" class="item">
        <div class="imagem">
            <img :src="mangaObject.cover_art" alt="Capa do manga">
        </div>
        <div class="info">
            <h3 class="title-manga">
                {{ mangaObject.title }}
            </h3>
            <h3 class="status-manga">
                {{ mangaObject.status }}
            </h3>
        </div>
    </a>
</template>
<script>
import VanillaTilt from 'vanilla-tilt';
export default {
    name: 'MangaItem',
    props: {
        manga: Object
    },
    data() {
        return {
            mangaObject: {}
        }
    },
    methods: {
        reorderMangaObject() {
            this.mangaObject = {
                link: "http://localhost:8080/info-mangas?id=" + this.manga[0],
                title: this.manga[1].title,
                status: this.manga[1].status == "completed" ? "Completo" : "Em andamento",
                cover_art: this.manga[1].cover_art,
            }
        },
        applyTilt() {
            VanillaTilt.init(document.querySelectorAll('.imagem'), {
                max: 5,
                speed: 300,
                perspective: 1000,
                scale: 1,
                glare: true,
                "max-glare": 0.3
            });
        }
    },
    mounted() {
        this.reorderMangaObject()
        this.applyTilt()
    },
    watch: {
        manga: function (newManga) {
            this.mangaObject = newManga
            this.reorderMangaObject()
            this.applyTilt()
        }
    }
}
</script>
<style>
.item {
    display: block;
    height: calc(100% - 42px);
    width: calc(100% - 42px);
    color: #555;
    border: 1px solid #555;
    border-radius: 5px;
    padding: 20px;
    display: block;
    text-decoration: none;
    transition: all 0.8s ease;
}

.item:hover {
    background: #dc5d51;
    border: 1px solid #dc5d51;
    color: #fff;
}

.item .imagem {
    width: 100%;
    max-width: 250px;
    object-fit: cover;
    display: block;
    margin: 0 auto;
}
.item .imagem img{
    width: 100%;
    object-fit: cover;
}

.item .info {
    margin-top: 1rem;
    text-align: center;
}

.item .info .title-manga {
    font-weight: bold;
    font-size: clamp(1.2rem, 2vw, 1.5rem);
}

.item .info .status-manga {
    font-size: clamp(0.8rem, 2vw, 1rem);
    margin-top: 1rem;
}
/* @media (max-width: 1024px) {
    .item .imagem {
        width: ;
    }
} */
</style>