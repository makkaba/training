//숫자 하나 받는 포맷
const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

T = 0;
isFirst = true;

rl.on("line", function(line) {
    if(isFirst){
        T = line;
        isFirst = false;
        return;
    }
    rl.close();
    
    
    
}).on("close", function() {
    
    solution(T);
  process.exit();
});

function solution(arr){
    console.log(arr);
}




//1차원 숫자 배열 받는 템플릿

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
    arr = line.split(' ').map(function(num){ return parseInt(num, 10)});
    rl.close();
}).on("close", function() {
    
    solution(arr, T);
  process.exit();
});

//2차원 배열 받는 포맷
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
    var temp = line.split(' ').map(function(num){ return parseInt(num,10);});
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