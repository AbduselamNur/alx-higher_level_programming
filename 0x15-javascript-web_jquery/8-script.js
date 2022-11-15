$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data, status) {
  $.each(data.results, function (i, v) {
    $('UL#list_movies').append(v.title);
  });
});
