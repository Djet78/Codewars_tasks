def array_diff(arr, dif_arr):
    """
    Your goal in this kata is to implement a difference function, which subtracts one list from another and
    returns the result.

    It should remove all values from list a, which are present in list b.

    array_diff([1,2],[1]) == [2]
    If a value is present in b, all of its occurrences must be removed from the other:

    array_diff([1,2,2,2,3],[2]) == [1,3]
    """
    if not arr or not dif_arr:
        return arr
    dif_arr = set(dif_arr)
    new_arr = []
    for elem in arr:
        if elem not in dif_arr:
            new_arr.append(elem)
    return new_arr


# ---------- Codewars --------------
def array_diff2(a, b):
    set_b = set(b)
    return [i for i in a if i not in set_b]
