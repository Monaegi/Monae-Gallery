<template>
  <section>
    <navigation/>
    <rent/>
  </section>
</template>

<script>
import navigation from './components/navigation'
import rent from './components/rent'

//새로운 컴포넌트를 추가 할 때는 아래 components에 추가해 주세요.
//ex) components: { scheduler, addComponent }
export default {
  name: 'app',
  components: {
    navigation, rent
  }
}
</script>

<style>
  html{
    font-size: 10px;
  }
  a{
    color: inherit;
    text-decoration: none;
    display: block;
  }
  body{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }
  h1, h2, h3, h4, h5{
    margin: 0;
    padding: 0;
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
</style>
