<template>
    <div class="list-mangas" v-if="list.length > 0">
        <ul class="list-group">
            <li class="manga-item" v-for="manga in list" :key="manga.id">
                <MangaItem :manga="manga"/>
            </li>
        </ul>
    </div>
</template>
<script>
    import MangaItem from './MangaItem.vue'
    export default {
        name: 'MangaList',
        props: {
            list: Array
        },
        data() {
            return {
                listManga: []
            }
        },
        components: {
            MangaItem
        },
        mounted() {
            this.listManga = this.list
        },
        watch: {
            list: function (newList) {
                this.listManga = newList
            }
        }
    }
</script>

<style>
.list-group {
    display: flex;
    flex-wrap: wrap;
    padding: 20px;
}
.list-group .manga-item {
    width: calc(33.33% - 10px);
    margin: 0 10px 10px 0;
}
@media (max-width: 1024px) {
    .list-group .manga-item {
        flex: 1 1 calc(50% - 10px); 
        max-width: calc(50% - 10px);
    }
}

@media (max-width: 600px) {
    .list-group .manga-item {
        flex: 1 1 100%; /* Um item por linha */
        max-width: 100%;
    }
}
</style>