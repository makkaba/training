def solution(word):
    size = len(word)
    if size%2==0 :
        mid = size//2
    else:
        mid = (size//2) - 1
    for i in range(mid):
        if word[i] != word[size-i-1]:
            return 0
    return 1    
    
def run():
    word = input()
    print(solution(word))
if __name__ == "__main__":
    run()