#Binary Search
#work in sorted array and usually left and right pointer work on index.
#calculate the mid of the array in each mid break of the array  
#Its time complexity is o(logn) which is in the between of O(1) and O(n)

#its mid formula is mid(m),right(r),left(l) is m=(l+r)/2 == m=l + (r-l)/2 -> l - l/2 + r/2 -> l/2 + r/2 = (l+r)/2
#m=l + (r-l)/2 (its for the overflow of the limited integer) for example ,only upto 10 integer exist so 5+10 can be 15 which is not exist
#left and right can be overlapped maximum

#normal alogorithm ->
A=[1,2,3,4,5,6,7,8,9,10]
t=10
l=0
r=len(A)-1
while l<=r:
    m=int( (l+r)/2 )
    if t < A[m]:
        r=m-1
    elif t> A[m]:
        l=m+1
    else:
        print(True)
        break
print(False)

#for repeated integers -> left most
A=[1,2,3,4,4,4,5,6,7]
t=4 #left most
l=0
r=len(A)-1
while l < r:
    m = int( (l+r)/2 )
    if t > A[m]:
        l=m+1
    else:   #both conditions
        r=m
print(m)

#for repeated integers -> right most

#integers
def func():
    func()

#only in one stack , if two function ,then changes into only one stack
#maximum calls is our soace complexity




        