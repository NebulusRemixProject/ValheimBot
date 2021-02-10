from enum import Enum

class Food:
  def __init__(self, name, health, healing, stamina, duration, found):
    self.name = name
    self.health = health    
    self.healing = healing
    self.stamina = stamina
    self.duration = duration
    self.found = found

class Ingredient:
  def __init__(self, name, found):
    self.name = name
    self.found = found

class Mead:
  def __init__(self, name, description, ingredients):
    self.name = name
    self.description = description
    self.ingredients = ingredients

class Mob:
  def __init__(self, name, found):
    self.name = name    
    self.found = found

class MeadIngredient:
  def __init__(self, name, amount):
    self.name = name
    self.amount = amount

foods = [
    Food("Raspberry", 10, 1, 20, 600, "Found in Meadows"),
    Food("Blueberry", 15, 1, 20, 600, "Found in Black Forest"),
    Food("Queens Jam", 30, 2, 40, 1200, "Crafted within a Cauldron"),
    Food("Cooked meat", 40, 2, 30, 1200, "By cooking raw meat in Cooking station"),
    Food("Mushroom", 15, 1, 20, 600, "Found in Meadows and Black Forest"),
    Food("Yellow Mushroom", 20, 1, 20, 600, "Found in crypt and dungeons within Black Forest and Swamp")
]

ingredients = [
    Ingredient("Bloodbag", "Dropped by Leeches found in the Swamp"),
    Ingredient("Honey", "Found in beehives"),
    Ingredient("Dandelion", "Found in Meadows"),
    Ingredient("Thistle", "A faintly glowing blue plant, typically found within the swamp and black forest."),
    Ingredient("Greydwarf eye", "Drops from Greydwarfs, found in Black Forest"),
    Ingredient("Neck tail", "Dropped by Neck, found in Meadows"),
    Ingredient("Coal", "Dropped by Surtlings, found in the Swamp"), 
    Ingredient("Raspberry", "Found in Meadows"), 
    Ingredient("Blueberry", "Found in Black Forest"), 
    Ingredient("Queens Jam", "Crafted within a Cauldron"), 
    Ingredient("Cooked meat", "By cooking raw meat in Cooking station"), 
    Ingredient("Mushroom", "Found in Meadows and Black Forest"), 
    Ingredient("Yellow Mushroom", "Found in crypt and dungeons within Black Forest and Swamp")
]

mobs = [
    Mob("Greyling", "Greylings are only found in the Meadows biome."),
    Mob("Greydwarf", "Greydwarfs spawn primarily in the Black Forest, but can spawn in other biomes during events")
]

meads = [
    Mead("Mead base: Medium healing", 
         "Restores 7.5 health per second over the course of 30 seconds.",
        [
        MeadIngredient("Honey", "10"),
        MeadIngredient("Bloodbag", "4"),
        MeadIngredient("Raspberry", "10"),
        MeadIngredient("Dandelion", "1")
    ]),
    Mead("Mead base: Frost resistance", 
         "Fortifies you against frost, 10 Minutes (600 Seconds)",
        [
        MeadIngredient("Honey", "10"),
        MeadIngredient("Greydwarf eye", "1"),
        MeadIngredient("Bloodbag", "2"),
        MeadIngredient("Thistle", "5")
    ]),
    Mead("Mead Base: Minor Healing", 
         "Restores 3.3 health per second over the course of 30 seconds.",
      [
        MeadIngredient("Honey", "10"),
        MeadIngredient("Blueberries", "5"),
        MeadIngredient("Raspberry", "10"),
        MeadIngredient("Dandelion", "1")
    ]),    
    Mead("Mead base: Poison resistance", 
         "Fortifies you against Poison, 10 Minutes (600 Seconds)",
     [
        MeadIngredient("Honey", "10"),
        MeadIngredient("Neck tail", "1"),
        MeadIngredient("Coal", "10"),
        MeadIngredient("Thistle", "5")
    ])
]