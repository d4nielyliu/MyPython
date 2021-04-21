class Set:
      
    def __init__(self,elements):
        self.set = []
        for i in elements:
            self.set.append(i)

    def addElement(self,x):
        self.set.append(x)

    def member(self,x):
        if x in self.set:
           return True
        else:
           return False

    def deleteElement(self,x):
        if self.member(x):
           self.set.remove(x)
 
    def intersection(self, set2):
        intersection = []
        for i in set2:
            if i in (set2 and self.set):
               intersection.append(i)
        return intersection

    def union(self, set2):
        for x in self.intersection(set2):
            set2.remove(x)
        uni = self.set + set2
        return uni
            

    def subtraction(self, set2):
        for x in self.set:
            if x in set2:
               self.set.remove(x)
        return self.set

    def getSet(self):
        return self.set


            
def main():
    List = ['cat', 'dog', 'fish', 'mouse', 'banana']
    setA = Set(List)
    setA.addElement('small')
    setA.deleteElement('dog')
 
    print("The set A is",setA.getSet())
    
    setB = ['flat', 'cat', 'rectangle', 'banana', 'dog', 'mouse', 'lemon']
    print("The set B is", setB)
    setC = ['cat', 'dog', 'mouse', 'fish']
    intersect = setA.intersection(setB)
    print("The intersection between A and B is ", intersect)
    U = setA.union(setB)
    print("The union is ", U)
    Sub = setA.subtraction(setC)
    print("The substraction is ", Sub)




main()
        
