// Run by Node.js
const readline = require('readline')

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
})

rl.question("Input", function(chunk) {
  var numbers = chunk.toString().split(" ");
  var n = Number(numbers[0]);
  var d = Number(numbers[1]);
  var k = Number(numbers[2]);
  var j = Number(numbers[3]);

  
	var move = 0;
	var cur = 0;
	var delCount = 0;
	var dir = 1;
    var endCount=0;
    
	//여기부터 작성해 주세요
	if(d==1){
		dir = 1;
	}else{
		dir = -1;
	}
	
	var people = new Array(n);
	for (var i=0; i<n; i++){
		people[i] = i+1;
	}
	//초기화끝.
	while(delCount < n-1){
		move = 0;
        console.log("outer while");
		while(move != k && endCount<100){
            endCount++;
            console.log("move", move, "k", k, "cur:",cur);
            console.log(people);
            console.log('index:', (cur+1)%n);
			//실제 이동한 거리==k이면 중지시키는 와일
			if(people[(cur+1)%n] == -1){
				//이미 탈락한 사람
                cur = (cur+1)%n;
				continue;
			}else{
				//아니면 한칸씩 전진.
				move++;
				cur = (cur+1)%n;
			}
		}
		//탈락자를 제외하고 실제 이동 끝.
		//탈락시킨다.
		people[cur] = -1;
		delCount++;
		k = k+j;
	}
	//한명 남으면 종료.
	var result = people.filter(function(value){
		return value != -1;
	});
	console.log(result);
	
	
	
	
  rl.close()
});
