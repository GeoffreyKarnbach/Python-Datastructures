class ListNode:

    '''
    Basic implementation of a ListNode:

    constructor(value, next = None) -> Pass beginning values for given node

    '''
    def __init__(self, value, next = None) -> None:
        self.value = value
        self.next = next
    
    def __str__(self) -> str:
        return "Node: " + str(self.value)
    
    

class LinkedList:
    
    '''
    Basic implementation of a Linked List:

    constructor(head: ListNode) -> Constructor with option to pass first Node, has to be a ListNode!!

    add(value, i) -> adds the given value to a ListNode inserted at position i
    addFirst(value) -> adds the given value to a ListNode in first position
    addLast(value) -> adds the given value to a ListNode in last position

    get(i) -> returns value at index i
    getFirst() -> returns value of "head" node
    getLast() -> returns value of last node

    pollFirst() -> returns value of head node and removes it
    pollLast() -> returns value of last node and removes it

    indexOf(value) -> returns index of given value or -1 if not found
    size() -> returns amount of Nodes in LinkedList
    '''

    def __init__(self, head = None) -> None:
        self.head = head
    
    def add(self, value, index):

        if index == 0:
            self.addFirst(value)
        
        elif index >= self.size():
            raise IndexError("Linked List Index too high, max Value: " + str(self.size()))
        else:
            counter = 0
            current = self.head

            while counter < index-1:
                current = current.next
                counter += 1
            
            nextElem = current.next
            current.next = ListNode(value, nextElem)
            

    def addFirst(self, value):
        if self.head is None:
            toAdd = ListNode(value)
            self.head = toAdd
        
        else:
            oldHead = self.head
            self.head = ListNode(value, oldHead)
    
    def addLast(self, value):

        if self.head is None:
            self.addFirst(value)
        
        else:
            current = self.head

            while current.next is not None:
                current = current.next
            
            current.next = ListNode(value)
    
    def get(self, index):

        if index >= self.size():
            raise IndexError("Linked List Index too high, max Value: " + str(self.size()-1))

        counter = 0
        current = self.head

        while counter < index:
            current = current.next
            counter += 1
        
        return current.value

    def getFirst(self):

        if self.head is not None:
            return self.head.value

        return None

    def getLast(self):

        if self.head is not None:
            return self.get(self.size()-1)
        
        return None
    
    
    def pollFirst(self):

        if self.head is None:
            return None
        
        toReturn = self.head.value
        self.head = self.head.next
        return toReturn

    def pollLast(self):
        if self.head is None:
            return None
        
        if self.head.next is None:
            self.head = None
        
        current = self.head
        while current.next.next is not None:
            current = current.next
        
        toReturn = current.next.value
        current.next = None
        return toReturn

    def indexOf(self, value):
        counter = 0
        current = self.head

        while counter < self.size() and current.value != value:
            current = current.next
            counter += 1
        
        if counter < self.size():
            return counter
        
        return -1

    def size(self):
        current = self.head
        counter = 1

        while current.next is not None:
            current = current.next
            counter += 1
        
        return counter


    def __str__(self) -> str:

        if self.head is None:
            return "EMPTY"

        toReturn = ""
        current = self.head

        while current.next is not None:
            toReturn += (str(current) + "\n")
            current = current.next
        
        toReturn += (str(current) + "\n")

        return toReturn


if __name__ == "__main__":
    ll = LinkedList()

    ll.addLast(1)
    ll.addLast(2)
    ll.addLast(3)
    ll.addLast(4)

    print(ll) 