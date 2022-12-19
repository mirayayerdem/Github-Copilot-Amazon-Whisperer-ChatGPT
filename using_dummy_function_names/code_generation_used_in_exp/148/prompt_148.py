
def foo(planet1, planet2):
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
    foo("Jupiter", "Neptune") ==> ("Saturn", "Uranus")
    foo("Earth", "Mercury") ==> ("Venus")
    foo("Mercury", "Uranus") ==> ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    '''
    planets = {
        'Mercury': 0,
        'Venus': 1,
        'Earth': 2,
        'Mars': 3,
        'Jupiter': 4,
        'Saturn': 5,
        'Uranus': 6,
        'Neptune': 7
    }
    if planet1 not in planets or planet2 not in planets:
        return ()
    else:
        return tuple(sorted(planets.keys(), key=lambda x: planets[x]))[planets[planet1]:planets[planet2]+1]
