from node.node import *
from stack.stack import *

def search(a: stack, first: int, size: int, target: int):
    """Searches for a target value in a stack of noses
    starting at first.

    Args:
        a (stack):  the stack to search
        first (int): the list index at which the search will start
        size (int): the number of elements to search
        target : the elmenet to srarch

    Returns:
        int: If target appears in the list, index of the element 
        that contains the target. else -1  
    """    

    # set an int variable i = 0 
    i = 0

    # set a boolean variable found to false
    found = False

    # while there are more elements to search 
    # and the target hasn't been found 
    # i plus first doesn't exceed the length of the list
    while((i < size) and not found and (i + first < len(a))):
        # if the current element is the target
        if(a[i + first] == target):
            # set found to true 
            found = True
        else:
            # increment by 1 
            i += 1
    
    # check if the target was found
    if (found):
        # return index of the target
        return i + first
    else:
        # return negative 1 
        return -1
    




def testSerialSearch():
    # create an empty stack
    _a = stack()
    
    # initialize first
    first = 1
    
    # initialize size

    size = 7
    
    # initialize target
    target = 70
    
    # push -7 onto the top of the stack
    _a.push(-7)

    # push 42 onto the top of the stack
    _a.push(42)

    # push 70 onto the top of the stack
    _a.push(70)

    # push 39 onto the top of the stack
    _a.push(39)

    # push 3 onto the top of the stack
    _a.push(3)

    # push 63 onto the top of the stack
    _a.push(63)

    # push 8 onto the top of the stack
    _a.push(8)

    # print the stack
    print(_a)

    # call serial search method and display its return.
    print(search(_a,first,size,target))


if __name__ == "__serialsearch__":
    testSerialSearch()
