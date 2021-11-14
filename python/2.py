def binary_search(list_of_nums, item):
    low = 0
    high = len(list_of_nums) - 1
    while low <= high:
        mid = int((high + low)/2)
        guess = list_of_nums[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None
    
    
def find_two_indexies(nums, target):
    nums.sort()
    
    for i in range(0, len(nums)-1):
        opposite = target - nums[i]
        opposite_id = binary_search(nums, opposite)
        
        if opposite_id is not None:
            if opposite_id == i:
                if num[opposite_id - 1] == opposite:
                    return [i, opposite_id - 1]
                elif num[opposite_id + 1] == opposite:
                    return [i, opposite_id + 1]
            else:
                return [i, opposite_id]
        
    return []