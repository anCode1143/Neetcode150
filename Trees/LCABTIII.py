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