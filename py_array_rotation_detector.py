
def array_rotation_detector(arr1: list, arr2: list) -> bool:
    if arr1 == [] and arr2 == []:
        return True
 
    if len(arr1) != len(arr2):
        return False

    n = len(arr1)
    double = arr1 + arr1

    for i in range(n):
        if double[i:i + n] == arr2:
            return True
    return False

# TESTS
# cmp = [True, True, True, False, False, True]
# out = []
# out.append(array_rotation_detector([],[]))
# out.append(array_rotation_detector([1, 2, 3, 4, 5], [4, 5, 1, 2, 3]))
# out.append(array_rotation_detector([1, 2, 3, 4, 5], [5, 1, 2, 3, 4]))
# out.append(array_rotation_detector([1, 2, 3], [3, 2, 1]))
# out.append(array_rotation_detector([1, 2], [1, 2, 3]))
# out.append(array_rotation_detector([], []))

# if (out == cmp):
#     print("All tests passed sucessfully")
