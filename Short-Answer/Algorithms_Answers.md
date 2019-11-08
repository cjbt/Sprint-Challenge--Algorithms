#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) O(n^3) runtime complexity and O(1) space complexity

b) O(logn) runtime complexity and O(1) space complexity

c) O(n) runtime complexity and O(1) space complexity

## Exercise II

On a sorted number of floors, a binary search would work well here.
It has a runtime of `O(logn)`
pseudocode:

```
exercise_two(n_story_building)
    is_broken = False
    low = 0
    count = 0
    high = len(n_story_building) - 1
        while is_broken == False
            middle = (high + low)//2
            go to middle
            at middle if is_broken == True
                high = middle + -1
                count += 1
            at middle elif is_broken == False
                low = middle + 1
                count += 1
            if len(middle) === 1
                return
    return count

```
