# Description:

# Given a variable n,
# If n is an integer, Return a string with dash'-'marks before and after each odd integer, but do not begin or end the
# string with a dash mark. If n is negative, then the negative sign should be removed.
# If n is not an integer, return the string "None".

def dashatize(n):
    if not isinstance(n, int):
        return 'None'
    n = str(abs(n))
    str_n = ''
    for i in range(len(n)):
        if int(n[i]) % 2 and i == 0:
            str_n += f'{n[i]}-'
        elif int(n[i]) % 2 and int(n[i - 1]) % 2:
            str_n += f'{n[i]}-'
        elif int(n[i]) % 2:
            str_n += f'-{n[i]}-'
        else:
            str_n += n[i]
    return str_n.strip('-')
