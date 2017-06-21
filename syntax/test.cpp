#include <string>
#include <utility>
#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

int solution(string a);


int main(){
  int result;
  
  string str = '22001';
  result = solution(str);
  cout<<result;
  return 0;
  
}


int solution(string N) {
    int even =0;
    int answer = 0;
    int size = N.size();
    int cnt;
    int j=0;
    
    
    const char* n = N.c_str();
    vector<char> str;
    
    vector<char> temp;
    
    
    for(int i=0; i<size; i++){
        str[i] = n[i];
    }
    for(int i=0; i<size; i++){
        cnt = count(str.begin(), str.end(), str[i]);
        if(cnt == 2){
            even++;
            temp[j++]= str[i];
        }
    }
    if(even < 2){
        auto it = find(temp.begin(), temp.end(), '0');
        if(it==temp.end()){
            return 0;
        }
        
    }
    answer = (even*2)+1;
    
    return answer;
}