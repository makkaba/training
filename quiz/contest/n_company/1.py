#난이도 하
import sys
def addP(s, depth, n):
    if depth == n:
        return [""]
    depth +=1
    return ["()"+s, "("+s+")", s+"()" ]

def solution(N):
    answer = [ "" ]
    
    result = addP("()", 0, N)
    
    

    return result

def main():
    
    result = solution(3)
    print(result)
    

if __name__ == "__main__":
    main()