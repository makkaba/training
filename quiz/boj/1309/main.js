// 미완료.
// 왜 컴파일 에러 나는지 모르겠음.


const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

var num = 0;

rl.on("line", function(line) {
    num = parseInt(line,10);
    rl.close();
}).on("close", function() {
    
    solution(num);
  process.exit();
});

function solution(num){
    
    var dp = [];
    if(num <=0){
        console.log(1%9901);
        return;
    }
    for(var i =0; i<num; i++){
        var temp = new Array(3).fill(0);
        dp.push(temp);
    }
    console.log(dp);
    
    dp[0][0] = 1;
    dp[0][1] = 1;
    dp[0][2] = 1;
    //초기화 끝.
    

    
    for(var i=1; i<num; i++) {
        
        dp[i][0] = dp[i-1][0] + dp[i-1][1] + dp[i-1][2];
        dp[i][1] = dp[i-1][0] + dp[i-1][2];
        dp[i][2] = dp[i-1][0] + dp[i-1][1];
        dp[i][0] = dp[i][0]%9901;
        dp[i][1] = dp[i][1]%9901;
        dp[i][2] = dp[i][2]%9901;
        
    }
    var result = dp[num-1][0] + dp[num-1][1] + dp[num-1][2];
    result = result%9901;
    
    console.log(result);
    return;
}