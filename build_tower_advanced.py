def tower_builder(n_floors, block_size):
    """
    Build Tower by the following given arguments:
    number of floors (integer and always greater than 0)
    block size (width, height) (integer pair and always greater than (0, 0))

    Tower block unit is represented as *

    Python: return a list;
    JavaScript: returns an Array;
    Have fun!

    for example, a tower of 3 floors with block size = (2, 3) looks like below

    [
      ['    **    '],
      ['    **    '],
      ['    **    '],
      ['  ******  '],
      ['  ******  '],
      ['  ******  '],
      ['**********'],
      ['**********'],
      ['**********']
    ]
    and a tower of 6 floors with block size = (2, 1) looks like below

    [
      '          **          ',
      '        ******        ',
      '      **********      ',
      '    **************    ',
      '  ******************  ',
      '**********************'
    ]
    """
    w, h = block_size
    total = w
    result = list()
    block_width_per_floor = w
    for _ in range(n_floors - 1):
        total += 2 * w

    for _ in range(n_floors):
        for _ in range(h):
            result.append(("*" * block_width_per_floor).center(total))
        block_width_per_floor += w * 2

    return result
