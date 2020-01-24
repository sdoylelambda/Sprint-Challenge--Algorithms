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
        if len(word) <= 1:
            return 0
        elif word[0] == 't' and word[1] == 'h':
            word = word[2:]
            print('+1')
            return 1 + count_th(word)
        else:
            word = word[1:]
            return count_th(word)

    return th_count
