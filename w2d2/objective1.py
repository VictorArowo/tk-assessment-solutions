def bin_search(arr, item, left, right):
    if right < left:
        return False
    mid = left + (right - left) // 2
    curr = arr[mid]
    if curr == item:
        print(arr.index(curr))
        return True
    elif item < curr:
        return bin_search(arr, item, left, mid - 1)
    else:
        return bin_search(arr, item, mid + 1, right)


print(bin_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 5, 0, 8))


# Base Case
# In normal operation, the value of the left variable which starts of as 0 should always be less than the value of the right variable which starts off as the index of the last element in the array.
# Thus, a good base case exists when right > left. At that point we have gone throigh the array, and couldn't find the element

# How should our recursive solution converge on our base case(s)?
# After each run of the recursive function the difference between the left value and the right value is halved, thus with each run we approach the base case
