<template>
  <aside id="main_calendar">
    <ul class="calendar_warpper wrapper">
      <li class="month_wrapper wrapper">
        <span class="month">{{month}}</span>
        <span class="year">{{year}} {{english_month[month - 1]}}</span>
      </li>
      <li class="day_wrapper wrapper">
        <ul class="day_list">
          <li class="day" v-for="(day, index) in getMonthDay" :key="index">
            <button class="day_button effect" :class="today == day ? 'today' : ''">{{day}}</button>
          </li>
        </ul>
      </li>
    </ul>
    <button class="prev_button move_button" @click="prevMonth"><i class="fa fa-angle-left effect" aria-hidden="true"></i></button>
    <button class="next_button move_button" @click="nextMonth"><i class="fa fa-angle-right effect" aria-hidden="true"></i></button>
  </aside>
</template>

<script>
const date = new Date()
export default {
  data() {
    return {
      date: date,
      year: date.getFullYear(),
      month: date.getMonth()+1,
      today: date.getDate(),
      month_day: [],
      errors: '',
      english_month: ['January', 'Febuary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    }
  },
  computed: {
    getMonthDay: function() {
      let all_day_list = []
      this.month_day.forEach(element => element.forEach(value => value != 0 ? all_day_list.push(value) : ''));
      return all_day_list
    }
  },
  methods: {
    prevMonth: function() {
      if(this.month - 1 == 0) {
        this.year--;
        this.month = 12
      } else {
        this.month--;
      }
      this.checkToday();
      this.getData();
    },
    nextMonth: function() {
      if(this.month + 1 == 13) {
        this.year++;
        this.month = 1
      } else {
        this.month++;
      }
      this.checkToday();
      this.getData();
    },
    checkToday: function() {
      this.year == date.getFullYear() && this.month == (date.getMonth() + 1) ? this.today = date.getDate() : this.today = 1;
    },
    getData: function() {
      this.axios.get('http://localhost:8000/rent/scheduler/' + this.year + "/" + this.month + "/")
      .then(response => this.month_day = response.data.calendar)
      .catch(e => this.errors.push(e))
    }
  },
  created: function() {
    this.getData();
  }
}
</script>

<style scoped>
#main_calendar{
  position: relative;
  height: 10vh;
}
.calendar_warpper{
  position: absolute;
  left: 0;
  right: 0;
  padding: 0 40px;
}
.wrapper{
  line-height: 5vh;
  height: 5vh;
}
.month{
  border-bottom: 2px solid #a58a78;
  margin: 0 5px;
  padding: 0 5px;
  color: #a58a78;
  font-size: 3.5rem;
  font-weight: bold;
}
.year{
  font-size: 1.5rem;
}
.day_list{
  display: flex;
  justify-content: space-around;
}
.day_button{
  padding: 8px;
  border-radius: 100px;
  font-size: 1.5rem;
}
.day_button:hover, .day_button:focus{
  background-color: #777;
  color: white;
}
.move_button{
  height: 10vh;
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
}
.move_button i{
  color: #a58a78;
  font-size: 4rem;
  opacity: 0.5;
  padding: 0 5px;
}
.move_button i:hover{
  opacity: 1;
  color: #222;
}
.prev_button{
  left: 0;
}
.next_button{
  right: 0;
}
.today{
  background-color: #a58a78;
  color: white;
}
</style>

