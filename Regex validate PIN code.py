def validate_pin(pin):
    lenpin = len(pin)
    if lenpin == 4 or lenpin == 6:
        return (pin.isnumeric())
    else:
        return False


validate_pin('0000')
