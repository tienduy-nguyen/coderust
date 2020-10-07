var x = 3;
var y = 0;
function testY() {
  y++;
  return true;
}
if (x >= 3 && testY()) {
  y++;
}
if (x < 3 || testY()) {
  y++;
}
if (x < 3 && testY()) {
  y++;
}
if (x >= 3 || testY()) {
  y++;
}
var z = y;
console.log(z);
