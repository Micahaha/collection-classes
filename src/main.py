from node.node import *

def main():
    TestInit()

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

    print()

if __name__ == "__main__":
    main()