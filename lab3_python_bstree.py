import config
totalCmpInsert = 0
totalCmpFind = 0

class bstree:
    def __init__(self, value=None):
        self.verbose = config.verbose
        self.height = 0
        self.numOfCmpInsert = 0
        self.numOfCmpFind = 0

    def size(self):
        if (self.tree()):
            return 1 + self.leftTree.size() + self.rightTree.size()
        return 0
        
    def tree(self):
        # This counts as a tree if it has a field self.value
        # it should also have sub-trees self.left and self.right
        return hasattr(self, 'storedValue')
        
    def insert(self, value):
        global totalCmpInsert
        if not self.tree():
            self.leftTree = bstree()
            self.rightTree = bstree()
            self.storedValue = value
            return
        if value > self.storedValue:
            totalCmpInsert = totalCmpInsert + 1
            if self.rightTree != None:
                self.rightTree.insert(value)
            else:
                self.rightTree = bstree(value)
        elif value < self.storedValue:
            totalCmpInsert = totalCmpInsert + 1
            if self.leftTree != None:
                self.leftTree.insert(value)
            else:
                self.leftTree = bstree(value)
        else:
            return
     
    def find(self, value):
        global totalCmpFind
        if self.tree():
            if value == self.storedValue:
                return True
            elif value > self.storedValue:
                totalCmpFind = totalCmpFind + 1
                if self.rightTree != None:
                    return self.rightTree.find(value)
                else:
                    return False
            else:
                totalCmpFind = totalCmpFind + 1
                if self.leftTree != None:
                    return self.leftTree.find(value)
                else:
                    return False
        else:
            return False

 
    # You can update this if you want
    def print_set_recursive(self, depth):
        if (self.tree()):
            for i in range(depth):
                print(" ", end='')
            print("%s" % self.storedValue)
            self.leftTree.print_set_recursive(depth + 1)
            self.rightTree.print_set_recursive(depth + 1)
            
    # You can update this if you want
    def print_set(self):
        print("Tree:\n")
        self.print_set_recursive(0)
        
    def print_stats(self):
        # TODO update code to record and print statistic
        print("Size of the binary search tree: " + str(self.size()))
        print("Average number of comparisons per insert: " + str(round(totalCmpInsert/self.size())))
        print("Average number of comparisons per find: " + str(round(totalCmpFind/self.size())))



bt = bstree()
bt.insert("d")

bt.insert("a")

bt.insert("b")

bt.insert("y")

bt.insert("z")

bt.insert("p")

bt.insert("l")

bt.find("p")
print(totalCmpFind)
bt.find("z")
print(totalCmpFind)


print("\n\n")
print(totalCmpInsert)

print("\n\n")
