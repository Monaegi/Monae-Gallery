<template>
  <section id="banner">
    <ul class="event_wrapper effect" :style="{'margin-left': carusel_control + 'vw'}">
      <li class="event_list" v-for="(list, index) in banner_list" :style="list.style" :key="index">
        <div class="event_info">
          <h2>{{list.title}}</h2>
          <p>{{list.content}}</p>
        </div>
      </li>
    <button class="prev_button move_button" @click="prevBanner"><i class="fa fa-angle-left effect" aria-hidden="true"></i></button>
    <button class="next_button move_button" @click="nextBanner"><i class="fa fa-angle-right effect" aria-hidden="true"></i></button>
    </ul>
    
  </section>
</template>
<script>
import banner1 from './../../assets/banner/banner1.jpg'
import banner2 from './../../assets/banner/banner2.jpg'

export default {
  data() {
    return {
      carusel_control: 0,
      banner_list: [
        {
          style: {'background-image': 'url('+ banner1 +')'},
          title: 'Concert, Event',
          content: '2018.01.20 ~ 2018.02.01'
        },{
          style: {'background-image': 'url('+ banner2 +')'},
          title: 'Concert, Event',
          content: '2018.01.20 ~ 2018.02.01'
        }
      ],
    }
  },
  methods: {
    prevBanner: function() {
      if(this.carusel_control != 0 && this.carusel_control != (-100 * (this.banner_list.length-1))) {
        this.carusel_control = this.carusel_control - 100;
      } else if(this.carusel_control == (-100 * (this.banner_list.length-1))) {
        this.carusel_control = 0;
      } else {
        this.carusel_control = -100 * (this.banner_list.length-1);
      };
    },
    nextBanner: function() {
      if(this.carusel_control == (-100 * (this.banner_list.length-1))) {
        this.carusel_control = 0;
      } else {
        this.carusel_control = -100 * (this.banner_list.length-1)
      }
    }
  }
}
</script>
<style>
#banner{
  position: relative;
}
.event_wrapper{
  display: flex;
  width: 200vw;
}
.event_list{
  position: relative;
  z-index: -2;
  background-position: center;
  background-repeat: no-repeat;
  width: 100%;
  height: 60vh;
}
.event_list::after{
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
.event_info{
  position: absolute;
  z-index: 1000;
  color: white;
  font-size: 2rem;
  right: 60px;
  top: 40px;
}
.event_info h2{
  display: inline;
  font-size: 6rem;
}

.move_button{
  height: 10vh;
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
}
.move_button i{
  color: #444;
  font-size: 10rem;
  padding: 0 5px;
}
.move_button i:hover{
  transform: scale(1.5);
  opacity: 1;
  color: #a58a78;
}
.prev_button{
  left: 0;
}
.next_button{
  right: 0;
}
</style>
