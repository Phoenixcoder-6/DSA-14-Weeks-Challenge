class Tree:
    def __init__(self, val=0, left=None, right = None):
        self.val= val
        self.left= left
        self.right=right

def build_tree(arr, index=0):
    if index >= len(arr) or arr[index] is None:
        return None
    root= Tree(arr[index])
    root.left= build_tree(arr, 2*index + 1)
    root.right= build_tree(arr, 2 *index + 2)
    return root

def pre_order(root):
    result=[]
    def dfs(node):
        if not node:
            return 
        else:
            result.append(node.val)
            dfs(node.left)
            dfs(node.right)
    dfs(root)
    return result

arr=[1,2,3,4,5,6,7,8,9,10]
root= build_tree(arr)
res= pre_order(root)
print(res)
