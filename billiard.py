"""u = int(input('uzunlikni kiriting u='))
h = int(input('balandlikni kiriting h='))


def bil(a, b, k=0, tom='↘️'):
"""
    if a - b == 0:
        res = 0
        if tom == '↖️':
            res = 1
        if tom == '↗️':
            res = 2
        if tom == '↘️':
            res = 3
        if tom == '↙️':
            res = 4
        return f"{k} {res}"

    elif a - b > 0:
        if tom == '↘️':
            tom = '↗️'
        elif tom == '↙️':
            tom = '↖️'
        elif tom == '↗️':
            tom = '↘️'
        elif tom == '↖️':
            tom = '↙️'
        return bil(a - b, h, k + 1, tom)

    elif a - b < 0:
        if tom == '↘️':
            tom = '↙️'
        elif tom == '↗️':
            tom = '↖️'
        elif tom == '↙️':
            tom = '↘️'
        elif tom == '↖️':
            tom = '↗️'
        return bil(u, b-a, k + 1, tom)


print(bil(u, h))
