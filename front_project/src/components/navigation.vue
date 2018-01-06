<template>
  <nav id="navigation">
    <aside class="sign-wrap">
      <div class="logo">
        <a href="#" title="Monae Gallery 홈으로 바로가기" class="link"><img src="../assets/logo/logo.png" width="80%" alt="logo"></a>
      </div>
      <ul class="sign-nav">
        <li class="sign-list" title="알람"><a href="#" class="link"><i class="fa fa-bell-o" aria-hidden="true"></i></a></li>
        <li class="sign-list" title="로그인"><a href="#" class="link"><i class="fa fa-sign-in" aria-hidden="true"></i></a></li>
        <li class="sign-list" title="회원가입"><a href="#" class="link"><i class="fa fa-user-plus" aria-hidden="true"></i></a></li>
      </ul>
    </aside>
    <ul class="menu">
      <li class="menu-list"><h2>Monae Gallery</h2></li>
      <li class="menu-list"><a href="#" class="link">Visit</a></li>
      <li class="menu-list"><a href="#" class="link">Exhibition</a></li>
      <li class="menu-list"><a href="#" class="link">Program</a></li>
      <li class="menu-list"><a href="#" class="link">News</a></li>
    </ul>
  </nav>  
</template>
<script>
export default {
  
}
</script>
<style>
  #navigation{
    overflow: hidden;
  }
  .sign-wrap{
    height: 6vh;
    position: fixed;
    width: 100%;
    color: #fff;
    background-color: #111;
    font-size: 1.5rem;
  }
  .sign-wrap::after{
    content:'';
    display:block;
    clear:both;
  }
  .sign-nav{
    float: right;
  }
  .logo{
    float: left;
  }
  .logo .link{
    padding-top: 2px;
  }
  .sign-list{
    line-height: 45px;
    float: left;
  }
  .link{
    padding: 0 17px;
  }
  .menu{
    line-height: 9vh;
    margin-top: 6vh;
    height: 9vh;
  }
  .menu::after{
    content:'';
    display:block;
    clear:both;
  }
  .menu h2{
    font-size: 3rem;
  }
  .menu-list{
    padding-left: 17px;
    float: left;
    font-size: 2rem;
  }
</style>
