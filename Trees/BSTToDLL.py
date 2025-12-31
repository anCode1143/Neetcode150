def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
    if not root:
        return root
    orderNodes = []

    def inOrderAppend(node):
        if node.left:
            inOrderAppend(node.left)
        orderNodes.append(node)
        if node.right:
            inOrderAppend(node.right)
    inOrderAppend(root)
    if len(orderNodes) == 1:
        return root

    for nodeIndex in range(len(orderNodes)):
        if nodeIndex == 0:
            root = orderNodes[nodeIndex]
            orderNodes[nodeIndex].left = orderNodes[-1]
            orderNodes[nodeIndex].right = orderNodes[nodeIndex+1]
        elif orderNodes[nodeIndex] == orderNodes[-1]:
            orderNodes[nodeIndex].left = orderNodes[nodeIndex-1]
            orderNodes[nodeIndex].right = orderNodes[0]
        else:
            orderNodes[nodeIndex].left = orderNodes[nodeIndex-1]
            orderNodes[nodeIndex].right = orderNodes[nodeIndex+1]
    return root

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def helper(node):
            """
            Performs standard inorder traversal:
            left -> node -> right
            and links all nodes into DLL
            """
            nonlocal last, first
            if node:
                # left
                helper(node.left)

                # node 
                if last:
                    # link the previous node (last)
                    # with the current one (node)
                    last.right = node
                    node.left = last
                else:
                    # keep the smallest node
                    # to close DLL later on
                    first = node        
                last = node

                # right
                helper(node.right)
        
        if not root:
            return None
        
        # the smallest (first) and the largest (last) nodes
        first, last = None, None
        helper(root)

        # close DLL
        last.right = first
        first.left = last
        return first