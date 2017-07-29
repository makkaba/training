def f(n):
    #base condition
    if n == 1:
        return 1
    
    #main logic
    return f(n-1)+f(n-2)

def main():
    n = input()
    result = f(n)
    print(result)
    
main()
    
    