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
    
    for(int i=1; i<=n; i++){
        cin>>price[i];
    }
    
    
    for(int i=1; i<=n; i++){
        for(int j=1; j<=i; j++){
            //매 루프마다 모든 경우의 수를 따져서 
            //i개를 팔 때 최대 이득을 계산한다.
            //i= 2개면, 1개로 만드는 최대값 + 1개를 세트로 팔았을때 가격
            //0개로 만드는 최대값 + 2개셋트를 팔았을 때 가격
            //두 개를 을 비교해서 더 큰거를 취한다.
            cout<<"provedProfit["<<i<<"],"<<"provedProfit["<<i-j<<"]+revenueByNumItem["<<j<<"]\n";
            dp[i] = max(dp[i], dp[i-j]+price[j]);
        }
    }
    
    cout<<dp[n]<<'\n';

    
    
    return 0;
    
}