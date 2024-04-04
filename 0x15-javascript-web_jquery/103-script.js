function sayHello () {
  const urlLang = 'https://hellosalut.stefanbohacek.dev/?lang=';
  const urlToLang = urlLang + $('INPUT#language_code').val();
  $.ajax({
    type: 'POST',
    url: urlToLang,
    success: function (lang) {
      $('DIV#hello').text(lang.hello);
    }
  });
}

window.onload = () => {
  $('input#btn_translate').click(() => {
    sayHello();
  });

  $('input#language_code').keydown((event) => {
    if (event.key === 'Enter') {
      sayHello();
    }
  });
};
