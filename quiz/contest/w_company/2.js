// Run by Node.js

const readline = require('readline')

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
})

rl.question("Input", function(chunk) {
    //700 400 1600 1100 0 400 1100 900 900 0 1800 650
  var points = chunk.toString().split(" ");
  var x1 = Number(points[0]);
  var y1 = Number(points[1]);
  var x2 = Number(points[2]);
  var y2 = Number(points[3]);
  var x3 = Number(points[4]);
  var y3 = Number(points[5]);
  var x4 = Number(points[6]);
  var y4 = Number(points[7]);
  var x5 = Number(points[8]);
  var y5 = Number(points[9]);
  var x6 = Number(points[10]);
  var y6 = Number(points[11]);
	
  //여기부터 작성해 주세요
	var vol = (x2-x1)*(y2-y1);
    console.log("vol", vol);
	var result = vol - getDupVol(x1, y1, x2, y2, x3, y3, x4, y4) 
		- getDupVol(x1, y1, x2, y2, x5, y5, x6, y6) 
		+ getDupVol(x5, y5, x6, y6, x3, y3, x4, y4);
	
	console.log(result);
  rl.close()
});

function getDupVol(x1, y1, x2, y2, x3, y3, x4, y4){
	var width = 0;
	var height = 0;
	if(x1 >= x3){
        console.log('x1');
		width = x4 - x1;
	}else{
        console.log('x2');
		width = x2 - x3;
	}
	
	if(y1 >= y3){
        console.log('y1');
		height = y4-y1;
	}else{
        console.log('y2');
		height = y2 - y3;
	}
	var result = width*height;
    
    console.log("width",width, "height", height);
    console.log("each", result);
	return result;
	
}