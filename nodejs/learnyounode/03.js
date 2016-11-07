var fs = require('fs');
var buf = fs.readFileSync(process.argv[2]);
//console.log(buf);
var str = buf.toString();
//console.log(str);
var n = str.split('\n').length-1;
console.log(n);
