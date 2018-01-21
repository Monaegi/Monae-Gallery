<template>
  <section id="gallery_service">
    <ul class="gallery_service_wrapper">
      <li class="gallery_service_list effect left">
        <i class="fa fa-credit-card-alt" aria-hidden="true"></i>
        service 1
      </li>
      <li class="gallery_service_list effect center">
        service 2
      </li>
      <li class="gallery_service_list effect right">
        service 3
      </li>
    </ul>
  </section>
</template>
<script>
export default {
  
}
</script>
<style scoped>
#gallery_service{
  height: 25vh;
  width: 100%;
}
.gallery_service_wrapper{
  display: flex;
  justify-content: space-around;
}
.gallery_service_list{
  font-size: 2rem;
  border: 1px solid white;
  width: 100%;
  height: 25vh;
  background-color: #222;
}
.gallery_service_list:hover{
  z-index: 2;
  position: relative;
  transform: scale(1.2);
}
.left:hover{
  transform-origin: 0% 100%;
}
.center:hover{
  transform-origin: 50% 100%;
}
.right:hover{
  transform-origin: 100% 100%;
}
</style>

