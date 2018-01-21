<template>
  <nav id="navigation">
    <aside class="sign-wrap">
      <div class="logo">
        <a href="#" title="Monae Gallery 홈으로 바로가기" class="link"><img src="../../assets/logo/logo.png" width="80%" alt="logo"></a>
      </div>
      <ul class="sign-nav">
        <li class="sign-list" title="알람"><button><i class="fa fa-bell-o effect" aria-hidden="true"></i></button></li>
        <li class="sign-list" title="로그인"><button><i class="fa fa-user-circle effect" aria-hidden="true"></i></button></li>
        <li class="sign-list" title="회원가입"><button><i class="fa fa-user-plus effect" aria-hidden="true"></i></button></li>
      </ul>
    </aside>
    <ul class="menu">
      <li class="menu-list"><h2>Monae Gallery</h2></li>
      <li class="menu-list"><a href="#" class="link effect">Visit</a></li>
      <li class="menu-list"><a href="#" class="link effect">Exhibition</a></li>
      <li class="menu-list"><a href="#" class="link effect">Program</a></li>
      <li class="menu-list"><a href="#" class="link effect">News</a></li>
    </ul>
  </nav>  
</template>
<script>
export default {
  
}
</script>
<style>
  #navigation{
    position: relative;
    overflow: hidden;
  }
  .sign-wrap{
    z-index: 10000;
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
    height: 6vh;
    float: right;
  }
  .sign-nav i{
    line-height: 6vh;
    padding: 0 17px;
    height: 6vh;
    color: #fff;
  }
  .sign-nav i:hover{
    color: #a58a78;
    font-size: 3rem;
  }
  .logo{
    float: left;
  }
  .logo .link{
    position: absolute;
    transform: translateY(-50%);
    top: 50%;
  }
  .sign-list{
    float: left;
  }
  .sign-list button{
    padding: 0;
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
  .menu-list .link:hover{
    transform: rotate(20deg);
  }
</style>
