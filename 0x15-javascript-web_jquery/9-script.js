const url = 'https://fourtonfish.com/hellosalut/?lang=fr';
jQuery.getJSON(url, function (data) {
  $('DIV#hello').text(data.hello);
});
