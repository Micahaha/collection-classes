from node.node import *
from stack.stack import *
from stack.balancedparens import *
from stack.calculator import *
from queues.queue import *
from queues.palindrome_two_queues import *

def main():

    # testEnqueue()
    # testQueueIsEmpty()
    # testDequeue()
    # testQueuePeek()
    testIsPalindrome_queues()
    m

    # TestInit()
    # testGettersAndSetters()
    # testAddNodeAfter()
    # testRemoveNodeAfter()
    # review()

    # lists: 
    # testListLength()
    # testListSearch()
    # testListPosition()
    # testListCopy()
    # testListCopyWithTail() 

    # stacks: 
    # testPush()
    # testPop()
    # testIsEmpty()
    # testPeek()
    # print("Parenthesis are balanced?", balancedParens.isBalanced("{X+Y")) # FALSE
    # print("Parenthesis are balanced?", balancedParens.isBalanced("{X+Y)")) # FALSE
    # print("Parenthesis are balanced?", balancedParens.isBalanced("({X+Y}*Z)")) # TRUE
    # print("Parenthesis are balanced?", balancedParens.isBalanced("[A+B]*({X+Y})*Z")) # TRUE
    # print("(((6+9)/3)*(6-4)) = ", calculator.evaluate("(((6+9)/3)*(6-4))"))
    # print("(6+(3*(6-4))) = ", calculator.evaluate("(6+(3*(6-4)))"))
    # print("((5+2)-(3*(6/9))) = ", calculator.evaluate("((5+2)-(3*(6/9)))"))
    # print("((5*2)-(3*(6/2))) = ", calculator.evaluate("((5*2)-(3*(6/2)))"))


# def testIsPalindrome():
#   exp = input("Please enter an expression:")
#
#    if(palindrome(exp)):
#        print("Your expression is a palindrome.")
#    else:
#        print("Your expression is not a palindrome.")
    

def testIsPalindrome_queues():
    exp = input("Please enter an expression:")


    while exp != '':
        exp = input("Please enter an expression:")
        if(palindrome.isPalindrome(exp)):
            print("Your expression is a palindrome.")
        else:
            print("Your expression is not a palindrome.")
        


def testPeek():
    print("Testing Peek Method in Stack Class")
    
    s = stack()
    print("Stack size is", s.size())            # 0
    print('Stack Contains:', s)                 # []

    s.push('S')
    print("Stack size is", s.size())            # 1
    print('Stack Contains:', s)                 # [S]
    print('Top element in stack is:', s.peek()) # S

    s.push(1)
    print("Stack size is", s.size())            # 2
    print('Stack Contains:', s)                 # [B S]
    print('Top element in stack is:', s.peek()) # B

    s.push((1,2))
    print("Stack size is", s.size())            # 3
    print('Stack Contains:', s)                 # [O B S]
    print('Top element in stack is:', s.peek()) # O

    s.push([1, 2, 3])
    print("Stack size is", s.size())            # 4
    print('Stack Contains:', s)                 # [J O B S]
    print('Top element in stack is:', s.peek()) # J


def testIsEmpty():
    print("Testing Is Empty Method in Stack Class")

    s = stack()
    s.push('S')
    s.push('B')
    s.push('O')
    s.push('J')

    print("Stack size is", s.size()) # 4
    print('Stack Contains:', s) # [J O B S]

    while(not s.isEmpty()):
        print("Just popped:", s.pop())

    print("Stack size is:", s.size()) # 0
    print("Stack contains:", s) # []

def testPop():
    print("Testing Pop Method in Stack Class")

    s = stack()
    s.push('S')
    s.push('B')
    s.push('O')
    s.push('J')

    print("Stack size is", s.size()) # 4
    print("Stack contains:", s) # [J O B S]
    print("Just popped:", s.pop()) # J

    print("Stack size is", s.size()) # 3
    print("Stack contains:", s) # [O B S]
    print("Just popped:", s.pop()) # O

    print("Stack size is", s.size()) # 2
    print("Stack contains:", s) # [B S]
    print("Just popped:", s.pop()) # B

    print("Stack size is", s.size()) # 1
    print("Stack contains:", s) # [S]
    print("Just popped:", s.pop()) # S


