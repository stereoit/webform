window.onload = function() {
  var p = document.getElementById('translated-text');
  p.innerText = gettext('welcomesite') + get_format('DATE_FORMAT');;
}
