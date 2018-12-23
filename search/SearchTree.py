
# data structure based on BST, except with upto 30 child nodes yielding a 3.36x reduction in average node depth, when measured with 533 nodes.
class SearchTree:
    def __init__(self):
        self.root = Node('a')
        self.depth = 0
        
    def letToInt(self, letter):
        letters = 'a b c d e é f g h i j k l m n o p q r s t u ú v w x y z .'.split(' ')
        letters.append(' ')
        return letters.index(letter)
    
    def push(self, name):
        node = Node(name)
#        first check if the node can be put directly under root
        self.pushCore(node, self.root, 0)
        return self.depth
    
#   the root node is updated at every recursion 
#   and the level represents the index of the letter being compared
    def pushCore(self, nodeToPush, rootNode, level):
        offset = self.compare(nodeToPush.name, rootNode.name, level)
        if(rootNode.children[offset] == None):
#            print("{} level {} offset {} under {}".format(nodeToPush.name, level, offset, rootNode.name))
            self.depth = level
            nodeToPush.setParent(rootNode)
            rootNode.children[offset] = nodeToPush
            
        else:
            self.pushCore(nodeToPush, rootNode.children[offset], level+1)
            
    def compare(self, baseName, pushName, index):
        baseName = baseName.lower()
        pushName = pushName.lower()

        let1 = self.letToInt(baseName[index])
        let2 = self.letToInt(pushName[index])
        
#       returns the distance between the first letter of 
#       the baseName and the first letter of pushName and
#       returns 0 if they have the same first letter
        return let1 - let2
    

    
    def search(self, search_query):
        name = self.searchCore(search_query, self.root, 0)
        return name
    
    def searchCore(self, search_query, root, level):
        search_query = search_query.lower()

#       if no more letters in the search_string, returnes the closest match.
#       this prevents a crash when the search_query is a common name like john        
        if(level >= len(search_query)):
            print("{} was returned after length was exceeded".format(root.name))
            return root.name

        #try to match the level-th letter
        offset = self.compare(search_query, root.name, level)  
        match = root.children[offset]
        
        
        if(match):
            #the entire name matched
            if(match.name[level:].lower() == search_query[level:]):
                print("match {} was returned".format(match.name))
                return match.name
            else:
#                the first letter matched
                 return self.searchCore(search_query, match, level+1)
        else:
            print("{} was returned because None was returned as a match".format(root.name))
            return root.name
        
        
        
            
    
class Node:
    def __init__(self, name):
        self.name = name
        self.children = [None for i in range(30)]
        self.parent = None
    def setParent(self, node):
        self.parent = node
        
# basic BST implementation I used as a proof of concept
# -*- coding: utf-8 -*-
#class SearchTree:
#    def __init__(self, name):
#        self.root = Node(name)
#        self.depth = 0
#        
#    def push(self, name):
#        node = Node(name)
#        self.pushCore(node, self.root, 0)
#        return self.depth
#    
#    def pushCore(self, nodeToPush, rootNode, level):
#        compareValue = self.compare(nodeToPush.name, rootNode.name)
#        if(compareValue == 0):
#            if(rootNode.right == None):
#                print("pushed {} to the right of {}".format(nodeToPush.name, rootNode.name))
#                self.temp = level
#                rootNode.right = nodeToPush
#            else:
#                self.pushCore(nodeToPush, rootNode.right, level+1)
#            
#        elif(compareValue == 1):
#            if(rootNode.left == None):
#                print("pushed {} to the left of {}".format(nodeToPush.name, rootNode.name))
#                self.depth = level
#                rootNode.left = nodeToPush
#            else:
#                self.pushCore(nodeToPush, rootNode.left, level+1)
#        else:
#            print("SOMETHING WENT HORRIBLY WRONG")
#            return
#        
#        
#    
#    def compare(self, nameA, nameB):
#        nameA = nameA.lower()
#        nameB = nameB.lower()
#        if((len(nameA) == 0) or (len(nameB) == 0)):
#            return 2;
#        
#        elif(self.letToInt(nameA[0]) > self.letToInt(nameB[0])):
##           add to right
#            return 0
#        elif(self.letToInt(nameA[0]) < self.letToInt(nameB[0])):
##           add to left
#            return 1
#        else:
#            return self.compare(nameA[1:], nameB[1:])
#    
#    def letToInt(self, letter):
#        letters = 'a b c d e é f g h i j k l m n o p q r s t u ú v w x y z .'.split(' ')
#        letters.append(' ')
#        return letters.index(letter)
#        
#class Node:
#    def __init__(self, name):
#        self.left = None
#        self.right = None
#        self.name = name
#    
#    def setLeft(self, name):
#        nodeL = Node(name)
#        self.left = nodeL
#    
#    def setRight(self, name):
#        nodeR = Node(name)
#        self.right = nodeR
#    
