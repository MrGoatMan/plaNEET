import random

from Planet import Planet

class Planetarium(object):
    
    def __init__(self):
        self.create()

    def __str__(self):
        return '[' + ', '.join(str(body) for planet in self.planets) + ']'
    
    def create(self):
        self.planets = []
        for i in range(4):
            for j in range(0,14):
                self.planets.append(Card(i, j))

    def sort(self):
        n = len(self.planets)
        for i in range(n): 
            pos = i 
            for j in range(i+1, n):
                a = self.planets[pos]
                b = self.planets[j]
                if (a.suitIndex > b.suitIndex or (a.suitIndex == b.suitIndex and a.faceIndex > b.faceIndex)):
                    pos = j
            self.planets[i], self.planets[pos] = self.planets[pos], self.planets[i] 
        
    def shuffle(self):
        n = len(self.cards)
        for i in range(n-1,0,-1): 
            j = random.randint(0,i+1) 
            self.planets[i],self.planets[j] = self.planets[j],self.planets[i]
