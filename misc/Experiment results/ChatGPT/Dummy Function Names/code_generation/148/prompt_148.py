
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
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    planet1_index = planets.index(planet1) if planet1 in planets else -1
    planet2_index = planets.index(planet2) if planet2 in planets else -1
    if planet1_index == -1 or planet2_index == -1:
        return tuple()
    start = min(planet1_index, planet2_index)
    end = max(planet1_index, planet2_index)
    return tuple(planets[i] for i in range(start+1, end))
