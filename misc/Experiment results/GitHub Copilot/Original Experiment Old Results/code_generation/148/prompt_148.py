
def bf(planet1, planet2):
    '''
    There are eight planets in our solar system: the closerst to the Sun 
    is Mercury, the next one is Venus, then Earth, Mars, Jupiter, Saturn, 
    Uranus, Neptune.
    Write a function that takes two planet names as strings planet1 and planet2. 
    The function should return a tuple containing all planets whose orbits are 
    located between the orbit of planet1 and the orbit of planet2, sorted by 
    the proximity to the sun. 
    The function should return an empty tuple if planet1 or planet2
    are not correct planet names. 
    Examples
    bf("Jupiter", "Neptune") ==> ("Saturn", "Uranus")
    bf("Earth", "Mercury") ==> ("Venus")
    bf("Mercury", "Uranus") ==> ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    '''
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if planet1 not in planets or planet2 not in planets:
        return ()
    else:
        planets_between = []
        for planet in planets:
            if planet1 == planet:
                planet1_index = planets.index(planet)
            if planet2 == planet:
                planet2_index = planets.index(planet)
        if planet1_index > planet2_index:
            for planet in planets[planet2_index:planet1_index+1]:
                planets_between.append(planet)
        elif planet1_index < planet2_index:
            for planet in planets[planet1_index:planet2_index+1]:
                planets_between.append(planet)
        else:
            return ()
        return tuple(planets_between)

        