# def testPush():
    print("Testing Push Method in stack Class")

    s = stack()
    print("Stack size is:", s.size())       # 0
    print("Stack size contains", s)         # []

    s.push('S')
    print("Stack size is", s.size())       # 1
    print("Stack contains", s)             # [S]

    # s.push('B')
    s.push(1)
    print("Stack size is", s.size())       # 2
    print("Stack contains", s)             # [B S]

    # s.push('O')
    s.push((1,2))
    print("Stack size is", s.size())       # 3
    print("Stack contains", s)             # [O B S]

    # s.push('J')
    s.push([1,2,3])
    print("Stack size is", s.size())       # 4
    print("Stack contains", s)             # [J O B S]


def testListCopyWithTail():
    print("Testing List Copy")

    # construct a node with data equal to S and link equal to None
    # and assign its reference to a head
    source = node('S', None) # S

    # construct a node with data equal to B and link equal to head
    # and assign its reference to a head
    source = node('B', source) # B -> S

    # construct a node with data equal to O and link equal to head
    # and assign its reference to a head
    source = node('O', source) # O -> B -> S

   # construct a node with data equal to S and link equal to None
   # and assign its reference to a head
    source = node('J', source) # J -> O -> B -> S

    copy = node.listCopyWithHead(source) 
    # [J -> O -> B -> S, S]


    print("Source contains", node.listPosition(source,1).getData(),
          node.listPosition(source,2).getData(),
          node.listPosition(source,3).getData(),
          node.listPosition(source,4).getData(),
    )

    print("Copy contains", node.listPosition(copy[0],1).getData(),
          node.listPosition(copy[0],2).getData(),
          node.listPosition(copy[0],3).getData(),
          node.listPosition(copy[0],4).getData(),
    )
    print("Copy tail contains", node.listPosition(copy[1],1).getData())





def testListCopy():
    print("Testing List Copy")

     # construct a node with data equal to S and link equal to None
    # and assign its reference to a head
    source = node('S', None) # S

    # construct a node with data equal to B and link equal to head
    # and assign its reference to a head
    source = node('B', source) # B -> S

    # construct a node with data equal to O and link equal to head
    # and assign its reference to a head
    source = node('O', source) # O -> B -> S

   # construct a node with data equal to S and link equal to None
   # and assign its reference to a head
    source = node('J', source) # J -> O -> B -> S

    copy = node.listCopy(source)

    print("Source contains", node.listPosition(source,1).getData(),
          node.listPosition(source,2).getData(),
          node.listPosition(source,3).getData(),
          node.listPosition(source,4).getData(),
    )

    print("Copy contains", node.listPosition(copy,1).getData(),
          node.listPosition(copy,2).getData(),
          node.listPosition(copy,3).getData(),
          node.listPosition(copy,4).getData(),
    )




# def testListPosition():
    print("Testing List Position")

    # construct a node with data equal to S and link equal to None
    # and assign its reference to a head
    head = node('S', None) # S

    # construct a node with data equal to B and link equal to head
    # and assign its reference to a head
    head = node('B', head) # B -> S

    # construct a node with data equal to O and link equal to head
    # and assign its reference to a head
    head = node('O', head) # O -> B -> S

   # construct a node with data equal to S and link equal to None
   # and assign its reference to a head
    head = node('J', head) # J -> O -> B -> S

    print("First node contains data:", node.listPosition(head,1).getData())
    print("Second node contains data:", node.listPosition(head,2).getData())
    print("Third node contains data:", node.listPosition(head,3).getData())
    print("Fourth node contains data:", node.listPosition(head,4).getData())

    if (node.listPosition(head,5) != None):
        print("Fourth node contains data:", node.listPosition(head,5).getData())
    else:
        print('There is no Fifth node')        


# def testListSearch():
    print("Testing List Search")

    # construct a node with data equal to S and link equal to None
    # and assign its reference to a head
    head = node('S', None) # S

    # construct a node with data equal to B and link equal to head
    # and assign its reference to a head
    head = node('B', head) # B -> S

    # construct a node with data equal to O and link equal to head
    # and assign its reference to a head
    head = node('O', head) # O -> B -> S

   # construct a node with data equal to S and link equal to None
   # and assign its reference to a head
    head = node('J', head) # J -> O -> B -> S

    print("Length of head is: ", node.listLength(head))

    print("Head contains:", node.listSearch(head, 'J').getData())
    print("Head contains:", node.listSearch(head, 'O').getData())
    print("Head contains:", node.listSearch(head, 'B').getData())
    print("Head contains:", node.listSearch(head, 'S').getData())

    if(node.listSearch(head, 'Z') != None):
        print("Head contains:", node.listSearch(head, 'Z').getData())
    else:
        print("Head doesn't contain Z.")


