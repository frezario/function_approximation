**A project that allows you to approximate cos(3x)^2.**

It uses Taylor series to minimize the difference between the true value of the cos(3x)^2 and the approximate one.

To use this project you must have numpy and matplotlib installed.

main.py is the main module that performs all the magic. It contains 4 functions, namely:

1. ```approximate_value(arg: float, terms_count: int = 50)```

A function that computes the value of cos(3x)^2 using Teylor series.

It takes 2 parameters: the first one is an angle and the second is a count of terms of the Taylor series to be taken into account (by default it is 50).

To achieve better performance, I use periodic slicing (any number of 2 * pi will be sliced of the angle).

Then the function adds up passed count of the Taylor terms and returns a result.

The example of using:

```
>>> approximate_value(99 * math.pi/3, 50)
1.0000000000004259
```

2. ```value_difference(arg: float, terms_count=50)```

A function that returns an absolute difference between approximate value of cos(3*arg)^2 and a true value of it (by true value I mean a result of numpy.cos() function).

It takes 2 parameters: the first one is an angle and the second is a count of terms of the Taylor series to be taken into account.

The example of using:

```
>>> value_difference(math.pi/100)
2.220446049250313e-16
```

3. ```plot_graph_difference(terms_count=50)```

Draws a curve of a true cos(3x)^2 and it's approximation. Returns nothing.

Takes one parameter - a count of terms of the Taylor series to be taken into account.

Blue color represents 'true' value of the function and red represents approximate one.

Examples of using:

```
>>> plot_graph_difference()
```

![image](https://user-images.githubusercontent.com/91615650/154822076-e0d69796-f945-47fd-831a-ea129e349eac.png)

```
>>> plot_graph_difference(60)
```

![image](https://user-images.githubusercontent.com/91615650/154822106-7e3d10a9-0f8e-4906-ad5e-cd1ba1f0ce23.png)

As you can see, with value of 60, two graphs are almost indistinguishable.

4. ```epsilon_terms_count(args: list, epsilon: float = 10**(-9))```

Returns a count of terms of a series needed to minimize difference between a true value and approximate one.

rgs (list): a list of points, to which we will approximate our function.

epsilon (float): a desired difference. Defaults to 10**(-9).

More presicely, it returns a count of terms of a series needed for a difference between a true value and approximate one to reach the epsilon value.

The example of using:

```
>>> epsilon_terms_count([45, 80])
53
```
