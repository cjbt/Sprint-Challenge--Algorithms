'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    if len(word) == 0:
        return 0
    if len(word) == 1:
        return 0
    word_list = [*word]
    word_length = len(word) - 1
    count = 0
    def recurse(arr, n):
        nonlocal count
        if n < 0:
            return
        if arr[n - 1] == "t" and arr[n] == "h":
            count += 1
        return recurse(arr, n - 1)
    recurse(word_list, word_length)
    return count
