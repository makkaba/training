function solution(N) {
    var answer = 0;
    var lhs = [];
    var arr = N.split("");
    var even = 0;
    
    for(var i=0; i<arr.length; i++){
        console.log(arr[i]);
        if( -1 != lhs.indexOf(arr[i])){
            //이미 존재한다면
            console.log("exist");
            even++;
        }else{
            //없다면 추가
            console.log("not exist");
            lhs.push(arr[i]);    
        }
    }
    
    if(arr.length < 4 && lhs.indexOf('0') != -1 ){
        return 0;
    }
    console.log("even", even);
    answer = even*2 +1;
    return answer;
}