# Removing duplicates from a list

list1 = [1, 2, 2, 3, 4, 5, 6,8,9,12,54,5,4,12,21,12,12,12]

# Method 1: Using sets(sets dont contain duplicates)

set1 = set(list1)
list2 = list(set1)
print(f"Method 1: {list2}")

# Method 2: Using user defined function

def remove_duplicates(arr):
    newarr = []
    for i in arr:
        if i not in newarr:
            newarr.append(i)
    return newarr

list3 = remove_duplicates(list1)
print(f"Method 2: {list3}")


# Thank You !!!
