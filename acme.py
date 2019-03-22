import random

class Product:
  
  def __init__(self, name=None, price=10, weight=20, flammability=0.5,
               identifier= random.randint(1000000, 9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier
        
  def stealability(self):
    price_over_weight = self.price / self.weight
    
    if price_over_weight < 0.5:
      return "Not so stealable..."
    elif price_over_weight >= 0.5 and price_over_weight < 1.0:
      return "Kinda stealable."
    else:
      return "Very stealable!"
    
  def explode(self):
    flam_times_weight = self.flammability * self.weight
    
    if flam_times_weight < 10:
      return "...fizzle."
    elif flam_times_weight >= 10 and flam_times_weight < 10:
      return "...boom!"
    else:
      return "...BABOOM!!"
    
    
class BoxingGlove(Product):
  
  def __init__(self, name=None, price=10, weight=10, flammability=0.5,
               identifier= random.randint(1000000, 9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier
    
    
    
  def explode(self):
    return "...it's a glove"
  
  def punch(self):
    glove_weight = self.weight
    
    if glove_weight < 5:
      return "That tickles."
    
    elif glove_weight >= 5 and glove_weight < 15:
      return "Hey that hurt"
    else:
      return "OUCH!"
