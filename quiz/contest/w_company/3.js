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
    var maxNum = 0;
    var result = [];
    for(var i=0; i<arr.length; i++){
        maxNum = Math.max(arr[i][1], maxNum);
    }
    var a = new Array((maxNum+1)*2).fill(0);
    var cur = 0;
    
    console.log(arr.length);
    
    for(var i=0; i<arr.length; i++){
        var start = (arr[i][0])*2;
        var end = (arr[i][1])*2;
        
        // console.log(start);
        // console.log(end);
        
        for(var j=start; j<=end; j++){
            a[j]++;
            
        }
        
        
    }
    
    
    var first =0;
    while(a[first] == 0){
        first++;
    }
    first = Math.floor(first/2);
    result.push("(-, "+first+")");
    //첫번째끝.
    
    var f=first+1;
    
    for(var i=first+1; i<(maxNum+1)*2; i++){
        
        //짝수개 이면, 계속 전진
        if(a[i]%2 == 0){
            continue;
        }else{
            //홀수개 이면 누적된거 계산해서 짝수 범위취합
            if(f<i-1){
                
                result.push("["+Math.floor(f/2)+", "+Math.floor(((i-1)/2))+"]");
            }else if (f<i) {
                console.log("f:",f,"i",i);
                result.push("("+Math.floor(f/2)+", "+(Math.floor(f/2)+1)+")");
            }
            
            f = i+1;
            
        }
        
    }
    
    result.push("("+maxNum+", "+"+)");
    
    
    
    for(var i=0; i<result.length; i++){
        console.log(result[i]);
    }
    
}