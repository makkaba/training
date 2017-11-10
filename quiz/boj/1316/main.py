def solution(word):
    hit = []
    
    for i in range(1, len(word)):
        if word[i-1] != word[i]:
            if word[i] in hit:
                #       i
                #ccc bb c
                return 0
            else:
                hit.append(word[i-1])
    return 1
    
def run():
    n = int(input())
    words = []
    answer = 0
    for i in range(n):
        words.append(input())
    
    for i in range(n):
        answer += solution(words[i])
    
    print(answer)

if __name__ == "__main__":
    run()