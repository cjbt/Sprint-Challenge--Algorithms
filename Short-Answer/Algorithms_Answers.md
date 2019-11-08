#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) O(n^3) runtime complexity and O(1) space complexity since the amount that a has to loop is n times n times n. Although we are changing the produce of a depending on n \* n. it seems insignificant.

b) O(logn) runtime complexity and O(1) space complexity. Although it has two loops, the outer loop has a runtime of O(n) and the inner loop is only looping up until n and j is doubling itself each time which cuts the it in half.

c) O(n) runtime complexity and O(1) space complexity since the recursion is based on bunnies decreasing by on until it hits 0. Very linear.

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
