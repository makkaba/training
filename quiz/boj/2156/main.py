'''
문제특징&힌트: 
-선택할때 건너뛸수도 있고 안뛸수도 있다. 
=> 경우의 수가 갈린다 => D[i] = (D[i-1]) + (D[i-2] + D[i-3]) 이런 형태가 나올 일이 많음
이 케이스에는 경우의 수를 OR 취급한 뒤 더해줘야(+) 한다.

- 나머지를 어떻게든 세운 뒤, 하나를 놓으면 된다 => 큰 나를 작은 나를 해결해서 푼다

'''

def solution(n, glasses):
    '''
    틀린 풀이)
    D[i] = 마지막에 i 원소를 선택하는 경우 마실 수 있는 누적 최대 포도주 량
    
    직전꺼 i-1를 마신 경우) 
    D[i-1] + D[i-3]
    
    직전꺼를 i-2 안 마신 경우
    D[i-2] 
    
    둘 중 큰게 짱
    D[i] = max(D[i-1]+D[i-3], D[i-2])
    ----------------
    맞는 풀이)
    
    D[i] = 마지막에 i 원소를 선택하는 경우 마실 수 있는 누적 최대 포도주 량
    D[i]를 결정하기 위해서는 직전의 경우의 수가 두가지가 있다고 처음엔 생각.
    glasses[i]는 무조건 선택한다는 전제에서,
    자유... XO
    자유.. XOO
    
    이렇게 두가지라고 생각했는데 잘못됨.
    전제 자체가 잘못됨.
    D[i] = i번째까지 결정했을 때 구해진 최대값 으로 바꿔야 한다.
    현재 원소, glasses[i]를 선택할지 말지도 선택지에 포함시켜야 한다
    따라서 다음과 같이 나타낼 수 있다.
      XO
     XOO
    XOOX
      XX
      
    문제를 정의하면서 얻게된 이 문제에만 해당하는 직관은 
    "왼쪽에 X가 나오기 전까지는 자유에 맡길 수 없구나"
    O가 나오는 순간(그 잔을 마신 순간) 이전 선택지에 영향을 미치기 때문.
    '''
    size = len(glasses)
    D = [0 for i in range(n)]
    D[0] = glasses[0]
    D[1] = glasses[1] + glasses[0]
    D[2] = max(glasses[0]+ glasses[1], glasses[1]+ glasses[2], glasses[0]+ glasses[2])
    
    for i in range(3, n):
        #무조건 i번째를 선택헀을 때 최대 누적값은?
        #케이스 중 최대값 => 작은 나 로 해결
        
        D[i] = max(glasses[i]+ glasses[i-1] + D[i-3], glasses[i] + D[i-2], D[i-2], D[i-1])
        
    # 갯수가 n개면 n-1번째가 마지막원소
    return D[n-1]

n = int(input())

glasses = []
for i in range(n):
    glasses.append(int(input()))
    
result = solution(n, glasses)
print("최대값:",result)
