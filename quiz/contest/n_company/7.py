#난이도 중
import sys

def solution(a,b):
    answer = 0
    
    a = a.lower()
    b = b.lower()
    
    if len(a) != len(b):
        return False
    
    a = list(a)
    b = list(b)
    
    a.sort()
    b.sort()
    
    for i in range(len(a)):
        if a[i] != b[i]:
            return False
        
    return True

def main():
    result = solution("listen", "tilent")
    print(result)

if __name__ == "__main__":
    main()
    
    