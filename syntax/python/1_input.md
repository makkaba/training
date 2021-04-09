## 1.입력

(python의 버전이 3.0 이하인 경우, input = raw_input)

- 테스트케이스 갯수(T)가 정해진 경우

인풋

```
4
1 2 3 4
```

코드

```
T = input()
arr = [int(v) for v in input().split(' ')]
```

-----

인풋

;첫째 줄에 갯수 나머지 열에는 갯수만큼 반복되는 배열

```
5
4
3 5
1 3 8
2 5 3 4
3 6 6 8 2
```
코드 

```
arr = []
T = input()
for i in range(T):
    arr.append([int(v) for v in input().split(' ')])
```

----

인풋

```
0110100
0110101
1110101
0000111
0100000
0111110
0111000
```
코드 

```
n = int(input())
a = []
for i in range(n):
    b = input()
    b = [int(v) for v in b]
    a.append(b)
```
----

인풋

```
2 3 4

```
코드

```
a, b, c = map(int, input().split())
```
----


enumerate

```
for p in enumerate(input().split()):
    print(p)

for i, k enumerate(input().split()):
    print(i, k)
```
