def find_nb(m):
    """Your task is to construct a building which will be a pile of n cubes. 
    The cube at the bottom will have a volume of n^3, 
    the cube above will have volume of (n-1)^3 and so on until 
    the top which will have a volume of 1^3.

    You are given the total volume m of the building. 
    Being given m can you find the number n of cubes you will have to build?

    The parameter of the function findNb (find_nb, find-nb, findNb) will 
    be an integer m and you have to return the integer n such as 
    n^3 + (n-1)^3 + ... + 1^3 = m if such a n exists or -1 if there is no such n.

    Examples:

    find_nb(1071225) --> 45
    find_nb(91716553919377) --> -1
    
    Arguments:
        m {type[int]} -- volume of whole building.
    """ 
    # create an endless loop
    n = 1
    while True:
        if m > 0:
            # if m, the total volume, is not 0, we will subtract the volume of the current cube from it
            # first calculate the volume of the current cube
            curr_cube_volume = (n) ** 3
            # subtract the current cube volume from the total volume
            m = m - curr_cube_volume

        elif m is 0:
            # if m is zero then we've found our n, so return n
            return n

        elif m < 0:
            # if we've gone below zero there is no such n!
            return -1

        n += 1
