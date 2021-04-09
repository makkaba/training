
set는 중복이 되지 않는다 
변경도 되지 않는다 


### 차집합
```
dice = {1,2,3,4,5,6}
even = {2,4,6,8,10}

odd_dice = dice - even
print(odd_dice)
```

### 합집합

```
dice = {1,2,3,4,5,6}
even = {2,4,6,8,10}

sum_dice = dice | even
print(sum_dice)
```


### 교집합

```
dice = {1,2,3,4,5,6}
even = {2,4,6,8,10}

common = dice & even
print(common)
```


### 대상차집합 (교집합 빼고 나머지)

```
dice = {1,2,3,4,5,6}
even = {2,4,6,8,10}

outer = dice ^ even
print(outer)
```

### set의 포함 여부 

```
dice = {1,2,3,4,5,6}
even = {2,4,6,8,10}

if {1,2,12} <= dice:
    print("포함")
else:
    print("미포함")
```

