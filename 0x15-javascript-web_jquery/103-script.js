$(document).ready(function () {
  $('INPUT#btn_translate').click(fetchTranslation);
  $('INPUT#language_code').keypress(function (event) {
    if (event.keyCode === 13) {
      fetchTranslation();
    }
  });

  function fetchTranslation () {
    const languageCode = $('INPUT#language_code').val();
    const translationUrl = `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`;
    $.get(translationUrl, function (data) {
      const translation = data.hello;
      $('DIV#hello').text(translation);
    });
  }
});
