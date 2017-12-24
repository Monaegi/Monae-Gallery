<template>
  <div id="rent">
    <section class="form-wrap">
      <p>대관하기</p>
      <form action="">
        <input type="text" class="room-name" id="searchKeyword" placeholder="어떤 룸을 대관하시나요?" />
        <div id="autocomplete"></div>
        <article class="date-wrap">
          <div class="day">
            <button class="select-left">날짜 선택</button>
            <input type="text" class="target-left" placeholder="날짜를 선택하세요." readonly>
          </div>
          <div class="time">
            <button class="select-right">시간 선택</button>
            <input type="text" class="target-right" placeholder="시간을 선택하세요." readonly>
          </div>
        </article>
        <button class="regi-btn">예약하기</button>
      </form>
    </section>
  </div>
</template>

<script type="text/javascript">
  var searchKeyword = document.getElementById("searchKeyword");
  var autocomplete = document.getElementById("autocomplete");
  var keyword = "";

  searchKeyword.onkeyup = function (e) {
    if (e.char) {
      keyword = searchKeyword.value;
    }

    if (searchKeyword.value == "") {
      autocomplete.style.display = "none";
    } else {
      autocomplete.style.display = "block";
      fileSearchResult(autocomplete);
    }
  }

  function fileSearchResult(autocomplete) {
    autocomplete.innerHTML = "";
    var searchResults = [
      "루비 | 기본 요금 200,000(추가 1시간 70,000) | 최대 인원 6",
      "자바 | 기본 요금 300,000(추가 1시간 100,000) | 최대 인원 10",
      "파이썬 | 기본 요금 500,000(추가 1시간 150,000) | 최대 인원 20"
    ];
    for (var i=0; i<searchResults.length; i++) {
      autocomplete.innerHTML += "<div onclick='selectData(this)' style='margin: 5px 0'>" + searchResults[i] + "</div>";
    }
  }

  function selectData(that) {
    var searchKeyword = document.getElementById("searchKeyword");
    searchKeyword.value = (that.innerText).split(" | ")[0];
    var autocomplete = document.getElementById("autocomplete");
    autocomplete.style.display = "none";
  }
</script>
<style>
body {
  margin: 0;
  padding: 0;
}

.container {
  height: auto;
  background: url("https://s3.ap-northeast-2.amazonaws.com/usedbookstore-bucket/static/images/dryflower.png");
  background-repeat: no-repeat;
  background-size: cover;
  padding: 100px 0;
}

.container .form-wrap {
  height: auto;
  background: rgba(0, 0, 0, 0.3);
  width: 80%;
  margin: 0 10%;
  padding: 25px 0;
  position: relative;
}

.container .form-wrap p {
  width: 90%;
  margin: 0 5%;
  margin-bottom: 20px;
  color: #fafafa;
}

.container .form-wrap .room-name {
  width: 90%;
  margin: 0 4%;
  padding: 1%;
  height: 20px;
  border: none;
}

.container .form-wrap #autocomplete {
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

.container .form-wrap .date-wrap {
  width: 92%;
  margin: 20px 4%;
  float: left;
}

.container .form-wrap .date-wrap .day {
  width: 49.5%;
  margin-right: 0.5%;
  float: left;
}

.container .form-wrap .date-wrap .day .select-left {
  width: 100%;
  border: none;
  border-radius: 0;
  height: 30px;
  background: #333;
  color: #fafafa;
  cursor: pointer;
}

.container .form-wrap .date-wrap .day .target-left {
  width: 98%;
  border: none;
  padding: 1%;
  height: 25px;
  float: left;
}

.container .form-wrap .date-wrap .time {
  width: 49.5%;
  margin-left: 0.5%;
  background: #ddd;
  float: right;
}

.container .form-wrap .date-wrap .time .select-right {
  width: 100%;
  border: none;
  border-radius: 0;
  height: 30px;
  background: #333;
  color: #fafafa;
  cursor: pointer;
}

.container .form-wrap .date-wrap .time .target-right {
  width: 98%;
  border: none;
  padding: 1%;
  height: 25px;
  float: left;
}

.container .form-wrap .regi-btn {
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
