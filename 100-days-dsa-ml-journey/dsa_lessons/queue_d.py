import collections 

queue = collections.deque()

# If you want to initialize it with some initial values:
queue = collections.deque([1, 2, 3])

# Enqueueing/adding elements:
queue.append(4)
queue.append(5)

# Dequeuing/removing elements:
print(queue.popleft()) # 1
print(queue.popleft()) # 2

# Check element at front of queue (next element to be removed)
print(queue[0]) # 3

# Get size
print(len(queue)) # 3


# 
class recent_counter:
    def __init__(self):
        self.queue = deque()
    def ping(self, t):
        while self.queue and self.queue[0] < t - 3000:
            self.queue.popleft()
        self.queue.append(t)
        return len(self.queue)
        