import random

class Product:
  
  def __init__(self, name=None, price=10, weight=20, flammability=0.5,
               identifier= random.randint(1000000, 9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier
