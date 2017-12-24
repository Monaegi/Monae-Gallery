<template>
  <div id="scheduler">
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
            <li>
              <span class="time">10:00 ~ 13:00</span>
              <button class="reserve">예약 가능</button>
            </li>
            <li>
              <span class="time">13:00 ~ 16:00</span>
              <button class="reserve">예약 가능</button>
            </li>
            <li>
              <span class="time">16:00 ~ 19:00</span>
              <button class="reserve">예약 가능</button>
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
        <td>MON</td>
        <td>TUE</td>
        <td>WED</td>
        <td>THU</td>
        <td>FRI</td>
        <td>SAT</td>
        <td>SUN</td>
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

<script>
  var today = new Date();
  var year = today.getFullYear();
  var month = today.getMonth() + 1;
  var day = today.getDate();
  var weekIdx = today.getDay() - 1;
  var week = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
  export default {
  name: 'scheduler',
  data: function(){
    return {
      result: [],
      year: year,
      month: month,
      week: week[weekIdx],
      target: day
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
      }
    }
  }
</script>
<style>
#scheduler {
  background-color: #222;
  margin: 0 5%;
}

#scheduler::after {
  content:'';
  display:block;
  clear:both;
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

</style>
