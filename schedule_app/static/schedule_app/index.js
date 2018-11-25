"use strict";

(function() {

  function $(id) { return document.getElementById(id); }

  window.onload = function() {
    $("course-find").onclick = fetchCourses;
    $("clear").onclick = clear;
  }

  function fetchCourses() {
    fetch("http://localhost:8000/list/")
      .then(checkStatus)
      .then(JSON.parse)
      .then(displayCourses)
      .catch()
  }

  function displayCourses(response) {
    $("course").innerHTML = "";
    $("professor").innerHTML = "";
    $("semester").innerHTML = "";
    $("year").innerHTML = "";
    let query = $("prefix").value.toLowerCase();
    for (let i = 0; i < response.length; i++) {
      if (query == response[i]["prefix"]) {
        let course = document.createElement("p");
        let professor = document.createElement("p");
        let semester = document.createElement("p");
        let year = document.createElement("p");
        course.innerHTML = (response[i]["prefix"]).toUpperCase() + " " + response[i]["number"];
        professor.innerHTML = capF(response[i]["professor"]);
        semester.innerHTML = capF(response[i]["semester"]);
        year.innerHTML = response[i]["year"];

        $("course").appendChild(course);
        $("professor").appendChild(professor);
        $("semester").appendChild(semester);
        $("year").appendChild(year);
      }
    }
  }

  function clear() {
    $("course").innerHTML = "";
    $("professor").innerHTML = "";
    $("semester").innerHTML = "";
    $("year").innerHTML = "";
    $("prefix").value = "";
  }

  function capF(string) {
    return string.charAt(0).toUpperCase() + string.slice(1);
}

  function checkStatus(response) {
    if (response.status >= 200 && response.status < 300) { return response.text(); }
    else { return Promise.reject(new Error(response.status + ": " + response.statusText)); }
  }





















})();
