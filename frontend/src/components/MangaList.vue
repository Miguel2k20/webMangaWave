<template>
    <pre>{{ list }}</pre>
</template>
<script>
    export default {
        name: 'MangaList',
        props: {
            list: Array
        },
    }
</script>