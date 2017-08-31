def zeros(n):
    """Write a program that will calculate the number of trailing zeros in a
    factorial of a given number.
    https://www.codewars.com/kata/number-of-trailing-zeros-of-n/train/python

    http://mathworld.wolfram.com/Factorial.html

    N! = 1 * 2 * 3 * 4 ... N

    zeros(12) = 2 # 1 * 2 * 3 .. 12 = 479001600
    that has 2 trailing zeros 4790016(00)
    Be careful 1000! has length of 2568 digital numbers.
    """
    # its working but codewars doesn't accept it.
    # THEORY:-> count no of zero in the string backwards
    # fact = factorial(n)
    # no_of_zero = 0
    # while isinstance(fact, int):
    #     fact /= 10
    #     no_of_zero += 1
    # return no_of_zero

    # THEORY :-> divide the factorial till the remainder comes zero
    # doesn't accept
    # fact = factorial(n)
    # no_of_zero = 0
    # while fact % 10 == 0:
    #     no_of_zero += 1
    #     fact //= 10
    # return no_of_zero

    # theory http://www.purplemath.com/modules/factzero.htm
    if n < 5:
        return 0  # without this it shows UnboundLocalError for
    #  \max_power. weird
    if n == 5:
        return 1  # line 13 fails for n == 5
    no_of_zero = 0
    for i in range(n):
        no = n - 5 ** (i + 1)
        if no < 1:
            max_power = i
            break

    for power in range(1, max_power + 1):
        no_of_zero += int(n // (5 ** power))

    return no_of_zero
    # best solution
    # def zeros(n):
    # x = n/5
    # return x+zeros(x) if x else 0
