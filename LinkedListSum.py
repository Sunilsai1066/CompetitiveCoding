"""
Program To Find Sum Of Node Values In Linked List
Time Complexity - O(n)
Space Complexity - O(1)
"""
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

def LinkedListSum(head):
    Sum = 0
    while(head != None):
        Sum += head.val
        head = head.next
    return Sum

Link1 = Node(2)
Link2 = Node(5)
Link3 = Node(7)
Link4 = Node(9)

Link1.next = Link2
Link2.next = Link3
Link3.next = Link4

print(LinkedListSum(Link1))
