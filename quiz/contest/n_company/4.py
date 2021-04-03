#난이도 중
import sys

def solution(l,v):
    answer = 0
    
    v.sort()
    print(v)
    maxDiff = 0
    
    if len(v) == 1:
        return max(v[0] - 0, l - v[0])
    
    for i in range(len(v)-1):
        diff = v[i+1] - v[i]
        maxDiff = max(maxDiff, diff)
    
    answer = maxDiff//2
    if maxDiff%2 != 0:
        answer +=1
    return answer

def main():
    result = solution(1,[15,5,3,7,9,14,0])
    print(result)

if __name__ == "__main__":
    main()
    
    