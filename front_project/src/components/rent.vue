<template>
  <div id="rent" v-if="ok === true">
    <section class="form-wrap">
      <p>대관하기</p>
      <form action="">
        <input type="text" class="room-name" id="searchKeyword" placeholder="어떤 룸을 대관하시나요?" />
        <div id="autocomplete"></div>
        <article class="date-wrap">
          <div class="day">
            <button class="select-left">날짜 선택</button>
            <input type="text" class="target-left" v-bind:value="year + '-' + month + '-' + target" readonly>
          </div>
          <div class="time">
            <button class="select-right">시간 선택</button>
            <input type="text" class="target-right" v-bind:value="time" readonly>
          </div>
        </article>
        <button class="regi-btn">예약하기</button>
      </form>
    </section>
  </div>
  <div id="scheduler" v-else>
    <section class="desc">
      <article class="date">
        <p class="day">{{ target }}</p>
        <hr />
        <span>{{ week }}</span>
      </article>
      <article class="description">
        <p>대관하기</p>
        <button class="room active">파이썬</button>
        <button class="room no-active">자바</button>
        <button class="room no-active">루비</button>
        <div class="python">
          <ul>
            <li v-for="time in times">
              <span class="time">{{ time }}</span>
              <button class="reserve" v-on:click="reserve(time)">예약 가능</button>
            </li>
          </ul>
        </div>
        <div class="java"></div>
        <div class="ruby"></div>
      </article>
    </section>
    <table class="calendar">
      <tr class="month">
        <td colspan="7">
          <button class="prev-next" v-on:click="prevMonth()"><i class="im im-angle-left-circle"></i></button>
          <span>{{ year }}.{{ month }}</span>
          <button class="prev-next" v-on:click="nextMonth()"><i class="im im-angle-right-circle"></i></button>
        </td>
      </tr>
      <tr class="summit">
        <td>SUN</td>
        <td>MON</td>
        <td>TUE</td>
        <td>WED</td>
        <td>THU</td>
        <td>FRI</td>
        <td>SAT</td>
      </tr>
      <tr v-for="row in result" class="row">
        <td v-for="(day, index) in row">
          <a href="#" v-if="day == 0"></a>
          <a href="#" class="day" v-on:click="dayTarget(day, index)" v-else>{{ day }}</a>
        </td>
      </tr>
    </table>
  </div>
</template>

<script type="text/javascript">
  var today = new Date();
  var year = today.getFullYear();
  var month = today.getMonth() + 1;
  var day = today.getDate();
  var weekIdx = today.getDay();
  var week = ["SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY"]
  export default {
    name: 'scheduler',
    data: function(){
      return {
        result: [],
        year: year,
        month: month,
        week: week[weekIdx],
        target: day,
        ok: false,
        times: ['10:00 ~ 13:00', '13:00 ~ 16:00', '16:00 ~ 19:00'],
        time: ''
      }
    },
    created() {
      this.axios.get('http://localhost:8000/rent/scheduler/' + year + "/" + month + "/")
        .then(response => {
          this.result = response.data.calendar;
        })
        .catch(e => {
          this.errors.push(e)
        });
    },
    methods: {
      dayTarget: function(day, index) {
        var check = /^test$/g;
        var test = document.getElementsByClassName("test");
        console.log(test);
        // test.className = test.className.replace(check, " ").trim();
        event.target.className += " test";
        this.target = day;
        this.week = week[index];

      },
      prevMonth: function() {
        month--;
        if (month < 1) {
          month = 12;
          year--;
          this.year = year;
        }
        this.month = month;
        this.axios.get('http://localhost:8000/rent/scheduler/' + year + "/" + month + "/")
          .then(response => {
            this.result = response.data.calendar;
          })
          .catch(e => {
            this.errors.push(e)
          });
      },
      nextMonth: function() {
        month++;
        if (month > 12) {
          month = 1;
          year++;
          this.year = year;
        }
        this.month = month;
        this.axios.get('http://localhost:8000/rent/scheduler/' + year + "/" + month + "/")
          .then(response => {
            this.result = response.data.calendar;
          })
          .catch(e => {
            this.errors.push(e)
          });
      },
      reserve: function(time) {
        this.ok = true
        this.time = time
      }
    }
  }

  // var searchKeyword = document.getElementById("searchKeyword");
  // var autocomplete = document.getElementById("autocomplete");
  // var keyword = "";
  // searchKeyword.onkeyup = function (e) {
  //   if (e.char) {
  //     keyword = searchKeyword.value;
  //   }
  //
  //   if (searchKeyword.value == "") {
  //     autocomplete.style.display = "none";
  //   } else {
  //     autocomplete.style.display = "block";
  //     fileSearchResult(autocomplete);
  //   }
  // }
  //
  // function fileSearchResult(autocomplete) {
  //   autocomplete.innerHTML = "";
  //   var searchResults = [
  //     "루비 | 기본 요금 200,000(추가 1시간 70,000) | 최대 인원 6",
  //     "자바 | 기본 요금 300,000(추가 1시간 100,000) | 최대 인원 10",
  //     "파이썬 | 기본 요금 500,000(추가 1시간 150,000) | 최대 인원 20"
  //   ];
  //   for (var i=0; i<searchResults.length; i++) {
  //     autocomplete.innerHTML += "<div onclick='selectData(this)' style='margin: 5px 0'>" + searchResults[i] + "</div>";
  //   }
  // }
  //
  // function selectData(that) {
  //   var searchKeyword = document.getElementById("searchKeyword");
  //   searchKeyword.value = (that.innerText).split(" | ")[0];
  //   var autocomplete = document.getElementById("autocomplete");
  //   autocomplete.style.display = "none";
  // }
