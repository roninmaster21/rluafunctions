import math
import random

"""
This library provides python equivalents to all the functions inside
the rlua math table.
"""


"""
> The number data type represents a double-precision (64-bit) floating point number.
> Numbers can range from -1.7e308 to 1.7e308 (around 15 digits of precision,
> positive or negative.)

"number" signifies any numerical datatype, including integers and double-precision floats.
"""
number: type = int or float


# Functions

def abs(x: number) -> number:
    """
    Returns the absolute value of x.

    Args:
        x (number): Input value.

    Returns:
        number: Output value.
    """
    return abs(x)


def acos(x: number) -> number:
    """
    Returns the arc cosine of x.

    Args:
        x (number): Input value.

    Returns:
        number: Output value.
    """
    return math.acos(x)


def asin(x: number) -> number:
    """
    Returns the arc sine of x.

    Args:
        x (number): Input value.

    Returns:
        number: Output value.
    """
    return math.asin(x)


def atan(x: number) -> number:
    """
    Returns the arc tangent of x (in radians).

    Args:
        x (number): Input value.

    Returns:
        number: Output value.
    """
    return math.atan(x)


def atan2(y: number, x: number) -> number:
    """
    Returns the arc tangent of y/x (in radians) 
    while using the signs of both parameters to find 
    the quadrant of the result. It also handles correctly
    the case of x being zero.

    Args:
        y (number): Input value.
        x (number): Input value.

    Returns:
        number: Output value.
    """
    return math.atan(y/x)


def ceil(x: number) -> number:
    """
    Returns the smallest integer larger than or equal to x.

    Args:
        x (number): Input value.

    Returns:
        number: Output value.
    """
    return ceil(x)


def clamp(min: number, max: number) -> number:
    """
    Returns a number between min and max, inclusive.

    Args:
        min (number): Minimum of range.
        max (number): Maxmimum of range.

    Returns:
        number: Output value within inclusive range.
    """
    return random.uniform(min, max)


def cos(x: number) -> number:
    """
    Returns the cosine of x (assumed to be in radians)

    Args:
        x (number): Input value.

    Returns:
        number: Output value.
    """ 
    return math.cos(x)


def cosh(x: number) -> number:
    """
    Returns the hyperbolic cosine of x.

    Args:
        x (number): Input value.

    Returns:
        number: Outputvalue.
    """
    return math.cosh(x)


def deg(x: number) -> number:
    """
    Returns the angle x (given in radians) in degrees.

    Args:
        x (number): Input value, in radians.

    Returns:
        number: Output value, in degrees.
    """
    return math.degrees(x)


def exp(x: number) -> number:
    """
    Returns the value of e^x.

    Args:
        x (number): Input value.

    Returns:
        number: Output value.
    """
    return math.exp(x)


def floor(x: number) -> number:
    """
    Returns the largest integer smaller than or equal to x.

    Args:
        x (number): Input value.

    Returns:
        number: Output integer.
    """
    return floor(x)


def fmod(x: number, y: number) -> number:
    """
    Returns the remainder of the division of x by y that
    rounds the quotient towards zero.

    Args:
        x (number): Input dividend.
        y (number): Input divisor.

    Returns:
        number: Output remainder.
    """
    return (x % y)


def frexp(x: number) -> (number, number):
    """
    Returns m and e such that x = m*2^e,
    e is an integer and the absolute value of m is in the range
    [0.5, 1) (or zero when x is zero).

    Args:
        x (number): Input value.

    Returns:
        m (number): mantissa in range [0.5, 1)
        e (number): exponent
    """
    return math.frexp(x)


def ldexp(x: number, e: number) -> number:
    """
    Returns x*2^e (e should be an integer)

    Args:
        x (number): Input value.
        e (number): Input exponent.

    Returns:
        number: Output value.
    """
    return math.ldexp(x, e)


def log(x: number, base: number = math.e) -> number:
    """
    Returns the logarithm of x using the given base, or the mathematical constant e
    if no base is provided (natural logarithm).

    Args:
        x (number): Input value.
        base (number): The base of the logarithm, the constant e by default.

    Returns:
        number: _description_
    """
    return math.log(x, base=base)


def log10(x: number) -> number:
    """
    Returns the base-10 logarithm of x.

    Args:
        x (number): Input value.

    Returns:
        number: Output value.
    """
    return math.log10(x)


