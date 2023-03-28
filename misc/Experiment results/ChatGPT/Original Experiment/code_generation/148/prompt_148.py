def bf(planet1, planet2):
    planet_list = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if planet1 not in planet_list or planet2 not in planet_list:
        return ()
    start = planet_list.index(planet1)
    end = planet_list.index(planet2)
    if start > end:
        start, end = end, start
    return tuple(planet_list[i] for i in range(start, end+1))