# def testListLength():
    print("Testing List Length")

    # construct a node with data equal to S and link equal to None
    # and assign its reference to a head
    head = node('S', None) # S

    # construct a node with data equal to B and link equal to head
    # and assign its reference to a head
    head = node('B', head) # B -> S

    # construct a node with data equal to O and link equal to head
    # and assign its reference to a head
    head = node('O', head) # O -> B -> S

   # construct a node with data equal to S and link equal to None
    # and assign its reference to a head
    head = node('J', head) # J -> O -> B -> S

    print("Length of head is: ", node.listLength(head))




# def testRemoveNodeAfter():
    print('Testing Remove Node After')

    # construct a node with data equal to S and link equal to None
    # and assign its reference to a head
    head = node('S', None) # S

    # construct a node with data equal to B and link equal to head
    # and assign its reference to a head
    head = node('B', head) # B -> S

    # construct a node with data equal to O and link equal to head
    # and assign its reference to a head
    head = node('O', head) # O -> B -> S

   # construct a node with data equal to S and link equal to None
    # and assign its reference to a head
    head = node('J', head) # J -> O -> B -> S

    print("The head node contains data", head.getData())

    # Remove the node after the node head refers to (node that has data equal to O)
    head.removeNodeAfter() # J -> B -> S    

    head = head.getLink() # B -> S

    print("The head node contains data", head.getData())

    # Remove the node after the node head refers to (node that has data equal to S)
    head.removeNodeAfter() # B

    print("The head node contains data", head.getData())

    """    
    # Remove the node after the node head refers to (node that has data equal to S)
    head.removeNodeAfter() this line of code will generate an AttributeError"""



# def review():

    # Question 1: 
    print('Review')
    head = node('X', None) # X
    head = node('X', head) # X
    head = node('X', head) # X
    head = node('X', head) # X

    # Question 2
    selection1 = head

    # Question 3
    selection1.addNodeAfter('O')

    # Question 4
    selection1 = selection1.getLink()
    selection1 = selection1.getLink()

    # Question 5
    selection1.addNodeAfter('O')

    # Question 6
    selection1 = selection1.getLink()
    selection1 = selection1.getLink()

    # Question 7
    selection1.addNodeAfter('O')

    # Question 8
    tail = head

    # Question 9

    tail = tail.getLink()
    tail = tail.getLink()
    tail = tail.getLink()
    tail = tail.getLink()
    tail = tail.getLink()
    tail = tail.getLink()

    # Question 10
    selection2 = head

    # Question 11
    selection2 = selection2.getLink()
    selection2 = selection2.getLink()

    # Question 12
    head.setData('A')
    selection2.setData('A')
    selection2.setData('A')
    tail.setData('A')

    # Question 13
    head.removeNodeAfter()
    selection1.removeNodeAfter()
    selection2.removeNodeAfter()



# def testAddNodeAfter():
    print('Testing Add Node After')
    head = node('J', None) # J

    print("The head node contains data:", head.getData())

    # declare a new node named selection and make it refer
    # to the same node as head
    selection = head
    print("The head node contains data:", head.getData())
    print("The selection node contains data:", selection.getData())

    # add a node with data equal to O after the node selection
    # refers to 
    selection.addNodeAfter('O') # J -> O

    # get selection's link and assign its reference back to
    # selection
    selection = selection.getLink() # O
    
    print("The head node contains data:", head.getData())
    print("The selection node contains data:", selection.getData())

    # add a node with data equal to O after the node selection
    # refers to 
    selection.addNodeAfter('B') # O -> B

    # get selection's link and assign its reference back to
    # selection
    selection = selection.getLink() # B
    
    print("The head node contains data:", head.getData())
    print("The selection node contains data:", selection.getData())


 # add a node with data equal to S after the node selection
    # refers to 
    selection.addNodeAfter('S') # B -> S

    # get selection's link and assign its reference back to
    # selection
    selection = selection.getLink() # S
    
    print("The head node contains data:", head.getData())
    print("The selection node contains data:", selection.getData())

    # declare a new node named tail and make it refer to the same
    # node as head
    tail = head

    # get tail's link and assign its reference to tail
    tail = tail.getLink()
    tail = tail.getLink()
    tail = tail.getLink()

    # add a new node with data equal to Z after the node tail
    # refers to 
    tail.addNodeAfter('Z')

    # get tail's link and assign its reference to tail
    tail = tail.getLink()

    
    print("The head node contains data:", head.getData())
    print("The selection node contains data:", selection.getData())
    print("The tail node contains data:", tail.getData())

