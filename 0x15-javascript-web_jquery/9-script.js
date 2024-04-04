$.ajax({
  type: 'GET',
  url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
  success: function (hello) {
    $('DIV#hello').text(hello.hello);
  }
});
