import numpy as np

class BIT :
    def __init__(self,array):
        # self.array = np.array([[0 for i in range(len(array))], [0 for j in range(len(array))]])
        self.array = np.array([0 for i in range(len(array))])
        self.BIT = np.array([0 for j in range(len(array) + 1)])
        # self.tree = np.array([[0 for x in range(len(array) + 1)], [0 for y in range(len(array) + 1)]])
        # self.array = [0 for i in range(len(array) for j in range(len(array)]

        for i in range(len(array)):
            self.UpdateValue(i,array[i])

    def UpdateValue(self, position, value):
        current , self.array[position] = self.array[position] ,value
        value -= current
        position += 1
        while (position <= len(self.array)):
            self.BIT[position] += value
            position = self.GetNext(position)

    def GetParent(self,child_element):
        # in the arugument of this function , we have to pass the name of the child in order to know the parent
        # it will return the parent
        return (child_element - (child_element & -child_element))

    def GetNext(self,position):
        return (position + (position & -position))

    def PrefixSum(self,position):
        position += 1
        total = 0
        while (position > 0):
            total += self.BIT[position]
            position = self.GetParent(position)

        return total

    def SumOfRange(self,start,end):
        res = self.PrefixSum(max(start,end) - self.PrefixSum(min(start,end) - 1))
        return res

    def PrintArray(self):
        print("THE ARRAY =====>>> \t\t\t\t",self.array)


    def PrintTree(self):
        print("THE BINARY INDEXED TREE ====>>>",self.BIT)
        print("\n")

def test():

    cls = BIT([10,2,4,-5,6,8,1])
    cls.PrintArray()
    cls.PrintTree()
    cls.UpdateValue(3,23)
    print("\n")
    print("AFTER UPDATING THE VALUE ")
    print("\n")
    cls.PrintArray()
    cls.PrintTree()
    print("THE PARENT IS : ",cls.GetParent(5))
    print("THE NEXT VALUE IS : ",cls.GetNext(2))
    print("THE SUM OF THE PREFIX IS : ",cls.PrefixSum(5))
    print("THE SUM OF THE GIVEN RANGE IS : ",cls.SumOfRange(1,5))

#test()


