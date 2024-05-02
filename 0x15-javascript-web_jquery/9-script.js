//script that fetchesand displays the value of hello

let url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
$.get(url, function (data) {
  let hellotext = data.hello;
  $('div#hello').text(hellotext);
});
