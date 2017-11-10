
# def mostFrequentChar(word):
#     counter = 0
#     maxValue = -1
#     maxChar = ''
#     w = word.lower()
#     w = list(w)
#     w.sort()
# 
# 
#     for i in range(1, len(w)):
#         if w[i-1] == w[i]:
#             counter += 1
#             if counter > maxValue:
#                 maxValue = counter
#                 maxChar = w[i]
#             elif counter == maxValue:
#                 print("same! at", i)
#         elif w[i-1] != w[i]:
#             counter = 0
# 
#     print(maxChar)
    
def mostFrequentChar(w):
    word = w.lower()
    word = list(word)
    sameMaxCounter = 0
    maxValue = 0
    maxIdx = 0
    arr = [0 for i in range(27)]
    
    
    for i in range(len(word)):
        
        arr[ord(word[i]) - 97] += 1
    
    # maxValue = max(arr)
    for i in range(len(arr)):    
        if arr[i] == maxValue:
            sameMaxCounter+=1
            maxIdx = i
    
    if sameMaxCounter > 1:
        return "?"
    else:
        return chr(maxIdx+97).upper()
            
def main():
    word = input()
    print(mostFrequentChar(word))
    
if __name__ == "__main__":
    main()