def xo(s):
    """Check to see if a string has the same amount of 'x's and 'o's.
        The method must return a boolean and be case insensitive.
        The string can contains any char.

        Examples input/output:

        XO("ooxx") => true
        XO("xooxx") => false
        XO("ooxXm") => true
        XO("zpzpzpp") => true // when no 'x' and 'o' is present
        should return true
        XO("zzoo") => false
    """
    no_of_x = 0
    no_of_o = 0
    for symbol in s:
        if symbol == 'x':  # don't use "is" pto compare two different objects
            no_of_x += 1
        elif symbol == 'o':
            no_of_o += 1

    if no_of_o == no_of_x:
        return True
    else:
        return False
