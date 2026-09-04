#Date 08/28/2026

import math
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


# Date 09/04/2026
# Moving Average from Data Stream

from collections import deque
class MovingAverage:
    '''
    undestanding the problem which is for data stream and moving average with fixed window size n
    solution:
    - to save memory we can use deque and append to the right and pop from left so that we will not have     memory problem 
    '''

    def __init__(self, size: int):
        self.size = size
        self.queue = deque()
        
        #for tracking
        self.count = 0
        self.sum =0
        

    def next(self, val: int) -> float:
        self.queue.append(val)
        self.count += 1
        
        dequed_val = self.queue.popleft() if self.count> self.size else 0
            
        self.sum = self.sum - dequed_val + val
        
        return self.sum/min(self.size, self.count)
        
        
        
#test case
# [[3],[1],[10],[3],[5]]
obj = MovingAverage(3)
def test_ma_stream_data(input, target):
  
    flag =''
    for i in range(len(input)):
        if not math.isclose(obj.next(input[i]), target[i], rel_tol=1e-4):
            print(f'test faild  as {input[i]} is not same as {target[i]}')
            flag = "tast failed"
    
    return flag if flag else "All tests passed"


input = [1, 10, 3, 5]
target = [1.0, 5.5, 4.66667, 6.0]
print(f'\n Testing moving average on a data stream \n {test_ma_stream_data(input, target)}')
    




