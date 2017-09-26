#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int n;


int main(){
    n=0;
    
    cin>>n;
    
    vector<int> price(n+1);
    vector<int> dp(n+1);
    
    for(int i=0; i<n; i++){
        cin>>price[i];
    }
    
    for(int i=1; i<=n; i++){
        for(int j=1; j<=i; j++){
            dp[i] = max(dp[i], dp[i-j]+price[j]);
        }
    }
    
    cout<<dp[n]<<'\n';

    
    
    return 0;
    
}