
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def __str__(self):
        return str(self.val)
    
def pre_order(node):
    if not node:
        return
    
    print(node)
    pre_order(node.left)
    pre_order(node.right)
    
def in_order(node):
    if not node:
        return
    
    
    in_order(node.left)
    print(node)
    in_order(node.right)
    
def pre_order_iterative(node):
    stk = [node]
    
    while stk:
        node = stk.pop()
        print(node)
        if node.right: stk.append(node.right)
        if node.left: stk.append(node.left)
        
#BFS
from collections import deque
def level_order(node):
    q = deque()
    q.append(node)
    
    while q:
        node = q.popleft()
        print(node)
        if node.left: q.append(node.left)
        if node.right: q.append(node.right)
        
def search(node, target):
    if not node:
        return False
    
    if node.val == target:
        return True
    
    return search(node.left, target) or search(node.right, target)

def search_bst(node, target):
    if not node:
        return False
    
    if node.val == target:
        return True
    
    if target < node.val: return search_bst(node.left, target)
    else: return search_bst(node.right, target)
    
if __name__ == "__main__":
    A = TreeNode(5)
    B = TreeNode(3)
    C = TreeNode(8)
    D = TreeNode(2)
    E = TreeNode(4)
    F = TreeNode(10)

    A.left = B
    A.right = C
    B.left = D
    B.right = E
    C.right = F

    # print(A)
    # pre_order(A)
    # in_order(A)
    # pre_order_iterative(A)
    level_order(A)
    print(search_bst(A, 11))