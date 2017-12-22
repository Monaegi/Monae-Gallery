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
