# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 09:12:17 2019

@author: Caizhi Xu
"""

## Tree traversal, no recursion

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
def preOrder(root):
    if not root:
        return None
    current = root
    stack = []
    result = []
    while current:
        result.append(current.val)
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
            
        if stack:
            current = stack.pop()
        else:
            current = None
    return result

def inOrder(root):
    if not root:
        return None
    current = root
    stack = []
    result = []
    while True:
        while current:
            stack.append(current)
            current = current.left
        if not stack:
            return result
        current = stack.pop()
        result.append(current.val)
        current = current.right            

def postOrder(root):
    if not root:
        return None
    current = root
    stack = []
    result = []
    while current:
        result.append(current.val)
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)
                    
        if stack:
            current = stack.pop()
        else:
            current = None
    result.reverse()
    return result

def levelOrder(root):
    if not root:
        return None
    stack = [root]
    result = []
    while stack:
        length = len(stack)
        for i in range(length):
            result.append(stack[i].val)
            if stack[i].left:
                stack.append(stack[i].left)
            if stack[i].right:
                stack.append(stack[i].right)
        stack = stack[length:]
    return result


root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5)
#print(preOrder(root))
test = inOrder(root)
print(test)
#print(levelOrder(root))
#print(postOrder(root))




""" Templates got from others"""
## templates
def preOrder(root):
    stack, res = [], []
    curr = root
    while stack or curr:
        if curr:
            res.append(curr.val)
            stack.append(curr)
            curr = curr.left
        else:
            curr = stack.pop()
            curr = curr.right
    return res

def inOrder(root):
    stack, res = [], []
    curr = root
    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        res.append(curr.val)
        curr = curr.right
    return res

def postOrder(root):
    stack = []
    res = deque()
    curr = root
    while stack or curr:
        if curr:
            res.appendleft(curr.val)
            stack.append(curr)
            curr = curr.right
        else:
            curr = stack.pop()
            curr = curr.left
    return res

