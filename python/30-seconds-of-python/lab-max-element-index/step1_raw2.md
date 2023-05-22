# Index of Max Element

## Introduction

In this challenge, you will create a function that takes a list of numbers as an argument and returns the index of the element with the maximum value.

## Problem

Write a function `max_element_index(arr)` that takes a list `arr` as an argument and returns the index of the element with the maximum value. If there are multiple elements with the maximum value, return the index of the first occurrence.

To solve this problem, you can follow these steps:

1. Use the built-in `max()` function to find the maximum value in the list.
2. Use the built-in `list.index()` function to find the index of the first occurrence of the maximum value in the list.
3. Return the index.

## Example

```python
max_element_index([5, 8, 9, 7, 10, 3, 0]) # 4
```

In this example, the maximum value in the list `[5, 8, 9, 7, 10, 3, 0]` is `10`, which occurs at index `4`. Therefore, the function should return `4`.

## Summary

In this challenge, you learned how to find the index of the element with the maximum value in a list. You used the built-in `max()` and `list.index()` functions to solve the problem.