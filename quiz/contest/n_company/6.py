#난이도 중
import sys

def solution():
    answer = 0
    
    return answer

def main():
    n = input()
    
    print(n[0])
def solution(seat):
    answer = -1
    # print(seat[1][0])
    temp = []
    
    for i in range(len(seat)):
        temp.append( (seat[i][0], seat[i][1]) )
    total = len(temp)
    pure = list(set(temp))
    answer = len(pure)
    
    return answer

if __name__ == "__main__":
    main()
    
    