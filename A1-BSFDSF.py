#----------------------BFS----------------------
from collections import deque

def bfs(adj, s):
    
    q = deque()
    
    visited = [False] * len(adj)

    visited[s] = True
    q.append(s)

    while q: 
        curr = q.popleft()
        print(curr, end=" ") 
        
        for x in adj[curr]:
            if not visited[x]:
                visited[x] = True
                q.append(x)

def add_edge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)

if __name__ == "__main__":
  
    V = 6
    
    adj = [[] for _ in range(V)]

    add_edge(adj, 0, 1)
    add_edge(adj, 0, 2)
    add_edge(adj, 1, 3)
    add_edge(adj, 1, 5)
    add_edge(adj, 4, 1)
    add_edge(adj, 2, 4)

    print("BFS starting from 0: ")
    bfs(adj, 0)
    
#----------------------DFS----------------------
def dfs_rec(adj, visited, s):
    
    visited[s] = True

    print(s, end=" ")

    for i in adj[s]:
        if not visited[i]:
            dfs_rec(adj, visited, i)

def dfs(adj, s):
    visited = [False] * len(adj)
    
    dfs_rec(adj, visited, s)

def add_edge(adj, s, t):
    
    adj[s].append(t)
    
    adj[t].append(s)
    
if __name__ == "__main__":
    V = 6
    
    adj = [[] for _ in range(V)]
   
    edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5]]

    for u,v in edges:
        add_edge(adj, u, v)

    source = 0
    print("DFS from source:", source)
    dfs(adj, source)
