# Clamp Number Challenge

## Introduction

In programming, it is often necessary to limit a number to a certain range. This is where the concept of clamping comes in. Clamping a number means restricting it to a certain range of values. In this challenge, you will be tasked with creating a function that clamps a number within a specified range.

## Problem

Write a function `clamp_number(num, a, b)` that takes in three parameters:

- `num` (integer or float): the number to be clamped
- `a` (integer or float): the lower boundary of the range
- `b` (integer or float): the upper boundary of the range

The function should clamp `num` within the inclusive range specified by the boundary values. If `num` falls within the range (`a`, `b`), return `num`. Otherwise, return the nearest number in the range.

## Example

```py
clamp_number(2, 3, 5) # 3
clamp_number(1, -1, -5) # -1
clamp_number(10, 1, 5) # 5
clamp_number(-10, -5, -1) # -5
```

## Summary

In this challenge, you have learned how to clamp a number within a specified range. This is a useful technique in programming, especially when dealing with user input or data that needs to be restricted to a certain range. Keep practicing and honing your skills to become a better programmer!