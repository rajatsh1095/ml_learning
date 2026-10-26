def count_comparisons_linear_search(arr, target):
    """
    arr:    a list of numbers
    target: the value being searched for

    Returns:
        (found, comparisons): found is True if target is in arr, False
        otherwise. comparisons is the number of element-to-target
        comparisons actually performed (stop as soon as a match is
        found -- don't keep scanning).
    """
    # TODO: Implement a left-to-right linear scan, counting comparisons.
    count =0
    found = False
    for i in arr:
        count +=1
        if i == target:
            found = True
            return True, count        
    return False,count
    pass


def count_comparisons_binary_search(sorted_arr, target):
    """
    sorted_arr: a list of numbers, already sorted ascending
    target:     the value being searched for

    Returns:
        (found, comparisons): same shape as count_comparisons_linear_search,
        but using binary search -- each comparison must actually halve
        the remaining search space.
    """
    # TODO: Implement binary search from Theory, counting one
    # comparison per midpoint check.
    
    left = 0
    right = len(sorted_arr)
    count =0

    while(left<right):
        count+=1
        mid = (left+right)//2
        
        if target == sorted_arr[mid]:
            return True,count
        elif target > sorted_arr[mid]:
            left=mid+1 
        else:
            right = mid
    return False, count
    pass
