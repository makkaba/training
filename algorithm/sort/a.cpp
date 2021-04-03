void quickSort(int arr[], int left, int right){
	//L: pivot보다 작은 사람들이 앞에 있는지 체크하는 사람. 이상한 사람이 있으면 멈춘다.
	//R: pivot보다 큰 사람들이 뒤에 있는지 체크하는 사람. 이상한 사람이 있으면 멈춘다.
	//계속 전진하다가 둘이 크로스 될때 '이상 없습니다'라고 보고한다.
	int L = left;
	int R = right;
	
	do{
	
		while(arr[L] < pivot){
			L++;
		}
		
		while(pivot < arr[R]){
			R--;
		}
		
		//아직 크로스되지 않았다?=>뭔가 문제가 있다.
		if(L<=R){
			temp = arr[L];
			arr[L] = arr[R];
			arr[R] = temp;
			
			//처리했으니까 다음!
			L++;
			R--;
		}
	}while(L<=R);
	
	
	
	if(left < R){
		quickSort(arr, left, R);
	}
	
	if(L < right){
		quickSort(arr, L, right);
	}
	
}