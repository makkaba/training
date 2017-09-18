#include <cstdio>
#include <iostream>
using namespace std;

int findPattern(char*, char*);

int main(){	
	int result;
	char source[] = {"helloworld"};
	char pattern[] = {"low"};

	result = findPattern(source, pattern);
	cout<<"result:"<<result;

	return 0;
}

int findPattern(char *source, char* pattern){
	int i,j;
	int lastIndexSource = strlen(source) - 1;
	int lastIndexPattern = strlen(pattern) - 1;
	//패턴의 시작점과 종료지점은 같이 움직인다.
	int matchStart = 0;
	int matchEnd = strlen(pattern) - 1;
	int compareIndex;
	
	cout<<"lastIndexSource:"<<lastIndexSource<<" lastIndexPattern:"<<lastIndexPattern<<"\n";

	for(i=lastIndexPattern; i<strlen(source); i++, matchStart++){
		cout<<"i:"<<i<<"\n";
		if(pattern[lastIndexPattern] == source[i]){
			matchEnd=i;
			cout<<"in IF statement\n"<<"matchEnd:"<<matchEnd<<"\n";
			for(j=0, compareIndex = matchStart; compareIndex < matchEnd && source[compareIndex] == pattern[j]; j++, compareIndex++){
				cout<<"J:"<<j<<"\n";
			}
			if(j == lastIndexPattern){
				return matchStart;
			}
		}
		
	}
	
	return -1;
}

