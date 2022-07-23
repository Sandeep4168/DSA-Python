

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfString = False
        
class Trie:
    def __init__(self):
        self.rootNode = TrieNode()

    def insertString(self,word):
        current = self.rootNode
        for i in word:
            ch = i
            node = current.children.get(ch)
            if node == None:
                node = TrieNode()
                current.children.update({ch:node})

            current = node
        current.endOfString = True
        return "The value has been added successfully"
    def searchString(self, word):
        current = self.rootNode
        for i in word:
            node = current.children.get(i)
            if node == None:
                return False
            current = node
        
        if current.endOfString == True:
            return True
        else:
            return False
        
def deleteString(rootnode,word,index):
    ch = word[index]
    currentNode = rootnode.children.get(ch)
    canThisNodeBeDeleted = False
    
    if len(currentNode.children) > 1:
        deleteString(currentNode,word,index + 1)
        return False
    
    if index == len(word) - 1 :
        if len(currentNode.children) >= 1:
            currentNode.endOfString = False
            return False
        else:
            rootnode.children.pop()
            return True
    if currentNode.endOfString == True:
        deleteString(currentNode,word,index + 1)
        return False
    canThisNodeBeDeleted = deleteString(currentNode,word,index + 1)
    
    if canThisNodeBeDeleted == True:
        rootnode.children.pop()
        return True
    else:
        return False
              
        
trie = Trie()

print(trie.insertString("APPLE"))
print(trie.insertString("APPLE BEE"))
print(deleteString(trie,"APPLE",0))