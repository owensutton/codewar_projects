def number(bus_stops):
    TotalOn = 0
    z = 0
    input = bus_stops

    for x in bus_stops:
        TotalOn = TotalOn + input[z][0]
        TotalOn = TotalOn - input[z][1]
        z += 1


    return(TotalOn)

number([[10,0],[3,5],[5,8]])