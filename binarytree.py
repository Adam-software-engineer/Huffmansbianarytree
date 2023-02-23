# Huffmen tree practise day 1
# huffmen tree practise day 2 worked on fixing the node 

# error fix init needs two of the lines of the sides so 
# example  __init__ not _init_ needs two 


# you need the paramaters self,freq,,symbol,left=None,right=None

class node:
        # __init__ needs too have too of the lines or it gives
        # error for the nodes why can't it just work
        def __init__(self,freq,symbol,left=None,right=None):
                # Will make the freq the symbol comes up 
                self.freq = freq
                
                #will add the charaters of the symbol
                self.symbol = symbol
                
                #will add the left node
                self.left = left
                
                #will add the right node
                self.right = right
                
                #will add huffmens tree
                self.huff = ""
            
        
    # will then have to add a new def for the newly 
    # printed huffmen tree

def printNode(node,val=""):
        
        newval = val + str(node.huff)
            
        if(node.left):
                printNode(node.left, newval)
        if(node.right):
                printNode(node.right, newval)
                
        if(not node.left and not node.right):
                print(f"{node.symbol} -> {newval}")
            

# create charters for tree
chars = ['a','b','c','d','e','f']

#create the freq of charters 
freq = [5,9,12,13,16,45]
        
#Create a list where you can put the unused nodes 
nodes = []

    #converte the charters and the freq 
    #into the huffmens code
for x in range(len(chars)):
    #fix the node it is saying that it does not take an argument 
    nodes.append(node(freq[x], chars[x]))                       
        
while len(nodes) > 1:
    #this will sort the nodes in assending order
    nodes = sorted(nodes, key = lambda x: x.freq)
        
    #pick 2 smalles nodes
    left = nodes[0]
    right = nodes[1]
        
    #assisgn directionl of value to the nodes
    left.huff = 0
    right.huff = 1
        
    #combine the 2 smallest nodes to make a parent node
    newNode = node(left.freq + right.freq, left.symbol + right.symbol, left, right)
        
    #remove the 2 nodes and add the parents 
    nodes.remove(left)
    nodes.remove(right)
    nodes.append(newNode)
        
        
#print the tree
printNode(nodes[0])

#Adam steinberg 4/17/2022 huffmen tree 
#it finally works i should go back to copy and pasting things 

        
        
        