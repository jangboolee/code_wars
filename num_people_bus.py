def number(bus_stops):
    
    current = 0
    for bus_stop in bus_stops:
        current += bus_stop[0]
        current -= bus_stop[1]
    
    return current
