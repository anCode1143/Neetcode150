def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
    pAncestors = set()
    pAncestor = p
    while pAncestor.parent:
        pAncestors.add(pAncestor)
        if pAncestor == q:
            return pAncestor
        pAncestor = pAncestor.parent
    qAncestor = q
    while qAncestor.parent and qAncestor not in pAncestors:
        qAncestor = qAncestor.parent
    return qAncestor


"""
how to implement the solution
    go up from one node, saving all nodes as ancestors
        if any is the other target, return immediately
    go up from other node, until an ancestor from the set is reached

complexity details
    speed - linear, iterating up from target, doing constant speed comparing operations
    memory - linear, saving nodes from one target
"""