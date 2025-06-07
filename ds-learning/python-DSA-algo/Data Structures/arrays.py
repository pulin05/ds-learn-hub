import array

# my_array = array.array('i') ## create empty arary ----  both time and space O(1)
# print((my_array))

my_array1 = array.array('i',[1,2,3,4]) ## ---- both time and space O(n), since elements are copied to empty array
# print((my_array1))

# import numpy as np
# np_array = np.array([], dtype=int) # empty array ---- both time and space O(1)
# print(np_array)
# np_array1 = np.array([1,2,3,4,5]) ## ## ----  both time and space O(n)
# print(np_array1)

## Insertion to Array
print((my_array1))
my_array1.insert(100,6)
print((my_array1))

## Traversal operation
