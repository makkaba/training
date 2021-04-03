#난이도 하
import sys



def addP(s, depth, n):
    # s="[()]"
    
    print("this", s)
    if depth >= n:
        return s
    depth +=1
    temp = []
    
    #각 원소에 넣어보기
    for i in range(len(s)):
        temp.append("()" + s[i])
        print("temp",temp)
    left = addP(temp, depth, n)
    temp = []
    for i in range(len(s)):
        temp.append("(" + s[i] + ")")
    middle = addP(temp, depth, n)
    temp = []
    for i in range(len(s)):
        temp.append(s[i] + "()")
    right = addP(temp, depth, n)
    return left + middle + right
    
    

def solution(N):
    answer = [ "" ]
    
    result = addP(["()"], 0, N-1)
    result = list(set(result))
    print(result)
    

    return answer    


def main():
    answer = solution(2)
    
    return answer

if __name__ == "__main__":
    main()
    
    