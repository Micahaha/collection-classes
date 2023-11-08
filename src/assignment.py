from node.node import node


def assignment():

    # construct a node with data equal to 2 and link equal to None
    # and assign its reference to a head
    head = node(2, None) 

    # construct a node with data equal to '=' and link equal to None
    # and assign its reference to a head
    head = node('=', head) 

    # construct a node with data equal to 1 and link equal to None
    # and assign its reference to a head
    head = node(1, head) 

    # construct a node with data equal to '+' and link equal to None
    # and assign its reference to a head
    head = node('+', head)

    # construct a node with data equal to '1' and link equal to None
    # and assign its reference to a head
    head = node(1, head)


    # set operator to head
    operator = head
    # set result to head
    result = head

    # set the operator to the linked node
    operator = operator.getLink()


    # iterate result to first node
    result = result.getLink()
    result = result.getLink()
    result = result.getLink()
    result = result.getLink()
    
    # set operator to be subtraction
    operator.setData('-')
    # set the result to 0
    result.setData(0)
    # set operator to be multiplication
    operator.setData('*')
    # set operator to 1
    operator.setData(1)
    # set operator to division
    operator.setData('/')
    # set result to 1
    result.setData(1)
    # set data to 7
    head.setData(7)
    # set result to 7
    result.setData(7)
    # get last linked node
    operator = operator.getLink()
    # remove node after operator
    operator.removeNodeAfter()
    # remove node after head
    head.removeNodeAfter()

    print(f'head contains {node.listLength(head)} nodes')
    print(f'Operator contains {node.listLength(operator)} nodes')
    print(f'Result contains {node.listLength(result)} node')

    print()
    # make copies of the head node
    copy = node.listCopyWithHead(head)

    # check length of each linked list of nodes
    print(f'copy[0] contains {node.listLength(copy[0])} nodes')
    print(f'copy[1] contains {node.listLength(copy[1])} node')

    # search to see if copy[0] contains 1
    if(node.listSearch(copy[0],1) != None):
        print(f"copy[0] contains character 1")

    # search to see if copy[1] contains 1
    if(node.listSearch(copy[1],1) == None):
            print(f"copy[1] doesn't contain character 1")

    


    
assignment()