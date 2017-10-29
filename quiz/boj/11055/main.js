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

function solution(arr, size){
    var dp = arr.slice();

    for(var i=1; i<size; i++){
        for(var j=0; j<i; j++){
            if(arr[j]< arr[i]){
                dp[i] = Math.max(dp[i], dp[j]+arr[i]);
            }
            
        }
    }
    
    
    
    // var result = Math.max(...dp);
    var result= dp.reduce(function(prev, cur){ return prev> cur ? prev: cur; });
    
    
    console.log(result);
    
}
