# Mapped List Average

## Introduction

In Python, we can use the `map()` function to apply a function to each element of a list and return a new list with the modified elements. We can also use the `sum()` function to add up all the elements of a list. In this challenge, we will combine these two functions to calculate the average of a list, after mapping each element to a value using a provided function.

## Problem

Write a function called `average_by(lst, fn = lambda x: x)` that takes a list `lst` and a function `fn` as arguments. The function `fn` should be used to map each element of the list to a value. The function should then calculate the average of the mapped values and return it.

If the `fn` argument is not provided, the function should use the default identity function, which simply returns the element itself.

Your function should meet the following requirements:

- Use `map()` to map each element to the value returned by `fn`.
- Use `sum()` to sum all of the mapped values, divide by `len(lst)`.
- Omit the last argument, `fn`, to use the default identity function.

Function signature: `def average_by(lst, fn = lambda x: x) -> float:`

## Example

```py
assert average_by([1, 2, 3, 4, 5]) == 3.0
assert average_by([1, 2, 3, 4, 5], lambda x: x**2) == 11.0
assert average_by([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], lambda x: x['n']) == 5.0
```

## Summary

In this challenge, we learned how to use the `map()` and `sum()` functions to calculate the average of a list, after mapping each element to a value using a provided function. We also learned how to use default arguments in Python functions.