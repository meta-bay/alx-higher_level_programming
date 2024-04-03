const header = $('header');
const toggleHeader = $('DIV#toggle_header');
toggleHeader.on('click', () => {
    header.toggleClass('red green');
});
