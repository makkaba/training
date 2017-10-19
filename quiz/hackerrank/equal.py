# -*- coding: utf-8 -*- 
# Enter your code here. Read input from STDIN. Print output to STDOUT

def main():
    
    T = input()

    #모든 걸 다 해보는 경우의 수. 안될 것 같다.
    while(T--):
        n = input()
        choco = [for i in input().split(' ')]
    
    
    solution(n, choco)

def solution1():
    #dp로 모든 경우의 수 하려고 했는데 안될거같음.
    
    '''
    dp[i] = i번째 숫자를 기준으로 나머지 숫자들을 올렸을 때 최종적으로 같아지는데 걸리는 횟수
    dp[i] = min(go(+1), go(3), go(5))
    '''
    for i in range(len(choco)):
        for j in range(3):
            
        for k in range(len(choco)):
            if(k == i):
                continue
            
def solution2(n, choco):
    #매번 제외될 수를  어떤 걸 픽 하느냐가 중요.
    #한개를 골라서 빼주는것과 같다.
    
    count = 0
    diff = [0]
    # choco = [2 2 3 7]
    for i in range(1, len(choco)):
        diff.append(choco[0] - choco[i])
        # diff = [0 0 1 5]
    #이제 diff를 -1, -2, -5를 통해 모두 0인 배열로 만들면서 카운트를 하면 끝
    #아 근데 왠지 dp로 풀어야될 것같은데..
    
    
if __name__ == "__main__":
    main()
