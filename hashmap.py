from re import L


class Hashmap:

    '''
    Basic implementation of a hashmap:

    index(value) -> returns index that value would have in hashmap
    put(key, value) -> inserts or updates the value for the given key, and returns old value or None
    get(key) -> returns the value that is associated to the key or None
    containsKey(key) -> returns True/False if key is in the hashmap
    remove(key) -> removes the key/value pair from hashmap and returns True if key was removed (or False if not found)
    
    '''
    def __init__(self) -> None:
        self.keys = [None]*32
        self.values = [None]*32
        self.count = 0

    def index(self, value):
        '''
        Computes the position with hashing algorithm for given value (collision managment included)
        '''
        hash_ = hash(str(value))
        index = hash_ & (len(self.keys)-1)

        while self.keys[index] != None and not self.keys[index] == value:
            index = (index+1) & (len(self.keys)-1)
        
        return index

    def put(self, key, value):
        
        if key is None:
            return None
        
        index = self.index(key)

        toReturn = self.values[index]
        self.values[index] = value

        if self.keys[index] is None:

            self.keys[index] = key
            self.count += 1

            if (self.count >= len(self.keys)*3/4):

                # Rehash table
                tempKeys = self.keys[:]
                tempValues = self.values[:]

                self.keys = [None] * (len(self.keys)*2)
                self.values = [None] * (len(self.values)*2)

                for loop in range(len(tempKeys)):
                    if tempKeys[loop] is not None:
                        new_index = self.index(tempKeys[loop])
                        self.keys[new_index] = tempKeys[loop]
                        self.values[new_index] = tempValues[loop]

        return toReturn

    def get(self, key):
        
        index = self.index(key)

        if (self.keys[index] is not None and self.keys[index] == key):
            return self.values[index]
        
        return None
    
    def containsKey(self, key):
        return self.get(key) != None
    
    def remove(self, key):
        
        index = self.index(key)
        
        if self.keys[index] is not None:

            self.keys[index] = None
            self.values[index] = None

            self.count -= 1

            # Rehash table
            tempKeys = self.keys[:]
            tempValues = self.values[:]

            self.keys = [None] * (len(self.keys))
            self.values = [None] * (len(self.values))

            for loop in range(len(tempKeys)):
                if tempKeys[loop] is not None:
                    new_index = self.index(tempKeys[loop])
                    self.keys[new_index] = tempKeys[loop]
                    self.values[new_index] = tempValues[loop]
            
            return True
        
        return False

    def __str__(self) -> str:
        
        toReturn = "\nFilled " + str(self.count) + "/" + str(len(self.keys))+"\n"
        for loop in range(len(self.keys)):
            toReturn += ("Position "+str(loop+1)+": Key: "+str(self.keys[loop])+ "  |  Value: "+str(self.values[loop])+"\n")
        
        toReturn += "\n"

        return toReturn

if __name__ == "__main__":

    hm = Hashmap()

    for loop in range(16):
        hm.put(loop, loop*2)
    
    print(hm)

    for loop in range(16):
        print(str(loop) + " => " + str(hm.get(loop)))
    
    print()

    print(hm.containsKey(10)) #True 
    print(hm.containsKey(18)) #False

    hm.remove(10)

    print(hm)

    print(hm.containsKey(10)) #False