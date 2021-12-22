class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

def PrintLinkedLisIterative(head):
    while(head != None):
        print(head.val,end = ' ')
        head = head.next
    print()
    
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
