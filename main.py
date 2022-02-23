'''
    A project that allows you to approximate cos(3x)^2 using Teylor series.
'''
import math
import matplotlib.pyplot as plt
import numpy as np


def approximate_value(arg: float, terms_count: int = 50) -> float:
    """
        A function that computes the value of cos(3x)^2
        using Teylor series.
    Args:
        arg (float): an angle (given in radians).
        terms_count (int): a count of terms in Teylor series. Defaults to 50.
        is_radians (bool): True if argument is given in radians
        and False otherwise.
    Returns:
        float: a value cos(3*arg)^2
    Example:
        >>> approximate_value(99 * math.pi/3, 50)
        1.0000000000004259
    """
    result = 0
    arg %= 2 * math.pi
    arg *= 3
    for num in range(0, terms_count, 2):
        result += ((-1)**(num/2)) * (arg ** num) / math.factorial(num)
    return result ** 2


def value_difference(arg: float, terms_count=50):
    """
    A function that returns difference between approximate value of cos(3*arg)^2
    and a true value of it.
    Args:
        arg (float): an angle (given in radians).
        terms_count (int, optional): a count of terms in Teylor series. Defaults to 50.
    Returns:
        float: a difference.
    Example:
        >>> value_difference(math.pi/100)
        2.220446049250313e-16
    """
    return abs(approximate_value(arg, terms_count) - math.cos(3*arg)**2)


def plot_graph_difference(terms_count=50):
    """
        Draws a curve of a true cos(3x)^2 and it's approximation. Returns nothing.
    Args:
        terms_count (int, optional): a count of terms in Teylor series. Defaults to 50.
    """
    arguments = np.linspace(-np.pi*10, np.pi*10, 1000)
    values = np.cos(3 * arguments) ** 2
    appr = [approximate_value(point, terms_count) for point in arguments]

    fig = plt.figure()
    axes = fig.add_subplot(1, 1, 1)
    axes.spines['left'].set_position('center')
    axes.spines['bottom'].set_position('center')
    axes.spines['right'].set_color('none')
    axes.spines['top'].set_color('none')
    axes.xaxis.set_ticks_position('bottom')
    axes.yaxis.set_ticks_position('left')

    axes.plot((1), (0), ls="", marker=">", ms=10, color="k",
            transform=axes.get_yaxis_transform(), clip_on=False)
    axes.plot((0), (1), ls="", marker="^", ms=10, color="k",
            transform=axes.get_xaxis_transform(), clip_on=False)

    plt.axis([-30, 30, -10, 10])
    plt.plot(arguments, values, 'b')
    plt.plot(arguments, appr, 'r')

    plt.show()


def epsilon_terms_count(args: list, epsilon: float = 10**(-9))->int:
    """
    Returns a count of terms of a series needed to minimize difference between
    a true value and approximate one.
    Args:
        args (list): a list of points, to which we will approximate our function.
        epsilon (float, optional): a desired difference. Defaults to 10**(-9).
    Returns:
        int: a count of terms.
    Examples:
        >>> epsilon_terms_count([45, 80])
        53
    """
    terms_count = 1
    for arg in args:
        while value_difference(arg, terms_count) >= epsilon:
            terms_count += 1
    return terms_count


def main():
    print('Enter an angle:')
    while True:
        try:
            arg = float(input('>>> '))
            break
        except ValueError:
            print('Pls, enter the correct value.')
            continue

    print('Enter the number of terms:')
    while True:
        try:
            terms_count = int(input('>>> '))
            break
        except ValueError:
            print('Pls, enter the correct value.')
            continue
    
    print(f'The approximate value of a function is {approximate_value(arg, terms_count)}')
    print(f'The difference between my function and built-in function is {value_difference(arg, terms_count)}')
    print(f'A number of terms needed to minimize a difference between a true value and approximate one to')
    print(f'epsilon=10^(-1): {epsilon_terms_count([arg], 10**(-1))}')
    print(f'epsilon=10^(-2): {epsilon_terms_count([arg], 10**(-2))}')
    print(f'epsilon=10^(-6): {epsilon_terms_count([arg], 10**(-6))}')
    print(f'epsilon=10^(-9): {epsilon_terms_count([arg], 10**(-9))}')
    print('Plotting...')
    plot_graph_difference(terms_count)

if __name__ == '__main__':
    main()
