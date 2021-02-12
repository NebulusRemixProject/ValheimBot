from discord import Embed
from .library import furnitures

def comfort(query=None):    
    embedVar = "```\nComfort\nMax comfort is ?\n"
    for furniture in furnitures:
        #embedVar.add_field(name=furniture.name, value=furniture.comfort, inline=True)    
        embedVar = "{0} {1:<17} {2}\n".format(embedVar, furniture.name, furniture.comfort)     
    embedVar = embedVar + "```"
    return embedVar