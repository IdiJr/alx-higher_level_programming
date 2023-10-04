$(document).ready(function () {
  $('DIV#add_item').click(function () {
    const addItem = $('<li>Item</li>');
    $('ul.my_list').append(addItem);
  });
});
