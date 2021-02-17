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

class Furniture:
  def __init__(self, name, comfort):
    self.name = name    
    self.comfort = comfort

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
    
    Ingredient("Barley flour", "Processed by barley"), 
    
    #Berries
    Ingredient("Raspberry", "Found in Meadows"), 
    Ingredient("Blueberry", "Found in Black Forest"), 
    Ingredient("Cloudberries", "Found in Plains"), 

    #Mushrooms
    Ingredient("Mushroom", "Found in Meadows and Black Forest"), 
    Ingredient("Yellow Mushroom", "Found in crypt and dungeons within Black Forest and Swamp"),

    #Harvesting
    Ingredient("Barley", "Harvested in Plains"), 
    Ingredient("Carrot", "Harvested in Meadows"),
    Ingredient("Turnip", "Harvested in Meadows"),

    #Raw Food
    Ingredient("Raw meat", "Looted from deers and boars"),
    Ingredient("Entrails", "Looted from draugs"),
    Ingredient("Serpent meat", "Looted from Serpents"),

    #Cooked Food
    Ingredient("Queens Jam", "Crafted within a Cauldron"), 
    Ingredient("Cooked meat", "By cooking raw meat in Cooking station"),     
    Ingredient("Cooked Lox Meat", ""),     
    Ingredient("Cooked serpent meat", "By cooking serpent meat in Cooking station"),

    #Furniture
    Ingredient("Dragonbed", ""),
    Ingredient("Lox rug", ""),
    Ingredient("Wolf rug", ""),
    Ingredient("Deer rug", ""),
    Ingredient("Chair", ""),
    Ingredient("Raventhrone", ""),
    Ingredient("Banner", ""),
    Ingredient("Hanging Brazier", ""),
]

mobs = [
    Mob("Greyling", "Greylings are only found in the Meadows biome."),
    Mob("Greydwarf", "Greydwarfs spawn primarily in the Black Forest, but can spawn in other biomes during events")
]

furnitures = [
    Furniture("Nearby fire", "Seems to give 3"),
    Furniture("Dragonbed", "1 or 2"),
    Furniture("Lox rug", "1"),
    Furniture("Wolf rug", "1"),
    Furniture("Deer rug", "3 (The rugs stack, so you can get 5 total from all 3 in the same area)"),
    Furniture("Chair", "1"),
    Furniture("Raventhrone", "2 (The chairs don't stack)"),
    Furniture("Banner", "1"),
    Furniture("Hanging Brazier", "3"),
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
    ]),    
    Mead("Carrot soup", 
         "A warm tasty soup made of mostly carrots",
     [
        MeadIngredient("Mushroom", "1"),
        MeadIngredient("Carrot", "3")
    ]),
    Mead("Mead base: Minor stamina", 
         "",
     [
        MeadIngredient("Honey", "10"),
        MeadIngredient("Raspberry", "10"),
        MeadIngredient("Yellow Mushroom", "10")
    ]), 
    Mead("Mead base: Tasty", 
         "",
     [
        MeadIngredient("Honey", "10"),
        MeadIngredient("Raspberry", "10"),
        MeadIngredient("Blueberry", "5")
    ]), 
    Mead("Queens jam", 
         "You get 4",
     [
        MeadIngredient("Raspberry", "8"),
        MeadIngredient("Blueberry", "8")
    ]), 
    Mead("Sausages", 
         "You get 4",
     [
        MeadIngredient("Entrails", "2"),
        MeadIngredient("Raw meat", "1"),
        MeadIngredient("Thistle", "4")

    ]), 
    Mead("Mead base: Medium stamina", 
         "Used in fermenter to craft Medium stamina mead.",
     [
        MeadIngredient("Honey", "10"),
        MeadIngredient("Cloudberries", "10"),
        MeadIngredient("Yellow mushroom", "10")
    ]), 
    Mead("Barley wine base: Fire resistance", 
         "Used in fermenter to craft Medium stamina mead.",
     [
        MeadIngredient("Barley", "10"),
        MeadIngredient("Cloudberries", "10")
    ]), 
    Mead("Turnip stew", 
         "",
     [
        MeadIngredient("Raw meat", "1"),
        MeadIngredient("Turnip", "3")
    ]), 
    Mead("Blood pudding", 
         "",
     [
        MeadIngredient("Thistle", "2"),
        MeadIngredient("Bloodbag", "2"),
        MeadIngredient("Barley flour", "4")
    ]), 
    Mead("Bread", 
         "",
     [
        MeadIngredient("Barley flour", "10")
    ]), 
    Mead("Fish wraps", 
         "",
     [
        MeadIngredient("Barley flour", "4"),
        MeadIngredient("Cooked fish", "2")        
    ]), 
    Mead("Lox meat pie", 
         "",
     [
        MeadIngredient("Barley flour", "4"),
        MeadIngredient("Cloudberries", "2"),
        MeadIngredient("Cooked Lox Meat", "2")
    ]), 
    Mead("Serpent stew", 
         "",
     [
        MeadIngredient("Mushroom", "1"),
        MeadIngredient("Cooked serpent meat", "1"),
        MeadIngredient("Honey", "2")
    ])

]