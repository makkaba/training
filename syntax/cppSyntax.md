# C++

## 전략

1. 절차마다 아웃풋을 써서 관찰해라.
2. 인풋에 고정적인 것은 무엇인지 파악해서 인풋을 쉽게 받아라.  ex) dosomething 4 helloworld `cin>>a>>b>>c;`
3. 많이 쓰는 코드는 미리 적어놓자 ex)2진수 변환

## 입력
- 테스트케이스 갯수(T)가 정해진 경우


한줄 읽기

```
4
1 2 3 4
```

```
vector<int> a(n+1);
while(T--){
	cin>>a[i];
}
```

(cin을 쓰면 띄어쓰기가 무시된다)



붙어있는 매트릭스 읽기

```
0110100
0110101
1110101
0000111
0100000
0111110
0111000
```
```
for(int i=0; i<n; i++){
    for(int j=0; j<n; j++){
        scanf("%1d", &a[i][j]);
    }
}
```

- 갯수가 정해지지 않은 경우(드물지만..)
(진짜 이렇게 출제하지 마라ㅡㅡ)

ex)
`
2 9 10 11 24
`

```
string s;
getline(cin, s);

```
- 갯수가 정해지지 않은 경우

ex)



## 문자열

```
s1 = "Hello";
s2 = "World";
s3 = s1[0] + s2.substr(1);
Horld
```

- 문자열 각 자리를 바꿔서 다시 리턴

유니코드 상 +3을 해서 문자열을 바꿔라

```
int solution(string s){
	answer = 0;
	for(int i=0; i<s.size(); i++){
			
	}
	return answer;
}

```

## 그래프
- 4방향 탐색

```
vector<int> dy = {0,1,0,-1};
vector<int> dx = {1,0,-1,0};
   
for(int i=0; i<4; i++){
    yy = y+dy[i];
    xx = x+dx[i];
    cout<<yy<<","<<xx<<'\n';
}

```

- 탐색 조건 필터링

```
if(yy <0 | yy>n | xx<0 | xx>n | visited[yy][xx] == true){
	continue;
}
sum += findPath(yy,xx);
```
조건이 많을 때는 반대의 조건을 or로 연결해서 continue로 무시해버리는게 좋다.

## 벡터
- 단순 정렬

```
sort(a.begin(), a.end());
```

- 커스텀 sort

```

```

## 기타

- 전역변수를 쓰자.

전역변수를 쓰는것이 PS에서는 나쁜 것이 아니다.
어차피 환경을 통제하고 알고리즘을 보는 것이기 때문에.

이런 방법도 있긴 한데 (2차원 벡터 -1로 초기화)

```
vector<vector<int>> visited(size, vector<int> (size, -1));
```
visited는 갯수가 정해져있기 때문에 벡터로 할 필요가 없다. 글로벌 변수로 선언하자. 초기화는 함수 안에서 해줘야 한다.

```
bool visited[50][50];
```

- for문을 수동으로 써야할 때가 많으니 미리 복사해놓자.

```
for(int i=0; i<n; i++){
	for(int j=0; j<n; j++){
		
	}
}
```
