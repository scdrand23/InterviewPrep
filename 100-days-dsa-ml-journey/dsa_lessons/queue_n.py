#Date 08/28/2026

'''
Queue:FIFO- services,printer queue
operations:
- enqueue: adding to the queue
- dequeue: deleting from the queue

Efficient way would be:
1. using doubly linked list as add and delete given a node is O(1)
2. in python a data structure call deque (prounced (deck)) which is part of collections library

- most common use of queue is to implement BFS
- other than BFS, there is no much problem use cases for queue

'''

# deque interface
from collections import deque

#inti with some intial values
_queue = deque([1,2,3])

print("")

#adding and removing (enque/deque)
_queue.append(4)
_queue.append(5)

print(_queue)
_queue.popleft() # remove 1

print(_queue)

_queue.popleft() # remove 2
print(_queue)

#expect 3
print(_queue[0])


#finish poping
while _queue:
    print(_queue.popleft())

if not _queue:
    print("Queue is empty!")



class RecentCounter:
    def __init__(self):
        self._queue = deque()

    def ping(self, t: int)-> int:
        while self._queue and self._queue[0] < t-3000:
            self._queue.popleft()

        self._queue.append(t)
        return len(self._queue)


#test case

rc = RecentCounter()

def test_rc(pings, expected):
    rc = None
    for t, exp in zip(pings, expected):
        if t == []:                 # constructor call
            rc = RecentCounter()
            result = None
        else:
            result = rc.ping(t)
        print(f"ping({t}) -> {result} (expected {exp})")
        assert result == exp, f"ping({t}) returned {result}, expected {exp}"
    print("All tests passed")


test_rc([[], 1, 100, 3001, 3002], [None, 1, 2, 3, 3])
