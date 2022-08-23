class Dequeue:

    '''
    Basic implementation of a Double Ended Queue:

    addFirst(value) -> adds value to the beginning
    addLast(value) -> adds value to the end

    pollFirst() -> returns first value and deletes it
    pollLast() -> returns last value and deletes it

    peekFirst() -> returns first value
    peekLast() -> returns last value

    size() -> returns size of queue
    
    '''

    def __init__(self) -> None:
        self.content = []
        self.count = 0

    def addFirst(self, data):
        self.content.insert(0, data)
        self.count += 1
    
    def pollFirst(self):
        if self.count == 0:
            return None
        
        toReturn = self.content[0]
        del self.content[0]
        self.count-=1
        return toReturn
    
    def peekFirst(self):
        if self.count == 0:
            return None
        
        toReturn = self.content[0]
        return toReturn
    
    def addLast(self, data):
        self.content.append(data)
        self.count += 1
    
    def pollLast(self):
        if self.count == 0:
            return None
        
        toReturn = self.content[self.count-1]
        del self.content[self.count-1]
        self.count-=1
        return toReturn
    
    def peekLast(self):
        if self.count == 0:
            return None
        
        toReturn = self.content[self.count-1]
        return toReturn
    
    def size(self):
        return self.count
    
    def __str__(self) -> str:

        toReturn = "\n"

        for index in range(self.count):
            toReturn += str(self.content[index]) + "\n"

        toReturn += "\n"
        
        return toReturn


if __name__ == "__main__":
    dq = Dequeue()
    for loop in range(1,10):
        dq.addLast(loop)
    
    while dq.size() > 0:
        print(dq.pollFirst())
    
    print(dq.pollFirst())