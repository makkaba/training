void quickSort(int arr[], int left, int right){

	int i=left;
	int j=right;
	int pivot = arr[(left+right)/2];
	int temp;

	do {
		//원하는 구도: pivot보다 작은값이 왼쪽에, 큰값이 오른쪽에 몰려있는 형태.

		//피봇의 왼쪽을 차례로 훑으면서 원하는 구도대로 되어있으면 넘어간다.
		while(arr[i] < pivot)
			i++;
		//피봇의 오른쪽 끝부터 피봇쪽으로 훑으면서 원하는 구도대로 되어있으면 넘어간다.
		while(pivot < arr[j])
			j--;


		if(i<=j){
			//역전이 안됐으면 스왑한다
			temp = arr[i];
			arr[i] = arr[j];
			arr[j] = temp;
			//얘네는 제자리 찾은 애들이니까 넘어가도록 처리.
			i++;
			j--;
		}
		//i와 j가 크로스되면 끝낸다.
	}while(i <= j);

	if(left < j){
		quickSort(arr, left, j);
	}
	if(i < right){
		quickSort(arr, i, right);

	}

}
