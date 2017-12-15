# https://www.hackerrank.com/challenges/ctci-is-binary-search-tree/problem
# Determine whether a tree is a binary search tree
# Created 12.15.2017 by CB Fay

prev = -1
balance = True
def checkBST(node):
    global prev, balance
    if node:
        if node.left:
            checkBST(node.left)
        if node.data <= prev:
            balance = False
        prev = node.data
        if node.right:
            checkBST(node.right)
    return balance
