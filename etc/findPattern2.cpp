#include <cstdio>
#include <iostream>
using namespace std;

int findPattern(char*, char*);

int main(){	
	int result;
	char source[] = {"helloworld"};
	char pattern[] = {"owo"};

	result = findPattern(source, pattern);
	cout<<"result:"<<result;

	return 0;
}

int findPattern(char* string, char* pattern){
	int i,j,k;
	int lastp = strlen(pattern) - 1;
	int lasts = strlen(string) - 1;
	int matchStart = 0, matchEnd = lastp;
	
	for(i=lastp; i<lasts; i++, matchStart++, matchEnd++){
		cout<<"i:"<<i<<"\n";
		
		if(string[i] == pattern[lastp]){
			//마지막 글자를 찾았으니 앞글자 검사
			k = matchStart;
			for(j=0; j<lastp && pattern[j] == string[k]; j++, k++){
				cout<<pattern[j]<<"="<<string[k]<<"\n";
			}
			//마지막 글자를 보여주기 위해서
			cout<<pattern[j+1]<<"="<<string[k]<<"\n";
			//마지막 글자까지 일치했었는지 체크
			if(j == lastp){
				return matchStart;
			}
			//마지막 글자가 일치했지만 단어가 일치하지 않은 경우, 다시 실행
		}

	}
	return -1;
}

