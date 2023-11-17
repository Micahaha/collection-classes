from stack.stack import *
from node.node import *

def selectionsort (data: stack, first: int):
    """Sorts a stack from smallest to largest 
    bypassing the nodes to the left of first 

    Args:
        data (stack): list of integers 
        first (int): the list index at which the
    """    

    # Initialize loop counter variable named i 
    i = data.size()

    # initalize loop counter variable named j to 0 
    j = 0

    # initialize variable named big that will be used
    # to store index of the biggest value
    big = 0

    # initalize variable named temp that will be used to swap list values
    temp = 0


    # loop through list as many times as specified by 
    # len(data) and first
    # this loop represents the blue arrow
    
    while (i  > 0):
        # set big equal to first
        big = first

        # set j = first + 1
        j = first + 1

        # loop through list starting with element at
        # first + 1 and continue until reach first + i 
        # this loop represents the yellow arrow
        while (j <= first + 1):
        
        # if value in data[big] is less than data[j]
        # set big equal to j
        # increment j by 1

            if (node.listPosition(data.getHead(), big).getData() < node.listPosition(data.getHead(), j).getData()):
            
                # set big = j
                big = j

            # increment j by 1
            j += 1

            # swap the data in first + 1 with the data in big
            # set temp to value in data[first + i] 

            data.getHead().setDataAtPosition(first+i, big)
            temp = node.listPosition(data.getHead(),first+i).getData()

            # set data[first + i] to value in data[big]
            data.getHead().setDataAtPosition(first+i, big)
            

            # set data[big] to value in temp
            data.gethead()

            
        i-=1



def main():
    s = stack()
    s.push(8)
    s.push(63)
    s.push(3)
    s.push(39)
    s.push(70)
    s.push(42)
    s.push(-7)

    selectionsort(s,1)
    print(s)
main()