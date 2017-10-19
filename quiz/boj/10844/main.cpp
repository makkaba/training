#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;



int main(){
    int n;
    int D[100][10];
    int sum=0;
    cin>>n;
    
    
    //base condition
    for(int i=0; i<10; i++){
        if(i==0){
            D[1][i] = 0;
        }else{
            D[1][i] = 1;
        }
    }
    
    
    for(int i=2; i<n+1; i++){
        for(int j=0; j<10; j++){
            if(j==0 || j==9){
                int delta = (j==0 ? 1:-1);
                D[i][j] = D[i-1][j+delta];
            }else{
                D[i][j] = D[i-1][j-1]+D[i-1][j+1];
            }
            
        }
        
    }
    for(int i=0; i<10; i++){
        sum += D[n][i];
    }
    
    cout<<sum<<'\n';
    
    return 0;
    
}