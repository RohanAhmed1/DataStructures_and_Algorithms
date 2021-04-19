#Binary tree is a non linear datat structure which is like a folder syttem
#pripority is from left to right.
#in other words each words break into some categories
#                  cat<-animal->dog
#start from zero level (----lvl_0----\n----lvl_1----\n) 
#height is level from root:
#complete binary tree is like a complete from left to right node but dont need to most right to be complete
#Perfect binary tree is like a complete binary tree but have a each node have 2 nodes 
#Balance tree is a difference of 0 and 1 in subtrees of each node.
#it is like in linked list having right and left
#three types of recursion,breadth first search, Depth Search
#Breadth First Search -> its like search from, above to the below
#print node on each level from left to right 
#Depth First Search; -> its like first goes into the Depth(last tree or node) then come back recursively to their root node
#   inorder -> left,root(print),right
#   preorder -> root(print),left,right
#   postorder -> left,right ,root(print)
#   Binary tree in recursion:
#       So, intraversal order(root) {
               #if root==(Null):
               #    return 
               #inorder(left <- root)
               #print(root)
               #inorder(rigt  <- root)
#              }
#   for example, 15 node calls 14 node then 14 node return to 15 node
#
#Breadth First Search or level search by iterative using queue(Google)
#Depth is the no of nodes
#  
#