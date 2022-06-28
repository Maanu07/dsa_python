import collections 

dequeue = collections.deque([2,3,4])

print(dequeue)

#add element from right side
dequeue.append(5)
print(dequeue)

#add element from left side
dequeue.appendleft(1)
print(dequeue)

#removes from right
dequeue.pop()
print(dequeue)

#removes from left
dequeue.popleft()
print(dequeue)