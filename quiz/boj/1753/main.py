from sys import stdin
input = stdin.readline
import heapq
def Dijkstra(n, adj, source):
    dist = [float('inf')]*(n+1);
    print("dist:", dist)
    dist[source] = 0
    print("dist:", dist)
    H = [];
    print("init H:", H)
    heapq.heappush(H, (0, source))
    print("init val H:", H)
    while H:
        d, u = heapq.heappop(H)
        print("after pop H:", H)
        if dist[u] != d: continue
        for v, c in adj[u]:
            if dist[v] > d+c: dist[v] = d+c; heapq.heappush(H, (d+c, v))
    return dist
# 
# n, m = map(int,input().split())
# s = int(input())
# adj = [[] for i in range(n+1)]
# for i in range(m):
#     a, b, c = map(int,input().split())
#     adj[a].append((b,c))
# print(adj)

n = 5
m = 6
s = 1
adj = [[], [(2, 2), (3, 3)], [(3, 4), (4, 5)], [(4, 6)], [], [(1, 1)]]

cost = Dijkstra(n, adj, s)
for i in range(1,n+1):
    if cost[i] == float('inf'):
        print("INF")
    else:
        print(cost[i])