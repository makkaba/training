def solution(s1, s2):
    
    s1 = list(s1)
    s2 = list(s2)
    
    fq1 = [0 for i in range(26)]
    fq2 = [0 for i in range(26)]
    
    answer = 0
    #count frequency
    for i in range(len(s1)):
        fq1[ord(s1[i])-97] +=1
    for i in range(len(s2)):
        fq2[ord(s2[i])-97] +=1
    
    for i in range(26):
        if fq1[i] != fq2[i]:
            answer += abs(fq1[i]-fq2[i])
    
    return answer
    
def run():
    s1 = input()
    s2 = input()
    
    print(solution(s1, s2))

if __name__ == "__main__":
    run()