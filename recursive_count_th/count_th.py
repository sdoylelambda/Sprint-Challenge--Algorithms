'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # UPER
    # U - UNDERSTAND
    # Take in a single parameter (a string `word`)
    # return(INT) occurences of ***"th"*** occur within `word`.
    th = 'th'
    th_count = 0
    # Case matters
    # NO LOOPS -- USE WHILE
    looper = True
    # P - PLAN
    while looper:
        # if looper has th add 1 to th_count
        # and remove it from the string and keep going

        if len(word) < 1:
            return th_count

        # left = word[: len(word) // 2]
        # print('left:', left)
        # right = word[len(word) // 2:]
        # print('right:', right)
        # # Sort the left
        # left = count_th(left)
        # print('left2ndtime:', left)
        # # Sort the right
        # right = count_th(right)
        # print('right2ndtime:', right)
        # # Merge together
        # return merge(left, right)

    return th_count
