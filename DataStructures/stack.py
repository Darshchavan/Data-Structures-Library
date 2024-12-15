class Stack:
    def __init__(self):
        self.top = -1
        self.size = 1000
        self.arr = [0] * self.size

    def push(self, x):
        if self.top != self.size - 1:
            self.top += 1
            self.arr[self.top] = x
        else:
            print('Stack is full')

    def pop(self):
        if self.top == -1:
            print('Stack is empty')
        else:
            print(f'Popped element is {self.arr[self.top]}')
            self.top -= 1

    def peek(self):
        if self.top == -1:
            print('Stack is empty')
        else:
            print(self.arr[self.top])

    def get_size(self):
        print(self.top + 1)

# Example usage
# s = stack()
# s.push(2)
# s.push(4)
# s.push(5)
# s.pop()

# s.peek()
