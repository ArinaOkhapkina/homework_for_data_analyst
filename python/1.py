def recursion_for_find(nums, n, target, used_indexies):
    if target == 0:
        return used_indexies
    if n == 0:
        return []

    if nums[n-1] > target:
        return recursion_for_find(nums, n-1, target, used_indexies)
    
    variant_1 = recursion_for_find(nums, n-1, target, used_indexies)
    if(len(variant_1) != 0):
        return variant_1

    variant_2 = recursion_for_find(nums, n-1, target - nums[n-1], used_indexies + [n-1])
    if(len(variant_2) != 0):
        return variant_2
        
    return []
        
        
def find_indexies(nums, target):
    n = len(nums)
    used_indexies = []     
    return recursion_for_find(nums,n, target, used_indexies)