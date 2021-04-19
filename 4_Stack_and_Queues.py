#Stack and Queues
#stack is LIFO->Last in first out while queue is first out first out
#stack is like container while queue is like line of submission
#stack is built in dynamic list with end pointer while queue have two pointer front and end
#stack have push (o(1)) and pop(o(1)) function while queue have enqueue(o(1)) ,dequeue (0(1))
#in stack , end is start by -1 ,end pointer inceremented by 1 
# wile enqueue have front=-1,end=-1,in enequeue if front==-1 ->front=0 else: end+=1 and in dequeue front+=1 , if front=end, front,end=0,0
# So its all have o(1) time complexity with (o(n)) space complexity.
