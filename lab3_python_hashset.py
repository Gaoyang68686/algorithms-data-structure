from enum import Enum
import config

class Node:
    def __init__(self, value):
        self.storedValue = value
        self.nextNode = None
    def getNodeValue(self):
        return self.storedValue

class LinkedList:
    def __init__(self):
        self.head = None
    def addNode(self,value):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
        else:
            currentNode = self.head
            while currentNode.nextNode != None:
                currentNode = currentNode.nextNode
            currentNode.nextNode = newNode 
    def getAllValueList(self):
        myList = []
        if self.head == None:
            return myList
        else:
            currentNode = self.head
            while currentNode != None:
                myList.append(currentNode.getNodeValue())
                currentNode = currentNode.nextNode
            return myList
    def getLength(self):
        if self.head == None:
            return 0
        else:
            currentLength = 0
            currentNode = self.head
            while currentNode != None:
                currentLength = currentLength + 1
                currentNode = currentNode.nextNode
            return currentLength

def isPrimee(n):
    i = 2
    while (i * i <= n):
        if (n % i == 0):
            return False
        i = i + 1
    return True


class hashset:
    def __init__(self):
        # TODO: create initial hash table
        self.verbose = config.verbose
        self.mode = config.mode
        self.hash_table_size = config.init_size

        
        self.hashSet = [[i,None] for i in range(self.hash_table_size)]
        self.totalCollision = 0
        self.totalFailure = 0
        self.numOfItem = 0
        self.numOfReHashSize = 0
        self.numOfReHashLf = 0
        self.numOfReHashFail = 0
        self.loadFactor = 0        
    # Helper functions for finding prime numbers
    def isPrime(self, n):
        i = 2
        while (i * i <= n):
            if (n % i == 0):
                return False
            i = i + 1
        return True
        
    def nextPrime(self, n):
        while (not self.isPrime(n)):
            n = n + 1
        return n


    def reHash(self):                   # rehash function to solve full-HashSet and large-LoadFactor for Linear Probing, Quadratic Probing and Double Hashing
        self.numOfItem = 0
        self.hash_table_size = self.hash_table_size * 2
        tempHashSet = self.hashSet
        self.hashSet = [[None,None] for i in range(self.hash_table_size)]
        for i in range(self.hash_table_size):
            self.hashSet[i][0] = i
        for previousItem in tempHashSet:
            if previousItem[1] != None:
                self.insert(previousItem[1])


    def reHashFailure(self, value):       # rehash function for Quadratic Probing and Double Hashing when no slots for the insertion value
        self.numOfItem = 0
        self.hash_table_size = self.hash_table_size * 2
        tempHashSet = self.hashSet
        self.hashSet = [[None,None] for i in range(self.hash_table_size)]
        for i in range(self.hash_table_size):
            self.hashSet[i][0] = i
        for previousItem in tempHashSet:
            if previousItem[1] != None:
                self.insert(previousItem[1])
        self.insert(value)


    def reHashChain(self, value):         # rehash function to solve large-LoadFactor for Separate Chaining 
        self.numOfItem = 0
        self.hash_table_size = self.hash_table_size * 2
        tempHashSet = self.hashSet
        self.hashSet = [[None,None] for i in range(self.hash_table_size)]
        for i in range(self.hash_table_size):
            self.hashSet[i][0] = i
        for previousItem in tempHashSet:
            if previousItem[1] != None:
                for it in previousItem[1].getAllValueList():
                    self.insert(it)


        
    def insert(self, value):
        # TODO code for inserting into  hash table

        # LINEAR 1 start
        if self.mode == 0:
            self.loadFactor = self.numOfItem / self.hash_table_size
            if self.numOfItem == self.hash_table_size:
                print("Hash Set is full! Rehash by doubling the size to solve the problem............")
                self.numOfReHashSize = self.numOfReHashSize + 1
                self.reHash()
                self.loadFactor = self.numOfItem / self.hash_table_size
            while self.loadFactor > 0.75:
                print("Load Factor is too large! Rehash by doubling the size to solve the problem............")
                self.numOfReHashLf = self.numOfReHashLf + 1
                self.reHash()
                self.loadFactor = self.numOfItem / self.hash_table_size

            for item in self.hashSet:
                if item[1] == value:
                    print("value already in Hash Set!!!")
                    return


        #ASCII value of the value to be inserted
            ascValue = 0
            for i in range(len(value)):
                ascValue = ascValue + ord(value[i])
        #ASCII value of the value to be inserted
            index = ascValue % self.hash_table_size
            

            numOfCollision = 0            
            for i in range(index, self.hash_table_size):   # search a suitable position from the next position to the end of the hash set
                if self.hashSet[i][1] != None:
                    numOfCollision = numOfCollision + 1
                else:
                    self.hashSet[i][1] = value
                    self.numOfItem = self.numOfItem + 1
                    print("value '" + value + "' has been inserted successfully." + "\tNumber Of Collisions: " + str(numOfCollision))
                    self.totalCollision = self.totalCollision + numOfCollision
                    return
            

            for i in range(0, index):       # search a suitable position from the start of the hash set to the previous location of the location calculated at first
                if self.hashSet[i][1] != None:
                    numOfCollision = numOfCollision + 1
                else:
                    self.hashSet[i][1] = value
                    self.numOfItem = self.numOfItem + 1
                    print("value '" + value + "' has been inserted successfully." + "\tNumber Of Collisions: " + str(numOfCollision))
                    self.totalCollision = self.totalCollision + numOfCollision
                    return
            return
        # Linear 1 end





        # Linear 2 start
        elif self.mode == 4:
            self.loadFactor = self.numOfItem / self.hash_table_size
            if self.numOfItem == self.hash_table_size:
                print("\nHash Set is full! Rehash by doubling the size to solve the problem............\n")
                self.numOfReHashSize = self.numOfReHashSize + 1
                self.reHash()
                self.loadFactor = self.numOfItem / self.hash_table_size
            while self.loadFactor > 0.75:
                print("\nLoad Factor is too large! Rehash by doubling the size to solve the problem............\n")
                self.numOfReHashLf = self.numOfReHashLf + 1
                self.reHash()
                self.loadFactor = self.numOfItem / self.hash_table_size

            for item in self.hashSet:
                if item[1] == value:
                    print("value already in Hash Set!!!")
                    return


        #ASCII value of the value to be inserted
            ascValue = 0
            for i in range(len(value)):
                ascValue = ascValue + ord(value[i]) * (len(value)-i)
        #ASCII value of the value to be inserted
            divisor = self.hash_table_size
            for divisor in range(self.hash_table_size, 1, -1):
                if isPrimee(divisor):
                    break
            #get the maximum prime number which is less than the hash table size
            index = ascValue % divisor
            

            numOfCollision = 0            
            for i in range(index, self.hash_table_size):   # search a suitable position from the next position to the end of the hash set
                if self.hashSet[i][1] != None:
                    numOfCollision = numOfCollision + 1
                else:
                    self.hashSet[i][1] = value
                    self.numOfItem = self.numOfItem + 1
                    print("value '" + value + "' has been inserted successfully." + "\tNumber Of Collisions: " + str(numOfCollision))
                    self.totalCollision = self.totalCollision + numOfCollision
                    return
            

            for i in range(0, index):       # search a suitable position from the start of the hash set to the previous location of the location calculated at first
                if self.hashSet[i][1] != None:
                    numOfCollision = numOfCollision + 1
                else:
                    self.hashSet[i][1] = value
                    self.numOfItem = self.numOfItem + 1
                    print("value '" + value + "' has been inserted successfully." + "\tNumber Of Collisions: " + str(numOfCollision))
                    self.totalCollision = self.totalCollision + numOfCollision
                    return
            return
        # Linear 2 end



        

        # QUADRATIC 1 start
        elif self.mode == 1:
            self.loadFactor = self.numOfItem / self.hash_table_size
            if self.numOfItem == self.hash_table_size:
                print("\nHash Table is full! Rehash by doubling the size............\n")
                self.numOfReHashSize = self.numOfReHashSize + 1
                self.reHash()
                self.loadFactor = self.numOfItem / self.hash_table_size
            while self.loadFactor > 0.75:
                print("\nLoad Factor is too large! Rehash by doubling the size............\n")
                self.numOfReHashLf = self.numOfReHashLf + 1
                self.reHash()
                self.loadFactor = self.numOfItem / self.hash_table_size
                
            for item in self.hashSet:
                if item[1] == value:
                    print("value already in the hash table!!!")
                    return

            #ASCII value of the value to be inserted
            ascValue = 0
            for i in range(len(value)):
                ascValue = ascValue + ord(value[i]) 
            #get the insertion position
            index = ascValue % self.hash_table_size
            
            numOfCollision = 0
            for i in range(0, self.hash_table_size):
                newIndex = (index + (i*i)) % self.hash_table_size
                if self.hashSet[newIndex][1] != None:
                    numOfCollision = numOfCollision + 1
                else:
                    self.hashSet[newIndex][1] = value
                    self.numOfItem = self.numOfItem + 1
                    print("value '" + value + "' has been inserted successfully." + "\tNumber Of Collisions: " + str(numOfCollision))
                    self.totalCollision = self.totalCollision + numOfCollision
                    return
            
            self.totalFailure = self.totalFailure + 1
            print("\nFailed to insert this value due to the disadvantage of Quadratic Probing!!! Rehash by doubling the size............\n")
            self.numOfReHashFail = self.numOfReHashFail + 1
            self.reHashFailure(value)
            return 
        # QUADRATIC 1 end





        # QUADRATIC 2 start
        elif self.mode == 5:
            self.loadFactor = self.numOfItem / self.hash_table_size
            if self.numOfItem == self.hash_table_size:
                print("\nHash Table is full! Rehash by doubling the size............\n")
                self.numOfReHashSize = self.numOfReHashSize + 1
                self.reHash()
                self.loadFactor = self.numOfItem / self.hash_table_size
            while self.loadFactor > 0.75:
                print("\nLoad Factor is too large! Rehash by doubling the size............\n")
                self.numOfReHashLf = self.numOfReHashLf + 1
                self.reHash()
                self.loadFactor = self.numOfItem / self.hash_table_size
                
            for item in self.hashSet:
                if item[1] == value:
                    print("value already in the hash table!!!")
                    return

        #ASCII value of the value to be inserted
            ascValue = 0
            for i in range(len(value)):
                ascValue = ascValue + ord(value[i]) * i
        #ASCII value of the value to be inserted
            divisor = self.hash_table_size
            for divisor in range(self.hash_table_size, 1, -1):
                if isPrimee(divisor):
                    break
            #get the maximum prime number which is less than the hash table size
            index = ascValue % divisor

            
            numOfCollision = 0
            for i in range(0, self.hash_table_size):
                newIndex = (index + (i*i)) % self.hash_table_size
                if self.hashSet[newIndex][1] != None:
                    numOfCollision = numOfCollision + 1
                else:
                    self.hashSet[newIndex][1] = value
                    self.numOfItem = self.numOfItem + 1
                    print("value '" + value + "' has been inserted successfully." + "\tNumber Of Collisions: " + str(numOfCollision))
                    self.totalCollision = self.totalCollision + numOfCollision
                    return
            
            self.totalFailure = self.totalFailure + 1
            print("\nFailed to insert this value due to the disadvantage of Quadratic Probing!!! Rehash by doubling the size............\n")
            self.numOfReHashFail = self.numOfReHashFail + 1
            self.reHashFailure(value)
            return
        # QUADRATIC 2 end





        # SEPARATE CHAINING 1 start
        elif self.mode == 3:
            self.loadFactor = self.numOfItem / self.hash_table_size
            while self.loadFactor > 0.75:
                print("\nLoad Factor is too large! Rehash by doubling the size............\n")
                self.numOfReHashLf = self.numOfReHashLf + 1
                self.reHashChain()
                self.loadFactor = self.numOfItem / self.hash_table_size

            for item in self.hashSet:
                if item[1] == None:
                    item[1] = LinkedList()
            
            for item in self.hashSet:
                if item[1] != None:
                    if value in item[1].getAllValueList():
                        print("value already in Hash Set!!!")
                        return
            
            #ASCII value of the value to be inserted
            ascValue = 0
            for i in range(len(value)):
                ascValue = ascValue + ord(value[i]) 
            #ASCII value of the value to be inserted
            index = ascValue % self.hash_table_size
                
            for item in self.hashSet:
                if item[0] == index:
                    item[1].addNode(value)
                    numOfCollision = item[1].getLength() - 1
                    self.totalCollision = self.totalCollision + numOfCollision
                    #print("value has been inserted successfully.\tNumber of Collisions" + str(numOfCollision))
                    return
        # SEPARATE CHAINING 1 end





        # SEPARATE CHAINING 2 start
        elif self.mode == 7:
            self.loadFactor = self.numOfItem / self.hash_table_size
            while self.loadFactor > 0.75:
                print("\nLoad Factor is too large! Rehash by doubling the size............\n")
                self.numOfReHashLf = self.numOfReHashLf + 1
                self.reHashChain()
                self.loadFactor = self.numOfItem / self.hash_table_size

            for item in self.hashSet:
                if item[1] == None:
                    item[1] = LinkedList()
            
            for item in self.hashSet:
                if item[1] != None:
                    if value in item[1].getAllValueList():
                        print("value already in Hash Set!!!")
                        return
            
            #ASCII value of the value to be inserted
            ascValue = 0
            for i in range(len(value)):
                ascValue = ascValue + ord(value[i]) 
            #ASCII value of the value to be inserted
            index = ascValue % self.hash_table_size
                
            for item in self.hashSet:
                if item[0] == index:
                    item[1].addNode(value)
                    numOfCollision = item[1].getLength() - 1
                    self.totalCollision = self.totalCollision + numOfCollision
                    print("value has been inserted successfully.\tNumber of Collisions" + str(numOfCollision))
                    return
        # SEPARATE CHAINING 2 end





        # DOUBLE 1 start
        elif self.mode == 2:
            self.loadFactor = self.numOfItem / self.hash_table_size
            if self.numOfItem == self.hash_table_size:
                print("\nHash Table is full! Rehash by doubling the size............\n")
                self.numOfReHashSize = self.numOfReHashSize + 1
                self.reHash()
                self.loadFactor = self.numOfItem / self.hash_table_size
            while self.loadFactor > 0.75:
                print("\nLoad Factor is too large! Rehash by doubling the size............\n")
                self.numOfReHashLf = self.numOfReHashLf + 1
                self.reHash()
                self.loadFactor = self.numOfItem / self.hash_table_size
                
            for item in self.hashSet:
                if item[1] == value:
                    print("value already in the hash table!!!")
                    return

            #ASCII value of the value to be inserted
            ascValue = 0
            for i in range(len(value)):
                ascValue = ascValue + ord(value[i]) 
            #get the insertion position
            index1 = ascValue % self.hash_table_size
            index2 = ascValue % (self.hash_table_size-1)

            numOfCollision = 0
            for i in range(0, self.hash_table_size):
                newIndex = (index1 + (i*index2)) % self.hash_table_size
                if self.hashSet[newIndex][1] != None:
                    numOfCollision = numOfCollision + 1
                else:
                    self.hashSet[newIndex][1] = value
                    self.numOfItem = self.numOfItem + 1
                    print("value '" + value + "' has been inserted successfully." + "\tNumber Of Collisions: " + str(numOfCollision))
                    self.totalCollision = self.totalCollision + numOfCollision
                    return
            
            self.totalFailure = self.totalFailure + 1
            print("\nFailed to insert this value due to the disadvantage of Double Hashing!!! Rehash by doubling the size............\n")
            self.numOfReHashFail = self.numOfReHashFail + 1
            self.reHashFailure(value)
            return
        # DOUBLE 1 end





        # DOUBLE 2 start
        elif self.mode == 6:
            self.loadFactor = self.numOfItem / self.hash_table_size
            if self.numOfItem == self.hash_table_size:
                print("\nHash Table is full! Rehash by doubling the size............\n")
                self.numOfReHashSize = self.numOfReHashSize + 1
                self.reHash()
                self.loadFactor = self.numOfItem / self.hash_table_size
            while self.loadFactor > 0.75:
                print("\nLoad Factor is too large! Rehash by doubling the size............\n")
                self.numOfReHashLf = self.numOfReHashLf + 1
                self.reHash()
                self.loadFactor = self.numOfItem / self.hash_table_size
                
            for item in self.hashSet:
                if item[1] == value:
                    print("value already in the hash table!!!")
                    return

            #ASCII value of the value to be inserted
            ascValue = 0
            for i in range(len(value)):
                ascValue = ascValue + ord(value[i]) 
            #get the insertion position
            divisor1 = self.hash_table_size
            for divisor1 in range(self.hash_table_size,1,-1):
                if isPrimee(divisor1):
                    break
            divisor2 = divisor1 - 1
            for divisor2 in range(divisor1-1,1,-1):
                if isPrimee(divisor2):
                    break
            index1 = ascValue % divisor1
            index2 = ascValue % divisor2

            numOfCollision = 0
            for i in range(0, self.hash_table_size):
                newIndex = (index1 + (i*index2)) % self.hash_table_size
                if self.hashSet[newIndex][1] != None:
                    numOfCollision = numOfCollision + 1
                else:
                    self.hashSet[newIndex][1] = value
                    self.numOfItem = self.numOfItem + 1
                    print("value '" + value + "' has been inserted successfully." + "\tNumber Of Collisions: " + str(numOfCollision))
                    self.totalCollision = self.totalCollision + numOfCollision
                    return
            
            self.totalFailure = self.totalFailure + 1
            print("\nFailed to insert this value due to the disadvantage of Double Hashing!!! Rehash by doubling the size............\n")
            self.numOfReHashFail = self.numOfReHashFail + 1
            self.reHashFailure(value)
            return
        # DOUBLE 2 end        


    def find(self, value):
        # TODO code for looking up in hash table
        if (self.mode==3) or (self.mode==7):
            for item in self.hashSet:
                if (len(item[1].getAllValueList())>0) and (value == (item[1].getAllValueList())[0]):
                    return True             #print(item[0])
            return False                    #print(value + " cannot be found")
        else:
            for item in self.hashSet:
                if item[1] == value:
                    return True             #print(item[0])
            return False                    #print(value + " cannot be found")
        

    def print_set(self):
        # TODO code for printing hash table
        if (self.mode == 3) or (self.mode == 7):
            outputList = [[None,None] for i in range(self.hash_table_size)]
            for i in range(self.hash_table_size):
                outputList[i][0] = self.hashSet[i][0]
                outputList[i][1] = (self.hashSet[i][1]).getAllValueList()
            print(outputList)           

        else:
            print(self.hashSet)

        
    def print_stats(self):
        # TODO code for printing statistics
        print("Total Collisions: " + str(self.totalCollision))
        print("Total Failures(solved by rehashing): " + str(self.totalFailure))
        print("Average Collision per Insert: " + str(round(self.totalCollision/self.numOfItem*100, 3)))
        print("Average Failure per Insert: " + str(round(self.totalFailure/self.numOfItem*100, 3)))
        print("Number of Rehash used in total: " + str(self.numOfReHashLf + self.numOfReHashSize + self.numOfReHashFail))
        print("Number of Rehash used due to limited size of hash set: " + str(self.numOfReHashSize)) 
        print("Number of Rehash used due to failing to insert: " + str(self.numOfReHashFail)) 
        print("Number of Rehash used due to high load factor(Rehash when the load factor is larger than 0.75): " + str(self.numOfReHashLf)) 



    def reHash(self):                   # rehash function to solve full-HashSet and large-LoadFactor for Linear Probing, Quadratic Probing and Double Hashing
        self.numOfItem = 0
        self.hash_table_size = self.hash_table_size * 2
        tempHashSet = self.hashSet
        self.hashSet = [[None,None] for i in range(self.hash_table_size)]
        for i in range(self.hash_table_size):
            self.hashSet[i][0] = i
        for previousItem in tempHashSet:
            if previousItem[1] != None:
                self.insert(previousItem[1])


    def reHashFailure(self, value):       # rehash function for Quadratic Probing and Double Hashing when no slots for the insertion value
        self.numOfItem = 0
        self.hash_table_size = self.hash_table_size * 2
        tempHashSet = self.hashSet
        self.hashSet = [[None,None] for i in range(self.hash_table_size)]
        for i in range(self.hash_table_size):
            self.hashSet[i][0] = i
        for previousItem in tempHashSet:
            if previousItem[1] != None:
                self.insert(previousItem[1])
        self.insert(value)


    def reHashChain(self, value):         # rehash function to solve large-LoadFactor for Separate Chaining 
        self.numOfItem = 0
        self.hash_table_size = self.hash_table_size * 2
        tempHashSet = self.hashSet
        self.hashSet = [[None,None] for i in range(self.hash_table_size)]
        for i in range(self.hash_table_size):
            self.hashSet[i][0] = i
        for previousItem in tempHashSet:
            if previousItem[1] != None:
                for it in previousItem[1].getAllValueList():
                    self.insert(it)

# This is a cell structure assuming Open Addressing
# It should contain and element that is the key and a state which is empty, in_use or deleted
# You will need alternative data-structures for separate chaining
class cell:
    def __init__(self):
        pass
        
class state(Enum):
    empty = 0
    in_use = 1
    deleted = 2
        
# Hashing Modes
class HashingModes(Enum):
    HASH_1_LINEAR_PROBING=0
    HASH_1_QUADRATIC_PROBING=1
    HASH_1_DOUBLE_HASHING=2
    HASH_1_SEPARATE_CHAINING=3
    HASH_2_LINEAR_PROBING=4
    HASH_2_QUADRATIC_PROBING=5
    HASH_2_DOUBLE_HASHING=6
    HASH_2_SEPARATE_CHAINING=7
