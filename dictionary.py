class Dictionary:

    '''
    Basic implementation of a associative structure / dictionary:

    put(key, value) -> adds the key-value pair or updates the value (returning old value)
    get(key) -> returns corresponding value for given key
    remove(key) -> removes the given key-value pair and returns it
    containsKey(key) -> returns true/false
    containsValue(value) -> returns true/false
    size() -> return number of key-value pairs

    '''
    def __init__(self) -> None:
        self.keys = []
        self.values = []
        self.count = 0

    def put(self, key, value):
        if not self.containsKey(key):
            self.keys.append(key)
            self.values.append(value)
            self.count += 1
            return None
        else:
            for index in range(self.count):
                if self.keys[index] == key:
                    toReturn = self.values[index]
                    self.values[index] = value
                    return toReturn
            
    
    def get(self, key):
        pos = -1

        for index in range(self.count):
            if self.keys[index] == key:
                pos = index
            
        if pos == -1:
            return None
        
        return self.values[pos]
    
    def remove(self, key):
        pos = -1

        for index in range(self.count):
            if self.keys[index] == key:
                pos = index
            
        if pos == -1:
            return None
        
        toReturn = self.values[pos]
        del self.keys[pos]
        del self.values[pos]
        self.count -= 1
        return toReturn
    
    def containsKey(self, key):
        for index in range(self.count):
            if self.keys[index] == key:
                return True
        
        return False

    def containsValue(self, value):
        for index in range(self.count):
            if self.values[index] == value:
                return True
        
        return False

    def size(self):
        return self.count
    
    def __str__(self) -> str:
        toReturn = ""
        for index in range(self.count):
            toReturn += (str(self.keys[index]) + " - " + str(self.values[index]) + "\n")

        return toReturn
    
if __name__ == "__main__":
    assoc = Dictionary()

    print(assoc.put("France", "Pari"))
    print(assoc.put("Germany", "Berlin"))
    print(assoc.put("Austria", "Vienna"))

    print(assoc)

    print(assoc.put("France", "Paris"))
    print(assoc.remove("England"))
    print(assoc.remove("Germany"))
    print(assoc)

    print(assoc.containsKey("England"))
    print(assoc.containsKey("France"))

    print(assoc.containsValue("London"))
    print(assoc.containsValue("Paris"))

    print(assoc.size())


