function solution(n,m) {
    
    
    var a = new Array(m).fill(0);
    var b = [];
    for(var i =0; i<n; i++){
        b.push(a);
    }
    return b;
}

var result = solution(3,5);
console.log(result[2][3]);