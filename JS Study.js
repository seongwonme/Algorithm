# 이진수 변환 
let a = 3
a.toString(2) // "11" 이진수 리턴

# Input 덧셈
var fs = require('fs');
var input = fs.readFileSync('/dev/stdin').toString().split(' '); //모든 문자열이 들어온다.
var a = parseInt(input[0]);
var b = parseInt(input[1]);
console.log(a+b);
