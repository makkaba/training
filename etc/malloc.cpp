/*
malloc: 사용할 수 있는 메모리의 시작 주소 포인터값을 리턴해준다
   */

int i, *pi;
float pi_detail;

pi = (int*)malloc(sizeof(int));
pi_detail = (float*)malloc(sizeof(float));

if(pi == NULL || pi_detail == NULL){
	exit((EXIT_FAILURE);
}

*pi = 1024;
*pi_detail = 3.14;

free(pi);
free(pi_detail);

