<template>
    <div id="footer">
      <span>
        © {{ year }} Miguel. Todos os direitos reservados. Este projeto utiliza a API do 
        <a href="https://api.mangadex.org/docs/"  target="_blank">MangaDex</a>, mas não é 
        afiliado ou endossado por eles.
      </span>
    </div>
</template>
<script>
export default {
  name: 'AppFooter',
  data() {
    return {
      year:  ""
    }
  },
  mounted() {
    this.year = new Date().getFullYear();
	}
}
</script>
<style>
#footer {
  background: #dc5d51;
  color: #fff;
  padding: 25px 15px;
  max-height: 65px;
  text-align: center;
  margin-top: 5%;
}
#footer a {
  color: #fff;
}
</style>
