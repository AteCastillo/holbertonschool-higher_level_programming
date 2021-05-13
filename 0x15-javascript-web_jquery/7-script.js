const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
jQuery.getJSON(url, function (data) {
  $('DIV#character').text(data.name);
});
// function(data){} is like (data) => {}
