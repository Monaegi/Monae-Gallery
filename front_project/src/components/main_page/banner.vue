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
      <li class="banner-nav" v-for="index in banner_list.length" :key="index">
        <button @click="setBanner(index)"><i class="fa fa-circle effect" :class="(index * (-100) +100) == carusel_control.position ? 'current-nav' : ''" aria-hidden="true"></i></button>
      </li>
    </ul>
    <button class="prev-button move-button"><i class="fa fa-angle-left effect" @click="prevBanner" aria-hidden="true"></i></button>
    <button class="next-button move-button"><i class="fa fa-angle-right effect"  @click="nextBanner" aria-hidden="true"></i></button>
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
        position: 0,
        color: '#fff'
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
    prevBanner: function() {
      let position = this.carusel_control.position;
      if(position != 0 && position != (-100 * (this.banner_list.length-1))) {
        this.carusel_control.position = position - 100;
      } else if(position == (-100 * (this.banner_list.length-1))) {
        this.carusel_control.position = 0;
      } else {
        this.carusel_control.position = -100 * (this.banner_list.length-1);
      };
    },
    nextBanner: function() {
      let position = this.carusel_control.position;
      if(position == (-100 * (this.banner_list.length-1))) {
        this.carusel_control.position = 0;
      } else {
        this.carusel_control.position = -100 * (this.banner_list.length-1)
      }
    },
    setBanner: function(index) {
      this.carusel_control.position = index * (-100) + 100;
    }
  },
  mounted () {
    setInterval(() => {this.carusel_control.mouse_check ? '' : this.nextBanner()}, 3000);
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
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
}
.banner-nav{
  float: left;
}
.banner-nav i{
  padding: 30px 7px;
  color: #999;
}
.banner-nav .current-nav{
  transform: scale(1.2);
  color: white;
}
.banner-nav i:hover{
  transform: scale(1.2);
  color: white;
}

.move-button{
  height: 10vh;
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
}
.move-button i{
  color: #444;
  font-size: 10rem;
  padding: 0 5px;
}
.move-button i:hover{
  transform: scale(1.5);
  opacity: 1;
  color: #a58a78;
}
.prev-button{
  left: 0;
}
.next-button{
  right: 0;
}
</style>
