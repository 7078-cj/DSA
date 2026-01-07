# stack
stk = []

stk.append(5)
stk.append(4)
stk.append(3)
print(stk)

x = stk.pop()
print(x)
print(stk)

# what in top
print(stk[-1])

# IsNotEmpty?
if stk:
    print(True)

# Queues

from collections import deque

q = deque()
print(q)

# enqueue - add
q.append(5)
q.append(6)
q.append(7)

print(q)

# Dequeue - remove pop left
q.popleft()
print(q)

# left side
print(q[0])

# right side
print(q[-1])

# output
# [5, 4, 3]
# 3
# [5, 4]
# 4
# True
# deque([])
# deque([5, 6, 7])
# deque([6, 7])
# 6
# 7
