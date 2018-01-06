<template>
  <section id="gallery_service">
    <ul class="gallery_service_wrapper">
      <li class="gallery_service_list">service 1</li>
      <li class="gallery_service_list">service 2</li>
      <li class="gallery_service_list">service 3</li>
    </ul>
  </section>
</template>
<script>
export default {
  
}
</script>
<style>
  #gallery_service{
    height: 25vh;
    width: 100%;
    background-color: #222;
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
  }
</style>
