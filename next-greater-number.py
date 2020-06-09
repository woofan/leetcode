def nextGreaterElement( nums1, nums2) :
    res = [-1] * len(nums1)
    for i in range(len(nums1)):
        for j in range(nums2.index(nums1[i]),len(nums2)):
            if nums2[j] > nums1[i]:
                res[i] = nums2[j]
                break
        if j == len(nums2):
            res[i] = -1
    return res


print(nextGreaterElement([4,1,2],[1,3,4,2]))