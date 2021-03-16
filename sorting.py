#!/bin/python3
'''
Python provides built-in sort/sorted
functions that use timsort internally.
You cannot use these built-in functions
anywhere in this file.
Every function in this file takes a comparator `cmp` as input
which controls how the elements of the list
should be compared against each other:
If cmp(a, b) returns -1, then a < b;
if cmp(a, b) returns  1, then a > b;
if cmp(a, b) returns  0, then a == b.
'''

import random


def cmp_standard(a, b):
    '''
    used for sorting from lowest to highest

    >>> cmp_standard(125, 322)
    -1
    >>> cmp_standard(523, 322)
    1
    '''
    if a < b:
        return -1
    if b < a:
        return 1
    return 0


def cmp_reverse(a, b):
    '''
    used for sorting from highest to lowest
    >>> cmp_reverse(125, 322)
    1
    >>> cmp_reverse(523, 322)
    -1
    '''
    if a < b:
        return 1
    if b < a:
        return -1
    return 0


def cmp_last_digit(a, b):
    '''
    used for sorting based on the last digit only

    >>> cmp_last_digit(125, 322)
    1
    >>> cmp_last_digit(523, 322)
    1
    '''
    return cmp_standard(a % 10, b % 10)


def _merged(xs, ys, cmp=cmp_standard):
    '''
    Assumes that both xs and ys are sorted,
    and returns a new list containing the elements of both xs and ys.
    Runs in linear time.
    NOTE:
    In python, helper functions are frequently prepended with the _.
    This is a signal to users of a library
    that these functions are for "internal use only",
    and not part of the "public interface".
    This _merged function could be implemented
    as a local function within the merge_sorted
    scope rather than a global function.
    (like the go functions from binary search).
    If it's possible to make a function stand-alone,

    >>> _merged([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    '''
    xs_lo = 0
    ys_lo = 0
    results = []
    while xs_lo < len(xs) and ys_lo < len(ys):
        if cmp(xs[xs_lo], ys[ys_lo]) == -1:
            results.append(xs[xs_lo])
            xs_lo += 1
            continue
        if cmp(xs[xs_lo], ys[ys_lo]) == 1:
            results.append(ys[ys_lo])
            ys_lo += 1
            continue
        if cmp(xs[xs_lo], ys[ys_lo]) == 0:
            # results.append(xs[xs_lo] + ys[ys_lo])
            results.append(xs[xs_lo])
            results.append(ys[ys_lo])
            xs_lo += 1
            ys_lo += 1
            continue
    while xs_lo < len(xs):
        results.append(xs[xs_lo])
        xs_lo += 1
    while ys_lo < len(ys):
        results.append(ys[ys_lo])
        ys_lo += 1
    return results


def merge_sorted(xs, cmp=cmp_standard):
    '''
    Merge sort is the standard O(n log n) sorting algorithm.
    Recall that the merge sort pseudo code is:
        if xs has 1 element
            it is sorted, so return xs
        else
            divide the list into two halves left,right
            sort the left
            sort the right
            merge the two sorted halves
    You should return a sorted version of the input list xs.
    You should not modify the input list xs in any way.
    '''
    if len(xs) == 1:
        return xs
    if xs == []:
        return xs
    mid = len(xs) // 2
    lefts = xs[:mid]
    rights = xs[mid:]
    lefts_sort = merge_sorted(lefts, cmp)
    rights_sort = merge_sorted(rights, cmp)
    return _merged(lefts_sort, rights_sort, cmp)


def quick_sorted(xs, cmp=cmp_standard):
    '''
    Quicksort is like mergesort,
    but it uses a different strategy to split the list.
    Instead of splitting the list down the middle,
    a "pivot" value is randomly selected,
    The pseudocode is:
        if xs has 1 element
            it is sorted, so return xs
        else
            select a pivot value p
            put all the values less than p in a list
            put all the values greater than p in a list
            put all the values equal to p in a list
            sort the greater/less than lists recursively
            return the concatenation of (less than, equal, greater than)
    You should return a sorted version of the input list xs.
    You should not modify the input list xs in any way.
    '''
    xs1 = xs
    less_than = []
    greater_than = []
    equal_to = []
    if len(xs) == 1:
        return xs
    if xs == []:
        return xs
    else:
        # p = random.choices(xs)
        p = random.randint(0, len(xs) - 1)
        for i in range(len(xs1)):
            if cmp(xs1[i], xs[p]) == -1:
                less_than.append(xs[i])
                continue
            if cmp(xs1[i], xs[p]) == 1:
                greater_than.append(xs[i])
                continue
            else:
                equal_to.append(xs[i])
                continue
        sort_less = merge_sorted(less_than, cmp)
        sort_greater = merge_sorted(greater_than, cmp)
    return sort_less + equal_to + sort_greater


def quick_sort(xs, cmp=cmp_standard):
    '''
    EXTRA CREDIT:
    '''
