class MyQueue:
    def __init__(self):
        self.start = -1
        self.end = -1
        self.size = 10
        self.arr = [0] * self.size
        self.cursize = 0

    def enqueue(self, data):
        if self.cursize < self.size:
            if self.cursize == 0:
                self.start = 0
                self.end = 0
                self.arr[self.end] = data
            else:
                self.end = (self.end + 1) % self.size
                self.arr[self.end] = data
            self.cursize += 1
        else:
            print('Queue is full')

    def dequeue(self):
        if self.cursize == 0:
            print('Queue is empty')
        else:
            print(f'Removed element: {self.arr[self.start]}')
            if self.start == self.end:
                self.start = self.end = -1
            else:
                self.start = (self.start + 1) % self.size
            self.cursize -= 1

    def peek(self):
        if self.cursize > 0:
            print(self.arr[self.start])
        else:
            print('Queue is empty')

    def get_size(self):
        print(self.cursize)



