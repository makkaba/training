#include <string>
#include <utility>
#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;
void printCount();
void printCountIf();
void printFind();
void printReverse();
int solution(string );


int main(){
  int result;
  
  result = solution('22001');
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


void printCount(){
  vector<int> a = {1,4,1,2,4,2,4,2,2,2,2,3,4};
  for (int i=1; i<=5; i++){
    cout<<i<<"의 개수: "<<count(a.begin(), a.end(), i);
    cout<<"\n";
  }  
}
void printCountIf(){
  //count_if에는 세번째 인수에 조건함수를 넣어줘야 하는데,
  // 람다함수를 써주는 것이 편하다
  vector<int> a = {1,4,1,2,4,2,4,2,2,2,2,3,4};
  int even = count_if(a.begin(), a.end(), [](int x){
    return x % 2 == 0;
  });
}

void printFind(){
    vector<int> a = {1,2,4,4,3,3,2,3};
    for(int i=1; i<=5; i++){
      auto it = find(a.begin(), a.end(), i);
      cout<< i << "의 위치:";
      if(it == a.end()){
        cout<<"cannot find";
      }else{
        cout<<(it-a.begin());
      }
      
    }
}
void printReverse(){
  vector<int> a = {1,4,1,2,3,4,2,4};
  for(int x : a){
    cout<<x<<' ';
  }
  
  cout<<"\n";
  reverse(a.begin(), a.end());
  for(int x : a){
    cout<<x<<' ';
  }
  cout<<'\n';
}

void printRotate(){
  //mid부터 end까지가 앞으로 이동
  vector<int> a= {0,1,2,3,4,5};
  rotate(a.begin(), a.begin()+2, a.end());
  for(int x:a){
    cout<<x<<' ';
  }
}

void printSwap(){
  int a=10, b=20;
  swap(a,b);
  cout<<"a:"<<a<<"b:"<<b;
}

void forLoop(){
  for(auto it=a.begin(); it!=last; ++it){
    cout<<*it;
  }
}