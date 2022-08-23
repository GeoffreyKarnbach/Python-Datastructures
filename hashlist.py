class Hashlist:

    '''
    Basic implementation of a hashlist:

    index(value) -> returns index that value would have in hashlist
    put(value) -> adds value to hashlist
    contains(value) -> returns True/False if value in hashlist
    remove(value) ->  removes value from hashlist and returns if something has been removed

    '''

    def __init__(self) -> None:
        self.content = [None]*32
        self.count = 0

    def index(self, value):

        hash_ = hash(str(value))
        index = hash_ & (len(self.content)-1)

        while self.content[index] != None and not self.content[index] == value:
            index = (index+1) & (len(self.content)-1)
        
        return index

    def put(self, value):

        index = self.index(value)

        if self.content[index] is None:

            self.content[index] = value
            self.count += 1

            if (self.count >= len(self.content)*3/4):

                # Rehash table
                tempValues = self.content[:]

                self.content = [None] * (len(self.content)*2)

                for loop in range(len(tempValues)):
                    if tempValues[loop] is not None:
                        new_index = self.index(tempValues[loop])
                        self.content[new_index] = tempValues[loop]


    def contains(self, value):
        index = self.index(value)

        if (self.content[index] is not None and self.content[index] == value):
            return True
        
        return False

    def remove(self, value):

        index = self.index(value)
        
        if self.content[index] == value:

            self.content[index] = None

            self.count -= 1

            # Rehash table
            tempValues = self.content[:]

            self.content = [None] * (len(self.content))

            for loop in range(len(tempValues)):
                if tempValues[loop] is not None:
                    new_index = self.index(tempValues[loop])
                    self.content[new_index] = tempValues[loop]
            
            return True
        
        return False

    def __str__(self) -> str:

        toReturn = "\nFilled " + str(self.count) + "/" + str(len(self.content))+"\n"
        for loop in range(len(self.content)):
            toReturn += ("Position "+str(loop+1)+" | Value: "+str(self.content[loop])+"\n")
        
        toReturn += "\n"

        return toReturn

if __name__ == "__main__":
    
    hl = Hashlist()

    hl.put("Python")
    hl.put("C++")
    hl.put("Java")

    toCheck = ["Python","C++","C#","Java"]

    for item in toCheck:
        print(f"Element {item} in hashlist: {hl.contains(item)}")
    
    print(hl.remove("Java"))

    print(hl)