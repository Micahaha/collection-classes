from queues.queue import *

class Palindrome:
    @staticmethod 
    def isPalindrome(expression: str):
        """Check if the expression given reads the same forward and backward.

        Args:
            expression (str): Specified expression 

        Returns: 
            Tuple[bool, Optional[str]]: True if the specified expression is a palindrome, 
                                        else False. If False, the second element of the tuple 
                                        contains the part of the string where the mismatch happens.
        """        

        q = queue()  # queue to read the expression forward
        q2 = queue()  # stack to read the expression backward
        line = queue()  # queue to store characters where the mismatch is detected

        mismatches = 0  # used to keep track of the differences in the queue and stack   
        mismatch_string = ""  # part of the string where the mismatch happens

        # convert expression to upper-case 
        expression = expression.upper()

        # loop through the expression a character at a time
        for e in expression:
            # if the current character is an alphabetic character
            if e.isalpha():
                # enqueue it into both queues
                q.enqueue(e)
                q2.enqueue(e)

        i = 0  # variable to manually track position without using enumerate

        # while both queues have elements and no mismatches detected
        while not q.isEmpty() and not q2.isEmpty() and mismatches == 0:
            current_char_q = q.dequeue()
            current_char_q2 = q2.dequeue()

            # if the element at the front of the queue isn't
            # equal to the element at the front of the second queue
            if current_char_q != current_char_q2:
                # increment mismatches, update mismatch_string, and enqueue to line
                mismatches += 1
                mismatch_string = expression[i]  # part of the string where the mismatch happens
                line.enqueue(expression[:i])  # enqueue the entire string up to the mismatch
            else:
                # if characters match, enqueue to line
                line.enqueue(current_char_q)

            i += 1  # manually increment position

        # print the entire string up to the mismatch
        print("Mismatch detected at:", end=' ')
        while not line.isEmpty():
            print(line.dequeue(), end='')

        # return True if mismatches is equal to 0, else return False and the mismatch_string
        return (mismatches == 0, mismatch_string if mismatches > 0 else None)