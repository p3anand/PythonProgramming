#Basic Data Structure - List, Set, Tuple, Dict
#Advanced Collections - deque, defaultDict, Counter, OrderedDict, ChainMap, namedTUPLE

#Advanced version of list
#DEQUE - Double Ended Queue | follows FIFO (First-In-First-Out)
from collections import deque

#create deque without elements
d1 = deque()
print(d1)

#create deque with elements
d2 = deque([1,2,3])
print(d2)

#Using append - to add a list item to the deque
d2.append(4)
print(d2)

#Adding element from left -> beginning of list
d2.appendleft(9)
print(d2)

#Using extend - to add a list to the deque
d2.extend([5,6,7])
print(d2)

#Remove last list item from deque
print("----------------")
print(d2)
print(d2.pop())
print(d2)
print(d2.popleft())
print(d2)
print("----------------")

