#val is some integer value
#Pointer is like a container likewise in "a=3", the "a" is a container of int 3
#it have a big advantage of the space. it is normally like a o(1) space in different programs.
#it have also a advantage of adding and deletion at first index.

# Definition for singly-linked list.
#head is always the pointer which point the first node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next       
#ListNode contains the integer and the pointer of the next node, for example a=3,b=3. So, node is like [3,b]
#ListNode(l1,l2,l3,...) is like a pointer of Node contains data and pointer
#l1,l2,l3,.....=ListNode(data,pointer)
#---pointer--- = ---------Node--------
#Node have a address temp

#Other definition for singly-linked list.
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
class SinglyLinkedList:
    def __init__(self):
        self.headval = None #Pointer
    
    def SLL_Traverse(self):                            # 1, 2, 3, 4, 5, 6, 7, 8
        a = self.headval                               # a check the current node
        while a.next != None:                          # Same as Above, the pointer will at outside the SLL
            print(a.val, end=" ")                      # if the next node is present then the current node will print
            a = a.next                                 # while a.next check the other node
        print()                                        # 1->2,2->3,4->5,6->7,8->None , the pointer will at last node 
                                                       # if the next node is present then the current node will print
    def addFirstNode(self,temp):
        temp.next=self.headval                         #Always first the pointer of the given node to the point of the head,   Pointer to Result Node              
        self.headval=temp                              #Now, the head to Node,                                                 Pointer in Given Node

    def addIndexNode(self,temp,index):
        a=self.headval                                 # We initialze new pointer to access data of each node
        for i in range(index):                         # Loop will continue index times
            a=a.next                                   #we never move head
        temp.next = a.next
        a.next = temp


#initializing Linked List
SLL=SinglyLinkedList()

e1 = Node("Mon")

SLL.headval = e1

#other Nodes
e2 = Node("Tues")
e3 = Node("Wednes")
e4 = Node("Thurs")
e5 = Node("Fri")
e6 = Node("Sat")
e7 = Node("Sun")

#Attaching Nodes
e1.next=e2
e2.next=e3
e3.next=e4
e4.next=e5
e5.next=e6
e6.next=e7

#traversing
SLL.SLL_Traverse()

#add first node
e_int=Node(1)
SLL.addFirstNode(e_int)

#traversing
SLL.SLL_Traverse()

#add first node
e_int_i=Node(2)
SLL.addIndexNode(e_int_i,3)    #Loop will continue 3 times 

#traversing
SLL.SLL_Traverse()

SLL.reverseList()
SLL.SLL_Traverse()



