#난이도 하
import sys

def solution(n, words):
    answer = []
    temp = [ words[0] ]
    for i in range(1, len(words)):
        print(words[i])
        last = len(temp)-1
        size = len(temp[last])
        if temp[last][size-1] != words[i][0]:
            print(temp[last][size-1], words[i][0])
            print(i)
            return [ (i%n) +1, (i//n) +1] 
        if words[i] in temp:
            
            return [(i%n) +1, (i//n) +1] 
        temp.append(words[i])
    
    return [0, 0]

def main():
    result = solution(2, ["hello", "one", "even", "never", "now", "world", "draw"])
    
    print(result)
if __name__ == "__main__":
    main()
    
    