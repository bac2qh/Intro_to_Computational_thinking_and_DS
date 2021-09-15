import random 

class Jewel: 
    def __init__(self, name, value, weight):
        self.name = name 
        self.value = value
        self.weight = weight 

    def getName(self):
        return self.name 

    def getValue(self):
        return self.value

    def getWeight(self):
        return self.weight 


def knapsack(toConsider, avail):
    # results is a tuple of the total value of a solution, and the items of that solution
    if toConsider == [] or avail == 0: 
        results = (0, ()) 
    elif toConsider[0].getWeight() > avail: 
        results = knapsack(toConsider[1:], avail)
    else: 
        nextItem = toConsider[0]
        # explore left branch 
        withVal, withToTake = knapsack(toConsider[1:], avail - nextItem.getWeight())
        withVal += nextItem.getValue()
        # explore right branch 
        withoutVal, withoutToTake = knapsack(toConsider[1:], avail)
        if withVal > withoutVal: 
            results = (withVal, withToTake + (nextItem,))
        else: 
            results = (withoutVal, withoutToTake)
    return results

names = list(range(8))
values = [random.randint(100, 500) for i in range(8)]
weights = [random.randint(10, 50) for i in range(8)]

jewels = [Jewel(names[i], values[i], weights[i]) for i in range(8)]

def test_knapsack(jewels, maxWeight, printItems=True):
    val, solution = knapsack(jewels, maxWeight)
    print("Total value of items taken = ", val)
    if printItems:
        for i in solution:
            print(i.name, i.value, i.weight)

test_knapsack(jewels, 200)


