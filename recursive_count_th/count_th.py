'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
# length of the word is the th
# return how many times th occurs in the word.


def count_th(word):
    if len(word) == 0 or len(word) < 2:
        return 0

    elif word[0:2] == "th":
        return count_th(word[1::]) + 1
    else:
        return count_th(word[1::])