</script>

<style>
  /* 스케쥴러 페이지 */
  #scheduler {
    /* background-color: #222; */
    margin: 0 5%;
  }

  #scheduler::after {
    content: '';
    display: block;
    clear: both;
  }

  #scheduler .desc {
    width: 45%;
    height: 398px;
    background: #333;
    color: #fafafa;
    float: left;
  }

  #scheduler .desc .date {
    text-align: center;
  }

  #scheduler .desc .date p {
    margin: 20px 0 5px 0;
    font-size: 5.6rem;
    font-weight: 900;
  }

  #scheduler .desc .date hr {
    width: 35px;
    margin-bottom: 25px;
  }

  #scheduler .desc .date span {
    color: #6cc091;
  }

  #scheduler .desc .description {
    padding: 15px;
    margin-top: 40px;
  }

  #scheduler .desc .description .room {
    border-radius: 0;
    font-size: 1.4rem;
    color: #fafafa;
    border-bottom: none;
    padding: 5px 10px;
    cursor: pointer;
  }

  #scheduler .desc .description .active {
    background: rgba(225, 225, 225, 0.3);
  }

  #scheduler .desc .description .no-active {
    background: transparent;
  }

  #scheduler .desc .description .no-active:hover {
    border-top: 1px solid #6cc091;
    border-left: 1px solid #6cc091;
    border-right: 1px solid #6cc091;
    color: #6cc091;
  }

  #scheduler .desc .description ul {
    border: 1px solid #f1f1f1;
    margin: 0;
  }

  #scheduler .desc .description ul li {
    line-height: 35px;
  }

  #scheduler .desc .description ul li .time {
    display: inline-block;
    width: 115px;
  }

  #scheduler .desc .description ul li .reserve {
    background: transparent;
    border: 1px solid #fafafa;
    border-radius: 20px;
    color: #fafafa;
    padding: 5px 10px;
  }

  #scheduler .calendar {
    width: 50%;
    margin: 15px 2.5% 40px 2.5%;
    text-align: center;
    border-collapse: collapse;
    font-weight: bold;
    float: left;
  }

  #scheduler .calendar .month {
    font-size: 2.2rem;
  }

  #scheduler .calendar .month td {
    padding: 25px;
  }

  #scheduler .calendar .month td .prev-next {
    border: none;
    color: #ddd;
    width: 50px;
  }

  #scheduler .calendar .summit {
    color: #8d8d8d;
  }

  #scheduler .calendar .summit td {
    height: 30px;
    line-height: 30px;
    padding-top: 5px;
    margin-bottom: 5px;
    border-top: 2px solid #f2f2f2;
    border-bottom: 2px solid #f2f2f2;
  }

  #scheduler .calendar .row {
    color: pink;
  }

  #scheduler .calendar .row td {
    width: 14.2%;
    height: 40px;
    padding-top: 5px;
  }

  #scheduler .calendar .row td a {
    text-decoration: none;
    color: #5d5d5d;
  }

  /* 대관하기 페이지 */
  #rent {
    height: auto;
    /* background: url("https://s3.ap-northeast-2.amazonaws.com/usedbookstore-bucket/static/images/dryflower.png"); */
    background-repeat: no-repeat;
    background-size: cover;
    padding: 100px 0;
  }

  #rent .form-wrap {
    height: auto;
    background: rgba(0, 0, 0, 0.3);
    width: 80%;
    margin: 0 10%;
    padding: 25px 0;
    position: relative;
  }

  #rent .form-wrap p {
    width: 90%;
    margin: 0 5%;
    margin-bottom: 20px;
    color: #fafafa;
  }

  #rent .form-wrap .room-name {
    width: 90%;
    margin: 0 4%;
    padding: 1%;
    height: 20px;
    border: none;
  }

  #rent .form-wrap #autocomplete {
    width: 90%;
    margin: 0 4%;
    padding: 10px 1%;
    z-index: 3;
    position: absolute;
    top: 97px;
    left: 0px;
    background: #f1f1f1;
    display: none;
  }

  #rent .form-wrap .date-wrap {
    width: 92%;
    margin: 20px 4%;
    float: left;
  }

  #rent .form-wrap .date-wrap .day {
    width: 49.5%;
    margin-right: 0.5%;
    float: left;
  }

  #rent .form-wrap .date-wrap .day .select-left {
    width: 100%;
    border: none;
    border-radius: 0;
    height: 30px;
    background: #333;
    color: #fafafa;
    cursor: pointer;
  }

  #rent .form-wrap .date-wrap .day .target-left {
    width: 98%;
    border: none;
    padding: 1%;
    height: 25px;
    float: left;
  }

  #rent .form-wrap .date-wrap .time {
    width: 49.5%;
    margin-left: 0.5%;
    background: #ddd;
    float: right;
  }

  #rent .form-wrap .date-wrap .time .select-right {
    width: 100%;
    border: none;
    border-radius: 0;
    height: 30px;
    background: #333;
    color: #fafafa;
    cursor: pointer;
  }

  #rent .form-wrap .date-wrap .time .target-right {
    width: 98%;
    border: none;
    padding: 1%;
    height: 25px;
    float: left;
  }

  #rent .form-wrap .regi-btn {
    width: 92%;
    margin: 5px 4%;
    height: 35px;
    border: none;
    border-radius: 0;
    background: #333;
    color: #fafafa;
    cursor: pointer;
    font-size: 1.5rem;
  }
</style>
