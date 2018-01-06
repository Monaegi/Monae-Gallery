<template>
  <section id="banner">
    <article class="event_info">
      <h2>Concert, Event</h2><p>2018.01.20 ~ 2018.02.01</p>
    </article>
  </section>
</template>
<script>
export default {
  
}
</script>
<style>
#banner{
  z-index: -2;
  position: relative;
  background-image: url(./../assets/banner.jpg);
  background-position: center;
  background-repeat: no-repeat;
  width: 100%;
  height: 60vh;
  padding: 20px;
}
#banner::after{
  content: '';
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  position: absolute;
  background-color: black;
  opacity: 0.6;
  z-index: -1;
}
.event_info{
  color: white;
  float: right;
  font-size: 2rem;
}
.event_info h2{
  display: inline;
  font-size: 6rem;
}
</style>
