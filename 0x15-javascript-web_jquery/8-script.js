$(document).ready(function () {
  const moviesLink = 'https://swapi-api.alx-tools.com/api/films/?format=json';
  $.get(moviesLink, function (data) {
    const movies = data.results;
    for (let i = 0; i < movies.length; i++) {
      const movieTitle = movies[i].title;
      $('UL#list_movies').append($('<li>').text(movieTitle));
    }
  });
});
