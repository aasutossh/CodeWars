def binary_array_to_number(arr):
    """[summary]
    Given an array of one's and zero's convert the equivalent binary
    value to an integer.

    Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1

    Examples:

    Testing: [0, 0, 0, 1] ==> 1
    Testing: [0, 0, 1, 0] ==> 2
    Testing: [0, 1, 0, 1] ==> 5
    Testing: [1, 0, 0, 1] ==> 9
    Testing: [0, 0, 1, 0] ==> 2
    Testing: [0, 1, 1, 0] ==> 6
    Testing: [1, 1, 1, 1] ==> 15
    Testing: [1, 0, 1, 1] ==> 11
    """

    ######## MY OWN DOING #########
    # arr_len = len(arr)
    # decimal = 0
    # for bit in arr:
    #     print("bit = ", bit)
    #     arr_len -= 1
    #     if arr_len is (-1):
    #         break

    #     decimal += bit * (2 ** arr_len)

    # return decimal
    ###############################
    return int(''.join(str(a) for a in arr), 2)
