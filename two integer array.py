def calculate_indices(nums1,nums2):
    answer1=sum(1 for num in nums1 if num in nums2)
    answer2=sum(1 for num in nums2 if num in nums1)
    return [answer1, answer2]
nums1=[2,3,2]
nums2=[1,2]
print(calculate_indices(nums1,nums2))

