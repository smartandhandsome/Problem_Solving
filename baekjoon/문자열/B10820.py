while True:
    try:
        st = input()
        space = 0
        upper = 0
        lower = 0
        number = 0
        for s in st:
            if s == ' ':
                space += 1
            elif s.isupper():
                upper += 1
            elif s.islower():
                lower += 1
            elif s.isdigit():
                number += 1
        print(lower, upper, number, space)
    except EOFError:
        break
