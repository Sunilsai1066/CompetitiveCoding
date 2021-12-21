"""
Finding Common Ancestor Of Binary Tree
Time Complexity - O(n)
Space Complexity - O(n)
"""
class Node: 
    def __init__(self,val): 
        self.val = val 
        self.right = None 
        self.left = None 

def Ancestor(root,p,q):
    if(root == None or root.val == p or root.val == q):return root
    LeftVal = Ancestor(root.left,p,q)
    RightVal = Ancestor(root.right,p,q)
    if(LeftVal == None):return RightVal
    elif(RightVal == None): return LeftVal
    else: return root

NumTree = Node(1)  
NumTree.left = Node(2)  
NumTree.right = Node(3)  
NumTree.left.left = Node(4)  
NumTree.left.right = Node(5) 

p,q = 4,5
Res = Ancestor(NumTree,p,q)
print(Res.val)
