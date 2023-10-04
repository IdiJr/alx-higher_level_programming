$(document).ready(function () {
  const characterLink = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
  $.get(characterLink, function (data) {
    $('DIV#character').text(data.name);
  });
});
