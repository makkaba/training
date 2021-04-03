#난이도 중
import sys

def solution(paper):
    answer = 0
    
    paper.sort(reverse = True)
    
    print("sorted:",paper)
    for i in range(len(paper)):
        print(i+1,"개 인용")
        upperSum=0
        for j in range(i+1):
            upperSum += paper[j]
        
        print(pow(i+1,2),"<=", upperSum)
        
        if pow(i+1,2) <= upperSum:
            answer = i
    return answer+1

def main():
    result = solution([1, 0, 0, 3, 0, 1])
    print(result)

if __name__ == "__main__":
    main()
    
    