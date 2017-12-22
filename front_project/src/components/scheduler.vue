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
