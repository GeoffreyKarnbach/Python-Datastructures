class Treenode:

    '''
    Basic implementation of tree node:

    constructor() -> set values for node
    add(key, value) -> finds position for new Treenode and place it (recursive)
    get(key) -> returns value associated with key
    contains(key) -> returns True/False if key within children nodes
   
    '''

    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        self.left = None
        self.right = None
    
    def add(self, key, value):

        if key == self.key:
            toReturn = self.value
            self.value = value
            return toReturn
        
        if key > self.key:
            if self.right is not None:
                self.right.add(key, value)
            
            else:
                self.right = Treenode(key, value)
                return None
        
        if key < self.key:
            if self.left is not None:
                self.left.add(key, value)
            
            else:
                self.left = Treenode(key, value)
                return None
        

    def contains(self, key):
        isLeft = False
        isRight = False

        if self.left is not None:
            isLeft = self.left.contains(key)
        
        if self.right is not None:
            isRight = self.right.contains(key)
        
        return self.key == key or isLeft or isRight

    
    def __str__(self) -> str:

        if self.right is None and self.left is None:
            return (str(self.key) + " - " + str(self.value) + "\n")
        
        elif self.right is None:
            return str(self.left) + (str(self.key) + " - " + str(self.value) + "\n") 
        
        elif self.left is None:
            return (str(self.key) + " - " + str(self.value) + "\n") + str(self.right)
        
        else:
            return str(self.left) + (str(self.key) + " - " + str(self.value) + "\n") + str(self.right)
    
    def get(self, key):
        if key == self.key:
            return self.value

        elif key < self.key:
            if self.left is None:
                return None
            
            return self.left.get(key)
        
        elif key > self.key:
            if self.right is None:
                return None
            
            return self.right.get(key)
        
        return None

class BinarySearchTree:

    '''
    Basic implemenation of Binary Search Tree:
    | BST: Each Treenode has left and right child
    | Key of left child always smaller then parent
    | Key of right child always bigger then parent

    constructor() -> /
    put(key, value) -> adds key-value pair to BST
    get(key) -> returns the associated value with key or None
    contains(key) -> returns True/False if key is in BST <=> get(key) != None
    
    '''
    def __init__(self) -> None:
        self.root = None
    
    def put(self, key, value):
        
        if self.root is None:
            self.root = Treenode(key, value)
            return None

        return self.root.add(key, value)
        

    def get(self, key):
        
        if self.root is not None:
            return self.root.get(key)
        
        return None

    def contains(self, key):

        if self.root is None:
            return False
        
        return self.root.contains(key)

    def __str__(self) -> str:
        if self.root is None:
            return "EMPTY"
        
        return str(self.root)


if __name__ == "__main__":

    '''
    root = Treenode(5,5)
    root.add(2,2)
    root.add(7,7)
    root.add(1,1)
    root.add(3,3)

    print(root)

    '''

    bst = BinarySearchTree()
    bst.put(5,10)
    bst.put(2,4)
    bst.put(7,14)
    bst.put(1,2)
    bst.put(3,6)

    print(bst.get(6))
    print(bst.contains(10))

    print(bst)