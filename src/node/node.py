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