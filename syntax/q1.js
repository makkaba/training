// var input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
// console.log(input[0]);
// 

// Run by Node.js

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

T = 0;
isFirst = true;
arr = [];

rl.on("line", function(line) {
    if(isFirst){
        T = line;
        isFirst = false;
        return;
    }
    var temp = line.split(' ');
    arr.push(temp);
    T--;
    
    if(!isFirst && T==0){
        rl.close();
    }
    
    
}).on("close", function() {
    
    solution(arr);
  process.exit();
});

function solution(arr){
    console.log(arr);
}

/*
function visible(a) {
    var R  =  ''
    for (var i = 0; i < a.length; i++) {
        if (a[i] == '\b') {  R -= 1; continue; }  
        if (a[i] == '\u001b') {
            while (a[i] != 'm' && i < a.length) i++
            if (a[i] == undefined) break
        }
        else R += a[i]
    }
    return  R
}

function empty(a) {
    a = visible(a)
    for (var i = 0; i < a.length; i++) {
        if (a[i] != ' ') return false
    }
    return  true
}

var readline = require('readline')
var rl = readline.createInterface({ input: process.stdin, output: process.stdout, terminal: false })

rl.on('line', function(line) {
    if (!empty(line)) console.log(line) 
})


*/