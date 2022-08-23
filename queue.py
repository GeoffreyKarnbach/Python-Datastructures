class Queue:

    '''
    Basic implementation of a queue:

    add(value) -> adds value to the end
    poll() -> returns first value and deletes it
    peek() -> returns first value
    size() -> returns size of queue

    '''

    def __init__(self) -> None:
        self.content = []
        self.count = 0

    def add(self, data):
        self.content.append(data)
        self.count += 1
    
    def poll(self):
        if self.count == 0:
            return None
        
        toReturn = self.content[0]
        del self.content[0]
        self.count -= 1
        return toReturn
    
    def peek(self):
        if self.count == 0:
            return None
        
        toReturn = self.content[0]
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
    q = Queue()
    for loop in range(1,10):
        q.add(loop)
    
    while q.size() > 0:
        print(q.poll())
    
    print(q.poll())