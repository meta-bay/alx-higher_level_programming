document.addEventListener('DOMContentLoaded', () => {
  $('INPUT#btn_translate').on('click', () => {
    const urlLang = 'https://hellosalut.stefanbohacek.dev/?lang=';
    const urlToLang = urlLang + $('INPUT#language_code').val();
    $.ajax({
      type: 'GET',
      url: urlToLang,
      success: function (lang) {
        $('DIV#hello').text(lang.hello);
      }
    });
  });
});
