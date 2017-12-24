<template>
  <nav>
    <aside class="sign-wrap">
      <ul class="sign-nav">
        <li class="sign-list"><a href="#" class="link">SignIn</a></li>
        <li class="sign-list"><a href="#" class="link">SignUp</a></li>
      </ul>
    </aside>
    <ul>
      <li><img src="../assets/logo/logo.png" alt="logo"></li>
      <li>Visit</li>
    </ul>
  </nav>  
</template>
<script>
export default {
  
}
</script>
<style>
  .sign-wrap{
    color: #fff;
    background-color: #222222;
    font-size: 1.5rem;
    height: 40px;
    line-height: 40px;
  }
  .sign-wrap::after{
    content:'';
    display:block;
    clear:both;
  }
  .sign-nav{
    float: right;
  }
  .sign-list{
    float: left;
  }
  .link{
    padding: 0 15px;
  }
</style>
