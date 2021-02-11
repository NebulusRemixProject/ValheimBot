from discord import Embed

class HelpCommand:
  def __init__(self, name, usage, description):
    self.name = name
    self.usage = usage
    self.description = description


help_commands = []
help_commands.append(HelpCommand('cauldron', 'cauldron [recipie name]', 'Displays for cauldron recipies'))
help_commands.append(HelpCommand('search', 'search [text]', 'Searches and displays the first entry in the Valheim fandom wiki'))
help_commands.append(HelpCommand('food', 'food [food name]', 'Displays foods'))


def bot_help(query=None):
  # Show all commands
  if query is None:
    embed_var = Embed(title="Help commands", description="Desc")
    for command in help_commands:
      embed_var.add_field(name=command.usage, value=command.description, inline=False)
    return embed_var
  # Search for specific command
  else:
    command_search = query.lower()
    found = False
    embed_var = Embed(title="Command:" + command_search, description="Desc")
    for command in help_commands:
      if command.name == command_search:
        embed_var.add_field(name=command.usage, value=command.description)
        found = True
    if found == False:
      embed_var.add_field(name='Command ' + command_search, value='Not found')
    return embed_var


