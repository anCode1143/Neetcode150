def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """

    s_sorted = "".join(sorted(s))
    t_sorted = "".join(sorted(t))
    if (s_sorted == t_sorted):
        return True
    return False

