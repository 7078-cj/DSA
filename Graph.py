
from collections import defaultdict, deque

#array of edges -> adjency matrix
def adjacency_matrix(A, n):
    M = []
    for i in range(n):
        M.append([0]*n)
    
    for u, v in A:# u is starting vertex then v is the connected vertex
        M[u][v] = 1
    
    return M

def adjacency_matrix_undirectional(A, n):
    M = []
    for i in range(n):
        M.append([0]*n)
    
    for u, v in A:
        M[v][u] = 1
    
    return M

def adjacency_list(A):
    D = defaultdict(list)
    
    for u, v in A:
        D[u].append(v)
        
    return D

def adjacency_list_undirected(A):
    D = defaultdict(list)
    
    for u, v in A:
        D[u].append(v)
        D[v].append(u)
        
    return D

def dfs_recursive(node, D, seen):
    print(node)
    for nei_node in D[node]:
        if nei_node not in seen:
            seen.add(nei_node)
            dfs_recursive(nei_node, D, seen)
        

def DFS_with_recursion(D):
    source = 0
    seen = set()
    seen.add(source)
    dfs_recursive(source, D, seen)
    
def DFS_stack(D):
    source = 0
    seen = set()
    seen.add(source)
    stack = [source]
    
    while stack:
        node=stack.pop()
        print(node)
        for nei_node in D[node]:
            if nei_node not in seen:
                seen.add(nei_node)
                stack.append(nei_node)
                
def BFS_queue(D):
    source = 0
    seen = set()
    seen.add(source)
    q = deque()
    q.append(source)
    
    while q:
        node=q.popleft()
        print(node)
        for nei_node in D[node]:
            if nei_node not in seen:
                seen.add(nei_node)
                q.append(nei_node)
                
class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []
        
    def __str__(self):
        return f'Node({self.value})'
    
    def display(self):
        connections = [node.value for node in self.neighbors]
        return f'{self.value} is connected to: {connections}'
    
    


if __name__ =="__main__":
    n=8
    A = [
        [0,1],[1,2],
        [0,3],[3,4],
        [3,6],[3,7],
        [4,2],[4,5],
        [5,2]
    ]
    
    print(adjacency_matrix(A, n))
    print(adjacency_list(A))
    print(adjacency_list_undirected(A))
    D = adjacency_list(A)
    DFS_with_recursion(D)
    print()
    DFS_stack(D)
    print()
    BFS_queue(D)
    
    A = Node('A')
    B = Node('B')
    C = Node('C')
    D = Node('D')
    
    A.neighbors.append(B)
    B.neighbors.append(A)
    
    C.neighbors.append(D)
    D.neighbors.append(C)
    
    print(A.display())

        