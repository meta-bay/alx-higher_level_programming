const header = $('header');
const redHeader = $('DIV#red_header');
redHeader.on('click', () => {
  header.addClass('red');
});
