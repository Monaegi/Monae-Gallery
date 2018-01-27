<template>
  <section id="banner" @mouseenter="carusel_control.mouse_check = true" @mouseleave="carusel_control.mouse_check = false">
    <ul class="event-wrapper effect" :style="{'margin-left': carusel_control.position + 'vw'}">
      <li class="event-list" v-for="(list, index) in banner_list" :style="list.style" :key="index">
        <div class="event-info">
          <h2>{{list.title}}</h2>
          <p>{{list.content}}</p>
        </div>
      </li>
    </ul>
    <ul class="banner-nav-list">
      <li class="banner-nav effect" :class="(index * (-100)) == carusel_control.position ? 'current-nav' : ''" v-for="(list, index) in banner_list" :key="index" :style="list.style">
        <button @click="setBanner(index)"></button>
      </li>
    </ul>
  </section>
</template>
<script>
import banner1 from './../../assets/banner/banner1.jpg'
import banner2 from './../../assets/banner/banner2.jpg'

export default {
  data() {
    return {
      carusel_control: {
        mouse_check: false,
        position: 0
      },
      banner_list: [
        {
          style: {'background-image': 'url('+ banner1 +')'},
          title: 'Concert, Event',
          content: '2018.01.20 ~ 2018.02.01'
        },{
          style: {'background-image': 'url('+ banner2 +')'},
          title: 'Korean War Exhibition',
          content: '2018.01.30 ~ 2018.02.20'
        }
      ],
    }
  },
  methods: {
    nextBanner: function() {
      let position = this.carusel_control.position;
      if(position == (-100 * (this.banner_list.length-1))) {
        this.carusel_control.position = 0;
      } else {
        this.carusel_control.position = -100 * (this.banner_list.length-1)
      }
    },
    setBanner: function(index) {
      this.carusel_control.position = ++index * (-100) + 100;
    }
  },
  mounted () {
    setInterval(() => {this.carusel_control.mouse_check ? '' : this.nextBanner()}, 4000);
  }
}
</script>
<style scoped>
#banner{
  position: relative;
}
.event-wrapper{
  display: flex;
  width: 200vw;
}
.event-list{
  position: relative;
  z-index: -2;
  background-position: center;
  background-repeat: no-repeat;
  width: 100%;
  height: 60vh;
}
.event-list::after{
  content: '';
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  position: absolute;
  background-color: black;
  opacity: 0.6;
  z-index: 1;
}
.event-info{
  position: absolute;
  z-index: 1000;
  color: white;
  font-size: 2rem;
  right: 60px;
  top: 40px;
}
.event-info h2{
  display: inline;
  font-size: 6rem;
}
.banner-nav-list{
  position: absolute;
  bottom: 10px;
  right: 0;
}
.banner-nav{
  /* box-shadow: 1px 1px 2px 2px #a58a78, -1px -1px 2px 2px #a58a78; */
  opacity: 0.5;
  border-radius: 5px;
  float: left;
  margin-right: 30px;
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}
.banner-nav:hover, .current-nav{
  opacity: 1;
  box-shadow: 1px 1px 1px #fff, -1px -1px 1px #fff;
  transform: scale(1.2);
}
.banner-nav button{
  padding: 40px 80px;
}
.current-nav{
  transform: scale(1.2);
}
</style>
