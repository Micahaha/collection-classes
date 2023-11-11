from node.node import *

class stack:
    """Stack class that uses linked Lists of nodes as its underlying data structure.
    """

    def __init__(self):
        """Constructs an empty stack.
        """        
        self.__head = None          # A reference to the top node of the stack.
        self.__tail = self.__head   # A reference to the bottom node of the stack.
        self.__manyNodes = 0        # keeps track of the number of nodes in the stack.  


    def size(self):
        """ Returns the number of nodes in the calling stack.

        Returns:
            int: number of nodes 
        """        
        return self.__manyNodes
    

    def getHead(self):
        """Returns a reference to the head (top) of the calling stack

        Returns:
            node: Reference to the head top of the calling stack
        """        

        return self.__head

    def getTail(self):
        """Returns a reference to the tail (bottom) of the calling stack

        Returns:
            node: reference to the tail (bottom) of the calling stack
        """        

        return self.__tail

    def getData(self):
        """Returns the data values in the calling stack

        Returns:
            str: data values in the calling stack
        """        

        cursor = self.__head    #  used to step through the nodes in a calling stack
        data = ""               #  string representation of data values in the calling stack   
        i = 1                   # used to count the nodes in the calling stack

        # loop through the calling stack one node at a time, getting the data values
        # and concatening them into the data

        while(i <= self.__manyNodes):
            data = data + (str(cursor.getData()) + ' ')
            cursor = cursor.getLink()
            i += 1

        # return data
        return data

    def __str__(self):
        """Returns string representation of the calling stack 

        Returns:
            str: string representation of the calling stack
        """        
        return f"[  {self.getData()} ]"
    

    def push(self, element):
        """Pushes (adds) the specified element to the top of the calling stack.

        Args:
            element: specified element
        """        

        # if the calling stack is empty
        if(self.__head is None):
            # add node to the calling stack
            self.__head = node(element, None)
            # make tail refer to the same node as head
            self.__tail = self.__head
        else:
            # add node to the top of the stack
            self.__head = node(element, self.__head)

        # get the number of nodes in the calling stack
        self.__manyNodes = node.listLength(self.__head)


    def isEmpty(self):
        """Checks if the calling stack is empty

        Returns:
            Boolean: True if the calling stack is empty, else False
        """        
        return self.size() == 0 