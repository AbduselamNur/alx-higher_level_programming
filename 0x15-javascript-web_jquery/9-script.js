$.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data, status) {
  $('DIV#hello').append(data.hello);
});
