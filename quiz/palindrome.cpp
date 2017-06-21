//주어진 숫자로 만들 수 있는 팰린드롬의 최대 길이는?
//단, 0으로 시작할 수 없다.

#include <cstdio>
#include <iostream>

int solution(int[], int);
using namespace std;


int main(){
    
    int arr[] = {1,2,3,3,4,3,2,0,3,3};
    int result;
    
    
    result = solution(arr, sizeof(arr)/sizeof(*arr));
    cout<<"result:"<<result<<'\n';
    
    
    return 0;
}
 

int solution(int src[], int size){
    int answer = 0;
    int cnt[10] = {0};
    int num =0;
    int odd =0;
    bool zeroException= true;
    
    for(int i=0; i<size; i++){
        cout<<src[i]<<' ';
        num = src[i];
        cnt[num] = cnt[num] +1;
        //0이 아닌 숫자인데 2개 이상 있는 경우가 한번이라도 있으면
        if(num != 0 && cnt[num] > 1 ){
            zeroException = false;
        }
    }
    
    //예외 처리
    //0만 가지고는 팰린들럼을 만들 수 없다.
    if(zeroException){
        return 0;
    }
    
    //normal case
    for(int i=0; i<10;i++){
        
        //홀수
        if(cnt[i]%2 != 0){
            answer = answer + (cnt[i] - 1);
            odd = 1;
            //홀수가 하나라도 있으면 더해준다
            //ex) 22122
        }else{
            answer = answer + cnt[i];
        }
    }

    answer = answer + odd;
    
    
    
    return answer;
}