import os

def generateTest(filename):
    with open("./_test_"+filename+".py","w") as file:
        file.write("import unittest\n")
        file.write("from "+filename+" import*\n\n")
        file.write("class Test"+filename.capitalize()+"(unittest.TestCase):\n")
        file.write("\tdef test_default(self):\n")
        file.write("\t\tpass")

        file.write("\n\nif __name__ == \"__main__\":\n")
        file.write("\tunittest.main()")

    print(f"Test File created for {filename}.")


if __name__ == "__main__":
    choice = int(input("Do you would to generate a test for single file (0) or all files (1)? "))

    if choice == 0:
        filename = input("Enter filename to generate unittest: ")
        generateTest(filename) 
    
    elif choice == 1:
        with open("Documentation/all_structures.txt","r") as f:
            content = f.readlines()

        content = [elem.strip() for elem in content]
        for elem in content:
            generateTest(elem)
    
    else:
        print("Wrong option")
