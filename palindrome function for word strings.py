def is_palindrome(w):

    if not isinstance(w, str):
        return "ERROR: input is not a string."

    elif len(w) > 2:
        if w[0] == w[-1]:
            while len(w) > 2:
                w = w[1:-1]
                is_palindrome(w)

        if len(w) == 1:
            return True

        else:
            return False

    else:
        return "ERROR: input contains two or less characters."


print (is_palindrome('aibohphobia'))
print (is_palindrome('definitely'))
