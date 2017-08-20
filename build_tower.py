def tower_builder(n_floors):
    """Build Tower

    Build Tower by the following given argument:
    number of floors (integer and always greater than 0).

    Tower block is represented as *

    Python: return a list;
    JavaScript: returns an Array;
    C#: returns a string[];
    PHP: returns an array;
    C++: returns a vector<string>;
    Haskell: returns a [String];

    for example, a tower of 3 floors looks like below

    [
      '  *  ',
      ' *** ',
      '*****'
    ]
    and a tower of 6 floors looks like below

    [
      '     *     ',
      '    ***    ',
      '   *****   ',
      '  *******  ',
      ' ********* ',
      '***********'
    ]
    """
    asterisks = list([1, ])
    spaces = list(range(n_floors))
    spaces.reverse()
    result = list()
    for _ in range(n_floors - 1):
        asterisks.append(asterisks[-1] + 2)

    for i in range(n_floors):
        result.append(str(spaces[i] * " " + asterisks[i] * "*" + spaces[i] * " "))

    return result
    # and guess what it works
    # outstanding
"""other solution s
    return [("*" * (i*2-1)).center(n*2-1) for i in range(1, n+1)]
    # remember the center attribute
    return [" " * (n - i - 1) + "*" * (2*i + 1) + " " * (n - i - 1) for i in range(n)]
"""
    total = w
    result = list()
    for _ in range(n - 1):
        total += 2 * w

    for _ in range(n):
        for _ in range(h):
            result.append(("*" * w).center(total))
        w = w + w * 2

    return result
