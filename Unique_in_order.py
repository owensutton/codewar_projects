def unique_in_order(iterable):
    itlen = len(iterable)
    x = 0
    y = ''
    z = []

    while x < itlen:
        if iterable[x] == y:
            y = iterable[x]
            x += 1
        else:
            z.append(iterable[x])
            y = iterable[x]
            x += 1

    return(z)


unique_in_order("hello")
