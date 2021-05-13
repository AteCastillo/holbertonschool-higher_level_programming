const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
jQuery.getJSON(url, function (data) {
  list = data.results;
  list.forEach(element => {
    $('UL#list_movies').append(`<li>${element.title}</li>`);
  });
});
