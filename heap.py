class Heap:

    '''
    Basic implementation of a heap/priority queue:

    heapify(position) -> restores the heap condition for the index position and works up recursively
    heapifier() -> internal method to call all necessary "heapify() calls" to make sure that the heap condition is met again
    put(value) -> inserts value into the priority queue
    delete(positon) -> removes the element at position and restores heap condition with heapify
    get() -> returns item with highest priority (index 0) and deletes it
    
    '''
    def __init__(self) -> None:
        self.content = []
    
    def heapify(self, position):

        '''
        The method searches for the 3 local "nodes" the biggest one and if it isn't the root, it exchanges it with the root and keeps working up recursively

            Root
           /    \
        Left    Right

        '''
        root = position
        maxIndex = root
        left = position * 2 + 1
        right = position * 2 + 2

        if left < len(self.content) and self.content[maxIndex][0] < self.content[left][0]:
            # Checks if left node is within the priority queue and if it is bigger than the current max Value
            maxIndex = left
        
        if right < len(self.content) and self.content[maxIndex][0] < self.content[right][0]:
            # Checks if right node is within the priority queue and if it is bigger than the current max Value
            maxIndex = right
        
        # If heap condition still not met -> exchange "local" root with maxIndex keep heapifying recursively
        if maxIndex != root:
            tempVal = self.content[root]
            self.content[root] = self.content[maxIndex]
            self.content[maxIndex] = tempVal
            self.heapify(maxIndex)

    def heapifier(self):
        for loop in range((len(self.content)//2)-1, -1, -1):
            self.heapify(loop)

    def put(self, value, extra = "None"):
        
        self.content.append([value,extra])

        if len(self.content) == 1:
            # If single element, there is no need to heapify
            return
        
        self.heapifier()
        
    def delete(self, position):
        
        temp = self.content[position]
        self.content[position] = self.content[len(self.content)-1]
        self.content[len(self.content)-1] = temp

        del self.content[len(self.content)-1]

        self.heapifier()

    def get(self):

        if len(self.content) == 0:
            return None

        toReturn = self.content[0]
        self.delete(0)
        return toReturn
    
    def size(self):
        return len(self.content)

    def __str__(self) -> str:
        toReturn = "\n"

        for loop in range(len(self.content)):
            toReturn += ("Priority value "+str(self.content[loop][0]) + " | with information \""+str(self.content[loop][1]) +"\"\n")
        
        toReturn += "\n"
        return toReturn

if __name__ == "__main__":
    
    hp = Heap()

    hp.put(1)
    hp.put(6,"Prio 6")
    hp.put(10,"Prio 10")
    hp.put(5,"Prio 5")
    hp.put(8,"Prio 8")
    
    print(hp)

    while hp.size() > 0:
        print(hp.get())
    
    print(hp.get())
    