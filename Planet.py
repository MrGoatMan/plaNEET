class Planet(object):
    bodies = ['ringed', 'flat', 'gassy', 'terra']
    colors = ['orange', 'red', 'blue', 'blue-green', 'brown']

    def __init__(self, body, color):
        self.bodyIndex = body
        self.colorIndex = color

    def __str__(self):
        planet = Planet.bodies[self.bodyIndex]
        planet = Planet.colors[self.colorIndex]

        
    def __print__(self):
        return f"Planet: The shape is {body} and the color is {color}"
    
