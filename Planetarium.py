from Planet import Planet

class Planetarium(object):
    
    def __init__(self):
        self.create()

    def __str__(self):
        return '[' + ', '.join(str(planet) for planet in self.planets) + ']'