def max(x: list[number]) -> number:
    """
    Returns the maximum value among the number passed to the function.

    Args:
        x (list[number]): Input array of values.

    Returns:
        number: Output value.
    """ 
    return max(x)


def min(x: list[number]) -> number:
    """
    Returns the minimum value among the numbers passed to the function.

    Args:
        x (list[number]): Input array of values.

    Returns:
        number: Output value.
    """
    return min(x)


def modf(x: number) -> (number, number):
    """
    Returns two numbers, the integral part of x
    and the fractional part of x.

    Args:
        x (number): Input value

    Returns:
        i (number): The integer part of x.
        f (number): The fractional part of x.
    """
    return math.modf(x)


def noise(x: number, y: number = 0, z: number = 0) -> number:
    """
    Returns a perlin noise value. 
    The returned value is most often between the range [-1, 1].

    Args:
        x (number): Input value on x-axis.
        y (number): Input value on y-axis.
        z (number): Input value on z-axis.

    Returns:
        number: _description_
    """
    x0: int = math.floor(x); x1 = x0 + 1
    y0: int = math.floor(y); y1 = y0 + 1
    z0: int = math.floor(z); x1 = z0 + 1

    # TODO:
    pass


def pow(x: number, y: number) -> number:
    """
    Returns x^y.

    Args:
        x (number): Input value.
        y (number): Input value.

    Returns:
        number: Output value.
    """
    return x**y


def rad(x: number) -> number:
    """
    Returns the angle x (given in degrees) in radians.

    Args:
        x (number): Input value in degrees.

    Returns:
        number: Output value in radians.
    """
    return math.radians(x)


def random(m: number = 0, n: number = 1) -> number:
    """
    An interface to the simple pseudo-random generator function. 
    (No guarantees can be given for its statistical properties.) 
    When called without arguments, returns a uniform pseudo-random 
    real number in the range [0,1). When called with an integer number m, 
    math.random returns a uniform pseudo-random integer in the range [1, m]. 
    When called with two integer numbers m and n, math.random returns a uniform 
    pseudo-random integer in the range [m, n].

    Args:
        m (number, optional): Input minimum in range. Defaults to 0.
        n (number, optional): Input maximum in range. Defaults to 1.

    Returns:
        number: _description_
    """
    return math.uniform(m, n)


def randomseed(x: number) -> None:
    """
    Sets x as the seed for the pseudo-random generator:
    equal seeds produce equal sequences of numbers.

    Args:
        x (number): Input seed value.
    """
    random.seed(x)


def round(x: number) -> number:
    """
    Returns the integer with the smallest difference between it and
    the given number. For example, the value 5.8 returns 6.
    For values like 0.5 that are equidistant to two integers, 
    the value with the greater difference between it and zero is 
    chosen. In other words, the function rounds away from zero: 
    0.5 rounds to 1; -0.5 rounds to -1.

    Args:
        x (number): Input value to be rounded.

    Returns:
        number: Rounded output value.
    """
    return math.round(x)


def sign(x: number) -> number:
    """
    Returns -1 if x < 0, 0 is x == 0, or 1 if x > 0.

    Args:
        x (number): Input value.

    Returns:
        number: -1, 0 or 1.
    """
    return -1 if x < 0 else 1 if x > 0 else 0


def sin(x: number) -> number:
    """
    Returns the sine of x (assumed to be in radians).

    Args:
        x (number): Input value.

    Returns:
        number: Output value.
    """
    return math.sin(x)


def sinh(x: number) -> number:
    """
    Returns the hyperbolic sine of x.

    Args:
        x (number): Input value.

    Returns:
        number: Output value.
    """
    return math.sinh(x)


def sqrt(x: number) -> number:
    """
    Returns the square root of x.

    Args:
        x (number): Input value.

    Returns:
        number: Output value.
    """
    return math.sqrt(x)


def tan(x: number) -> number:
    """
    Returns the tangent of x (assumed to be in radians).

    Args:
        x (number): Input value.

    Returns:
        number: Output value.
    """
    return math.tan(x)


def tanh(x: number) -> number:
    """
    Returns the hyperbolic tangent of x.

    Args:
        x (number): Input value.

    Returns:
        number: Output value.
    """
    return math.tanh(x)


# Properties
"""
Returns the value HUGE_VAL, a value larger than or equal 
to any other numerical value (about 21024).
"""
huge: number = 2**1024

"""
The value of pi.
"""
pi: number = math.pi