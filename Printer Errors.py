def printer_error(s):
    y = 0
    z = 0


    for x in s:
        a = ord(s[z])

        if a > 109:
            y += 1
            z += 1
        else:
            z += 1


    return (str(y) + "/" + str(z))



printer_error("aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz")