function sum(a, b) {
  return a + b;
}
module.exports = sum;

// when run directly with `node sum.js` it will print a demo result
if (require.main === module) {
  console.log(sum(1, 2)); // should print 3
}
