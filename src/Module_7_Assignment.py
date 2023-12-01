from queues.queue import *
from stack.stack import *
from queues.palindrome_mismatch import *



def testPalindrome_mismatch():
    exp = input("Please enter an expression:")


    result, mismatch_part = Palindrome.isPalindrome(exp)
    print(f"\nIs the expression a palindrome? {result}")
    if not result:
        print(f"Mismatched detected at: {mismatch_part}")

        

testPalindrome_mismatch()