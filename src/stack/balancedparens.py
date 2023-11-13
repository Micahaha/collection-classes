from stack.stack import *

class balancedParens:
    @staticmethod
    def isBalanced(exp: str):
        """Checks a specified mathematical expression to see when the 
        parenthesis are balanced.

        Args:
            expression (str): specified mathematical expression


        Returns:
            Boolean: True if parenthesis in the expression are balanced, 
            else False
        """        

        # variables for parenthesis
        LEFT_NORMAL = '('
        RIGHT_NORMAL = ')'
        LEFT_CURLY = '{'
        RIGHT_CURLY = '}' 
        LEFT_SQUARE = '['
        RIGHT_SQUARE = ']'

        # stack used to store parenthesis
        store = stack()

        # variable used to indicate imbalance
        imbalance = False

        # loop through expression a character at a time
        # as long as there isn't an imbalance
        for s in exp:
            if(not imbalance):
                if(s==LEFT_CURLY or s==LEFT_NORMAL or s==LEFT_SQUARE):
                    # if the current chracter is a (, {, or [
                    # push it onto the stack
                    store.push(s)

                elif(s==RIGHT_NORMAL):
                    # if the current character is a ), check if stack is empty
                    # or if top node doesn't contain a (
                        if(store.isEmpty() or store.pop() != LEFT_NORMAL):
                                # set imbalance to True
                                imbalance = True

                elif(s==RIGHT_SQUARE):
                    # if the current character is a ), check if stack is empty
                    # or if top node doesn't contain a (
                        if(store.isEmpty() or store.pop() != LEFT_SQUARE):
                                # set imbalance to True
                                imbalance = True

                elif(s==RIGHT_CURLY):
                    # if the current character is a ), check if stack is empty
                    # or if top node doesn't contain a (
                        if(store.isEmpty() or store.pop() != LEFT_CURLY):
                                # set imbalance to True
                                imbalance = True


        # return true fi there are no parenthesis on the stack and
        # an imbalance hasn't been found
        return (store.isEmpty() and not imbalance) 