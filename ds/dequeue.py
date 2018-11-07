# Implementation of queue using Lists is too expensive
# instead use deque - double ended queue
# append and remove from from and back is O(1)

import collections

# creation
dq = collections.deque(['Tue','Wed','Fri'])
print(list(dq))

# append back
dq.append("Sun")
print(list(dq))

# append front
dq.appendleft("Mon")
print(list(dq))

# pop back
dq.pop()
print(list(dq))

# pop front
dq.popleft()
print(list(dq))


