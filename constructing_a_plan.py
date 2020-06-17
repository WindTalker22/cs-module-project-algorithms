"""
We'll say that a positive int divides itself
if every digit in the number divides into the
number evenly.

Example One:
So for example 128 divides itself
since 1, 2, and 8 all divide into 128 evenly.


Example Two:
64
This does not divide itself because 64 is not evenly divisible by 6

And we'll say that 0 does not divide into anything
evenly, so no number with a 0 digit divides itself.

Write a function to determine if a number divides itself.

[source - https://codingbat.com/prob/p165941]
"""
# Questions
# How big are the numbers we recieve as inputs?

# Assumptions
# The test has to work for all the numbers.
# Output will be a boolean (either true or false)


def divide_self(num):
    # if num is == to zero
    if num == 0:
        return False
    # if length of input is 1
    if len(str(num)) == 1:
        return True

    # split input into iterable collection of integers
    for digit in str(num):
        digit_int = int(digit)
    if digit_int == 0 or num % digit_int is not 0:
        return False

        return True


print(divide_self(0))
print(divide_self(1))
print(divide_self(10))
