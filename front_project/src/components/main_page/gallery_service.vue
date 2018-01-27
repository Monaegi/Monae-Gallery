<template>
  <section id="gallery-service">
    <button class="gallery-service-list effect left">
      <article class="service-content-wrapper">
        <i class="fa fa-ticket" aria-hidden="true"></i>
        <p>Event</p>
      </article>
    </button>
    <button class="gallery-service-list effect center">
      <article class="service-content-wrapper">
        <i class="fa fa-university" aria-hidden="true"></i>
        <p>Space Rental</p>
      </article>
    </button>
    <button class="gallery-service-list effect right">
      <article class="service-content-wrapper">
        <i class="fa fa-credit-card-alt" aria-hidden="true"></i>
        <p>MemberShip</p>
      </article>
    </button>
  </section>
</template>
<script>
export default {
  
}
</script>
<style scoped>
#gallery-service{
  height: 20vh;
  width: 100%;
  display: flex;
  justify-content: space-around;
}
.gallery-service-list{
  position: relative;
  font-size: 2rem;
  /* border: 1px solid white; */
  width: 100%;
  height: 20vh;
  background-color: #444;
  color: white;
  text-align: center;
}
.gallery-service-list:hover{
  position: relative;
  background-color: #a58a78;
  width: 300%;
}
.service-content-wrapper{
  position: absolute;
  width: 100%;
  left: 50%;
  top: 50%;
  transform: translateY(-50%) translateX(-50%);
}
.gallery-service-list i{
  margin-bottom: 10px;
  font-size: 4rem;
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

