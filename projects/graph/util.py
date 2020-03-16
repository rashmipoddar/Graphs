
# Note: This Queue class is sub-optimal. Why?
# It is sub optimal because it uses an array instead of a LL.
# Dequeue means removing from index 0. So, all the other elements have to be moved. So it has a time complexity of O(n) 
# It does not really matter for a stack
# Also appending is usually O(1) because Python over allocates memory 
# but when we have to resize the array for memory the time complexity is O(n)

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

