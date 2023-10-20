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