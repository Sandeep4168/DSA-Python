class Heap:
    def __init__(self,size):
        self.customList = (size + 1) * [None]
        self.heapSize = 0
        self.maxSize = size + 1
        
    def getHeapSize(self):
        return self.heapSize
    
    def print(self):
        if self.customList is None:
            return 
        else:
            for i in range(1,self.heapSize + 1):
                print(self.customList[i])
                
    def HeapifyTreeInsert(self,index,heapType):
        parentIndex = int(index / 2)
        if index <= 1:
            return 
        if heapType == "Min":
            if self.customList[index] < self.customList[parentIndex]:
                temp = self.customList[index]
                self.customList[index] = self.customList[parentIndex]
                self.customList[parentIndex] = temp
            self.HeapifyTreeInsert(parentIndex,heapType)
        elif heapType == "Max":
            if self.customList[index] > self.customList[parentIndex]:
                temp = self.customList[index]
                self.customList[index] = self.customList[parentIndex]
                self.customList[parentIndex] = temp
            self.HeapifyTreeInsert(parentIndex,heapType)
    
    def insertNode(self,nodeValue,heapType):
        if (self.heapSize + 1) == self.maxSize:
            return "The heap is full"
        
        self.customList[self.heapSize + 1] = nodeValue
        self.heapSize += 1
        self.HeapifyTreeInsert(self.heapSize,heapType)
        return "The value has been added successfully"



heap = Heap(4)
heap.insertNode(1,"Min")
heap.insertNode(1,"Min")
heap.print()