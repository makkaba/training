#include <cstdio>
#include <iostream>
using namespace std;
void selectionSort(int [], int);

int main(){
	int list[] = {5,1,2,4,3};
	selectionSort(list, 5);

	for(int i=0; i<5; i++){
		cout<<list[i]<<"\n";
	}
	return 0;
}

void selectionSort(int list[], int size){
	int min, temp;
	
	for(int i=0; i<size; i++){
		min = i;
		for(int next=0; next<size-1; next++){
			if(list[min] > list[next]){
				temp = list[min];
				list[min] = list[next];
				list[next] = temp;
			}
		} 
	}
}

