# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return None
        stack = []
        stack.append(root)
        result = []
        flag = 0
        while len(stack):
            #print(stack)
            #root = stack.pop()
            if root.left != None and flag == 0:
                stack.append(root.left)
                flag = 0
                root = root.left
                #print(1)
                #print(result)
            else:
                root = stack.pop()
                result.append(root.val)
                if root.right != None:
                    stack.append(root.right)
                    flag = 0
                    root = root.right
                    #print(2)
                    #print(result)
                elif len(stack)!=0:
                    root = stack[len(stack)-1]
                    flag = 1
                    #print(3)
                    #print(result)
        #result.append(root.val)
        #print(result)
        return result
