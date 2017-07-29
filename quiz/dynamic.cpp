#include <iostream>

using namespace std;
int d[100] = {0}

int shortestNum(n){
    int temp;
    
    //기저조건
    if(n==1){
        return 0;
    }
    
    

    //리컬시브
    //1. subtract one
    d[n] = shortestNum(n-1) + 1;

    //2. divide with 3
    if(n%3==0){
        //3으로 나누는게 더 작으면 교체
        temp = shortestNum(n/3) + 1;
        if(temp < d[n]){
            d[n] = temp;
        }
    }else if(n%2==0){
        //2로 나누는게 더 작으면 교체 
        temp = shortestNum(n/2) + 1;
        if(temp < d[n]){
            d[n] = temp;
        }
    }
    return d[n];
}

int main(){
     

    cin>>n;
    cout<<shortestNum(n);
    return 0;
}
