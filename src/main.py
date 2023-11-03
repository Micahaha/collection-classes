from node.node import *

def main():
    # TestInit()
    # testGettersAndSetters()
    # testAddNodeAfter()
    # testRemoveNodeAfter()
    # review()
    # testListLength()
    # testListSearch()
    # testListPosition()
    # testListCopy()
    testListCopyWithTail() 

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




def testListPosition():
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


def testListSearch():
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


def testListLength():
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




def testRemoveNodeAfter():
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



def review():

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



def testAddNodeAfter():
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

def testGettersAndSetters():
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

def TestInit():
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

    print()



if __name__ == "__main__":
    main()