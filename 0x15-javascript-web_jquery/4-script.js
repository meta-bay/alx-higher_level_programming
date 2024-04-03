const header = $('header');
const toggleHeader = $('DIV#toggle_header');
toggleHeader.on('click', () => {
  if (header.hasClass('red')) {
    header.removeClass('red').addClass('green');
  } else {
    header.removeClass('green').addClass('red');
  }
});
