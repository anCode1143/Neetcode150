def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    ranking = {}
    m_pointer, n_pointer = 0, 0
    for rank in range(m + n):
        if m_pointer < m and n_pointer < n:
            if nums1[m_pointer] < nums2[n_pointer]:
                ranking[rank] = nums1[m_pointer]
                m_pointer += 1
            else:
                ranking[rank] = nums2[n_pointer]
                n_pointer += 1
                
        elif n_pointer < n:
            ranking[rank] = nums2[n_pointer]
            n_pointer += 1
        elif m_pointer < m:
            ranking[rank] = nums1[m_pointer]
            m_pointer += 1

    for index in range(m + n):
        nums1[index] = ranking[index]

