class node:
    """The node class holds a collection of values using nodes. It includes methods that allow the nodes 
    to be manipulated.
    """     

    def __init__(self, data, link):
        """Constructs a node using the specified data and link.

        :ivar __data: data value of the node
        :ivar __link: link portion of the node 

        Args:
            data (_type_): data value
            link (_type_): specified link
        """

        self.__data = data
        self.__link = link


    def getData(self):
        """Returns the data value stored in the calling node
        
        Returns:
            _type_: data value store in the calling node.
        """

        return self.__data
    
    def setData(self, data):
        """Sets the data value stored in the calling node 
        to the specified data value.

        Args:
            data (_type_): Specified data value
        """        
        self.__data = data

    def getLink(self):
        """Returns the link stored in the calling node.

        Returns:
            node: link stored in the calling node
        """         
        return self.__link
    
    def setLink(self, link):
        """Sets the link stored in the calling node of the specified link

        Args:
            link (node): specified link
        """        

        self.__link = link

    def addNodeAfter(self, element):
        """Adds a new node containing a specified element value 
        at a selectected position in the calling node.

        Args:
            element (_type_): specified element value
        """        
        
        self.__link = node(element, self.__link)
    
    def removeNodeAfter(self):
        """Removes a node from the selected position in the calling node.
        """        
        self.__link = self.__link.__link

    @staticmethod
    def listLength(head):
        """Computes and returns the number of nodes in a specified node.

        Args:
            head (node): specified node

        Returns:
           int: number of nodes 
        """        
        cursor = head   # cursor used to ste through the specified node
        length = 0      # used to count the nodes

        # step through the nodes in the specified node as long as the 
        # cursor isn't null
        while (cursor != None):
            # increment length
            length += 1

            # move cursor to next node
            cursor = cursor.getLink()

        # return length 
        return length
    
    @staticmethod
    def listSearch(head, target):
        """Search for a specified target in a specified node.

        Args:
            head (node): specified node
            target: specified target
        
        Returns:
            node: reference to node that contains specified target value
            if specified target value is found, else None
        """

        cursor = head   # cursor used to STEP through the specified node

        # step through the nodes in the specified node as long as the 
        # cursor isn't null
        while (cursor != None):
            # check if the data value in the node cursor refers to is equal
            # to the target
            if (cursor.getData() == target):
                # return cursor
                return cursor

            # move cursor to next node
            cursor = cursor.getLink()

        # return None 
        return None
    
    @staticmethod
    def listPosition(head, position: int):
        """Search for a node in a specified node based on a specified position.

        Args:
            head (node): specified node
            position (int): specified position

        Raises:
            ValueError: indicates position is less than one

            
        Returns: 
            node: reference to node at specified position if specified position 
            is found, else None
        """         
