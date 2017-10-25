#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;


int main(){
    int n;
    
    cin>>n;
    long long dp[91];
    
    
    /*
    D[i] = i 자리수 이친수의 갯수.
    D[i] = D[i-2] + D[i-1]
    왜냐하면,
    D[100]을 구할 때
    100자리수라면 그 형태가
    100010101000....(99개)...1 이거나 
    10001010010....(99개)...0 일 것이다.
    그런데 마지막에 1이 오는 형태에는 그 전에 무조건 0으로 fix되어야 하기 때문에
    고정되지 않은 조합 갯수는 D[n-2]개.
    마지막에 0이 오는 형태는 고정되는 값이 젤 뒤에 0밖에 없으므로 
    D[n-1]개 
    따라서, 
    D[n] = D[n-1] + D[n-2]
    이고, 
    이친수는 0으로 시작할 수 없다고 했기 때문에 
    기저조건인 D[1], D[2]에 조건에 해당하는 경우의 수를 넣어준다.
    */
    
    /*
    중요한 교훈: 
    다이나믹은 십중팔구 끝을 고정시켜라
    이전에 과정들이 어떻게든 됐다 생각하고. 
    끝을 고정시키고 생각해보면 하나 더 픽스시킬 수 있을 것이다. 
    그러면 수식이 생기기 시작한다.
    제약조건이 있다면 베이스컨디션으로 해결될 것이다.
    
    */
    
    
    // 예외
    // 1
    dp[1] = 1;
    // 10
    dp[2] = 1;
    for(int i=3; i<=n; i++){
        dp[i] = dp[i-2] + dp[i-1];
    }
    
    
    cout<<dp[n]<<'\n';
    return 0;
    
}