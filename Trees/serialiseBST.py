from collections import deque

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "None"
        # level order traversal, keep track of parent list and children list
        serial = [root.val]
        queue = deque()
        queue.append(root)
        levels = []
        while queue:
            parents = len(queue)
            children = []
            for _ in range(parents):
                parent = queue.popleft()
                children.append(parent.left.val if parent.left else None)
                children.append(parent.right.val if parent.right else None)
                if parent.left: queue.append(parent.left)
                if parent.right: queue.append(parent.right)
            levels.append(children)
        serial.extend(element for level in levels for element in level)
        return ",".join(str(element) for element in serial)
            

    def deserialize(self, data):
        """Decodes your encoded data to tree.   
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "None":
            return None
        dataTree = [None if element == "None" else int(element) for element in data.split(',')]
        root = TreeNode(dataTree[0])
        queue = deque([root])
        treePtr = 1
        while queue and treePtr < len(dataTree):
            parents = len(queue)
            for _ in range(parents):
                parent = queue.popleft()
                if dataTree[treePtr] is not None:
                    parent.left = TreeNode(dataTree[treePtr])
                    queue.append(parent.left)
                treePtr += 1
                if treePtr == len(dataTree): break
                if dataTree[treePtr] is not None:
                    parent.right = TreeNode(dataTree[treePtr])
                    queue.append(parent.right)
                treePtr += 1
                if treePtr == len(dataTree): break
        return root
    