<template>
    <div id="spinner-main" v-show="show">
        <div class="content-spinner">
            <VueSpinnerOrbit size="150" color="#dc5d51" />
            <span>{{ text }}</span>
        </div>
    </div>
</template>
<script>
import {VueSpinnerOrbit} from 'vue3-spinners';
export default {
    name: 'SpinnerMain',
    components: {
        VueSpinnerOrbit
    },
    props: {
        show: Boolean,
        text: String
    },
}
</script>
<style>
#spinner-main {
    background: #f1efe3;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    width: 100%;
    z-index: 99;
    position: fixed;
    top: 0%;
    left: 0;
}
#spinner-main .content-spinner svg {
    margin: 0 auto;
    display: block;
}
#spinner-main .content-spinner span {
    display: block;
    font-size: 2rem;
    font-weight: bold;
    margin-top: 1rem;
}



</style>