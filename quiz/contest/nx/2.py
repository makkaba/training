def solution(s, x):
    if len(s) < len(x):
        return -1
    
    firstIdx = -1
    
    for i in range(len(s)):
        matchNum = 0
        firstIdx = -1
        #첫글자 일치할 때 시작
        if s[i] == x[0]:
            firstIdx = i
            for j in range(len(x)):
                if x[j]=="*" or s[i+j] == x[j]:
                    matchNum += 1
            if matchNum == len(x):
                return firstIdx
        # while i <= len(s)-len(x)+1:
    
    return -1        
        
                
    

def main():
    result = solution("julianthasamanth", "aman")
    # result = solution(["aab"])
    print(result)

if __name__ == "__main__":
    main()
    