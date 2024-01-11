#Implimintation a brute force algorithm to solve the problem
def findingDescending_order(arr):
    # length of the list
    n = len(arr)
    # Create an ordered array or list with one element and n length 
    orders = [0] * n
    # Looping every element in the list
    for l in range(n):
        # count the order to 1
        order = 1
        # nested loop goes through every element in the array
        for m in range(n):
            # If the current element (m) is larger than the element in the (l) loop, increment the order
            
            if arr[m] > arr[l]:
                order += 1
        # put the order of the current element(m) in the order list
        orders[l] = order
    # Return the order list
    return orders

# Test code
arr = [11, 13, 18, 15, 9, 4, 23]
print(findingDescending_order (arr))