# def testGettersAndSetters():
    print('Testing Getters and Setters')

    # construct a node with data equal to S and link equal to None
    # and assign its reference to a head
    head = node('R', None) # R

    print("The head node contains data:", head.getData())

    head.setData('S') # S
    print("The head node contains data:", head.getData())

    head = node('B', head) # B -> S
    print("The head node contains data:", head.getData())

    head = node('O', head) # O -> B -> S
    print("The head node contains data:", head.getData())

    head = node('J', head) # J -> O -> B -> S
    print("The head node contains data:", head.getData())

    # get head's link and assign its reference back to head
    head = head.getLink()
    print("The head node contains data:", head.getData())

    # get head's link and assign its reference back to head
    head = head.getLink()
    print("The head node contains data:", head.getData())

    # get head's link and assign its reference back to head
    head = head.getLink()
    print("The head node contains data:", head.getData())

    # get head's link and assign its reference back to head
    ### head = head.getLink()
    ### print("The head node contains data:", head.getData())

    print("The head node contains link:", head.getLink())

    # set head's link to a new node
    head.setLink(node('O', None)) # S -> O

# def TestInit():
    print("Testing Node Init")

    # construct a node with data equal to S and link equal to None
    # and assign its reference to a head
    head = node('S', None) # S

    # construct a node with data equal to B and link equal to head
    # and assign its reference to a head
    head = node('B', head) # B -> S

    # construct a node with data equal to O and link equal to head
    # and assign its reference to a head
    head = node('O', head) # O -> B -> S

    # construct a node with data equal to O and link equal to head
    # and assign its reference to a head
    head = node('J', head) # J -> O -> B -> S


    head = node(1, head) # 1-> J -> O -> B -> S
    head = node(1.5, head) # 1.5 -> 1 -> J -> O -> B -> S
    head = node([1,2], head) # [1,2] ->1.5 -> 1 -> J -> O -> B -> S
    head = node(('A','B'), head) # ('A', 'B') ->[1,2] ->1.5 -> 1 -> J -> O -> B -> S

    list = ['a','b','c','d']
    list.pop()
    print()


def testEnqueue():


    print("Testing Enqueue")

    my_queue = queue()
    my_queue.enqueue('J')
    my_queue.enqueue('O')
    my_queue.enqueue('B')
    my_queue.enqueue('S')

  
    print("Queue size is", my_queue.size()) # 4
    print('Queue Contains:', my_queue) # [J O B S]

def testQueueIsEmpty():
    print('\n')
    print("Testing IsEmpty Method in Queue Class")

    my_queue = queue()
    my_queue.enqueue('J')

    print("Queue size is", my_queue.size()) # 4
    print('Queue Contains:', my_queue) # [J O B S]

    my_queue.enqueue('O')

    print("Queue size is", my_queue.size()) # 4
    print('Queue Contains:', my_queue) # [J O B S]

    my_queue.enqueue('B')    
  
    print("Queue size is", my_queue.size()) # 4
    print('Queue Contains:', my_queue) # [J O B S]

    my_queue.enqueue('S')

    print("Queue size is", my_queue.size()) # 4
    print('Queue Contains:', my_queue) # [J O B S]

    print('\n')
    while(not my_queue.isEmpty()):
        print("Just dequeued:", my_queue.dequeue())

    print("Queue size is", my_queue.size()) # 4
    print('Queue Contains:', my_queue) # [J O B S]

def testDequeue():
    print('\n')
    print("Testing Dequeue Method in Queue Class")


    my_queue = queue()
    my_queue.enqueue('J')
    my_queue.enqueue('O')
    my_queue.enqueue('B')
    my_queue.enqueue('S')

    
    print("Queue size is", my_queue.size()) # 4
    print('Queue Contains:', my_queue) # [J O B S]
    print("Just Dequeued:", my_queue.dequeue()) # J

    print("Queue size is", my_queue.size()) # 3
    print('Queue Contains:', my_queue) # [O B S]
    print("Just Dequeued:", my_queue.dequeue()) # O

    print("Queue size is", my_queue.size()) # 2
    print('Queue Contains:', my_queue) # [B S]
    print("Just Dequeued:", my_queue.dequeue()) # B

    print("Queue size is", my_queue.size()) # 1
    print('Queue Contains:', my_queue) # [S]
    print("Just Dequeued:", my_queue.dequeue()) # S

def testQueuePeek():
    print('\n')
    my_queue = queue()
    my_queue.enqueue('J')
    my_queue.enqueue('O')
    my_queue.enqueue('B')
    my_queue.enqueue('S')

    print(f'Head at front of Queue: {my_queue.peek()}')





if __name__ == "__main__":
    main()
