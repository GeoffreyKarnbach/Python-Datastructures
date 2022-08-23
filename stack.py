class Stack:

    '''
    Basic implementation of a stack:

    push(value) -> adds value to the end
    pop() -> returns last value and deletes it
    peek() -> returns last value
    size() -> returns size of stack
    
    '''

    def __init__(self) -> None:
        self.content = []
        self.count = 0

    def push(self, data):
        self.content.append(data)
        self.count += 1
    
    def pop(self):
        if self.count == 0:
            return None
        
        toReturn = self.content[self.count-1]
        del self.content[self.count-1]
        self.count -= 1
        return toReturn
    
    def peek(self):
        if self.count == 0:
            return None
        
        return self.content[self.count-1]
    
    def size(self):
        return self.count
    
    def __str__(self) -> str:

        toReturn = "\n"

        for index in range(self.count):
            toReturn += (str(self.content[index]) + "\n")
        
        toReturn += "\n"
        
        return toReturn

if __name__ == "__main__":
    s = Stack()
    for loop in range(1,10):
        s.push(loop)
    
    print(s)

    while s.size() > 0:
        print(s.pop())
    
    print(s.pop())