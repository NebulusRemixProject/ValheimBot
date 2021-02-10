from enum import Enum

class ItemType(Enum):
    Food = 1,
    Ingredient = 2
    Mob = 3

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
  def __init__(self, itemType, name, amount):
    self.itemType = itemType
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
    Ingredient("Coal", "Dropped by Surtlings, found in the Swamp")   
]

mobs = [
    Mob("Greyling", "Greylings are only found in the Meadows biome."),
    Mob("Greydwarf", "Greydwarfs spawn primarily in the Black Forest, but can spawn in other biomes during events")
]

meads = [
    Mead("Mead base: Medium healing", 
         "To get the potion you have to ferment your mead base in a fermenter, this takes a while.\n" +
         "You get 6 potions out of 1 mead base.\n" +
         "A potion made with the Fermenter from a Mead base: Medium healing. It restores 75 health over 120 seconds.\n" +
         "Upon consumption a 2min buff is applied preventing consumption of another Medium Healing Mead and increasing the rate of health regeneration.\n",
        [
        MeadIngredient(ItemType.Ingredient, "Honey", "10"),
        MeadIngredient(ItemType.Ingredient, "Bloodbag", "4"),
        MeadIngredient(ItemType.Food, "Raspberry", "10"),
        MeadIngredient(ItemType.Ingredient, "Dandelion", "1")
    ]),
    Mead("Mead base: Frost resistance", 
         "Fortifies you against frost, 10 Minutes (600 Seconds)\n" +
         "You get 6 potions out of 1 mead base.",
        [
        MeadIngredient(ItemType.Ingredient, "Honey", "10"),
        MeadIngredient(ItemType.Ingredient, "Greydwarf eye", "1"),
        MeadIngredient(ItemType.Ingredient, "Bloodbag", "2"),
        MeadIngredient(ItemType.Ingredient, "Thistle", "5")
    ]),
    Mead("Mead Base: Minor Healing", 
         "To get the potion you have to ferment your mead base in a fermenter, this takes a while.\n" +
         "You get 6 potions out of 1 mead base.",
        [
        MeadIngredient(ItemType.Ingredient, "Honey", "10"),
        MeadIngredient(ItemType.Food, "Blueberries", "5"),
        MeadIngredient(ItemType.Food, "Raspberry", "10"),
        MeadIngredient(ItemType.Ingredient, "Dandelion", "1")
    ]),    
    Mead("Mead base: Poison resistance", 
         "Fortifies you against Poison, 10 Minutes (600 Seconds)\n" +
         "You get 6 potions out of 1 mead base.",
        [
        MeadIngredient(ItemType.Ingredient, "Honey", "10"),
        MeadIngredient(ItemType.Ingredient, "Neck tail", "1"),
        MeadIngredient(ItemType.Ingredient, "Coal", "10"),
        MeadIngredient(ItemType.Ingredient, "Thistle", "5")
    ])
]