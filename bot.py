#IF YOU ARE USING NEXTCORD OR A DIFFERENT DISCORD.PY LIBARIE THIS WILL ALSO WORK!

#IMPORTS
import discord
import os
from discord import commands

bot = commands.Bot(command_prefix = "your prefix") #You can also add intents

#OPTINAL
@bot.event
async def on_ready():
  print("{bot.user} is online!")
  
  
# HOW TO LOAD COGS

for filename in os.listdir("./cogs"):
  if filename.endswith(".py"):
    bot.load_extension(f"cogs.{filename[:-3]}")
    
    
#YOUR BOT RUN FUNCTION
bot.run(YOUR TOKEN)
