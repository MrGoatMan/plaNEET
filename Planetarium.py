from Planet import Planet

class Planetarium(object):
    
    def __init__(self):
        self.create()

    def __str__(self):
        return '[' + ', '.join(str(planet) for planet in self.planets) + ']'
    
    def create(self):
        self.planets = []
        for i in range(4):
            for j in range(0,4):
                self.planets.append(Planet(i, j)
