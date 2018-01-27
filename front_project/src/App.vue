<template>
  <section>
    <navigation/>
    <banner/>
    <galleryService/>
    <mainCalendar/>
    <router-view></router-view>
  </section>
</template>

<script>
import navigation from './components/main_page/navigation'
import banner from './components/main_page/banner'
import galleryService from './components/main_page/gallery_service'
import mainCalendar from './components/main_page/main_calendar'
import scheduler from './components/scheduler'


//새로운 컴포넌트를 추가 할 때는 아래 components에 추가해 주세요.
//ex) components: { scheduler, addComponent }
export default {
  name: 'app',
  components: {
    navigation, banner, galleryService, mainCalendar,
    scheduler
  }
}
</script>

<style>
  html{
    font-size: 10px;
  }
  section{
    box-sizing: border-box;
  }
  a, a:visited{
    color: inherit;
    text-decoration: none;
    display: block;
  }
  a:hover{
    color: #a58a78;
  }
  body{
    color: #555;
    box-sizing: border-box;
    height: 100%;
    margin: 0;
    padding: 0;
    overflow-x: hidden;
  }
  h1, h2, h3, h4, h5{
    margin: 0;
    padding: 0;
    font-weight: normal;
  }
  ul{
    margin: 0;
    padding: 0;
  }
  li{
    list-style: none;
    padding: 0;
    margin: 0;
  }
  i.fa{
    font-size: 1.7rem;
  }
  button{
    outline: none;
    cursor: pointer;
    background: none;
    border: none;
  }
  .effect{
    transition: 0.5s all;
  }
</style>
