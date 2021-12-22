class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

"""
In Iteration
Time Complexity - O(n)
Space Complexity - Since We Are Directly Printing No Space Is Needed
"""
def PrintLinkedLisIterative(head):
    while(head != None):
        print(head.val,end = ' ')
        head = head.next
    print()
    
"""
In Recursion
Time Complexity - O(n)
Space Complecity - O(n) [Even Though We're Printing Values Directly In Recursion Stack Space Is Needed]
"""
def PrintLinkedLisRecursive(head):
    if(head == None): return 
    print(head.val,end = ' ')
    PrintLinkedLisRecursive(head.next)
    
One = Node(1)
Two = Node(2)
Three = Node(3)
Four = Node(4)
One.next = Two
Two.next = Three
Three.next = Four

PrintLinkedLisIterative(One)
PrintLinkedLisRecursive(One)
