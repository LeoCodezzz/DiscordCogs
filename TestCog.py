#imports
import discord
from discord.ext import commands

# CLASS FUNCTION
class TestCog(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    
    
  @commands.command()
  async def test(self, ctx): #ALWAYS CARRY "SELF" AS THE FIRST ARGUMENT!
    return await ctx.send("Congrats!, you have learnt to make a working cog!")
  
  
  
  
  #SETUP FUNCTION
  def setup(bot):
    bot.add_cog(TestCog(bot)
                
  # YOU HAVE MADE A WORKING COG!
  
  # ALL COMMANDS MUST HAVE THE SAME INDENT SPACE AS THE "DEF" FUNCTION IN THE CLASS FUNCTION. EXAMPLE:
                
  class TestCog(commands.Cog):
#---->     def __init__(self, bot):
       self.bot = bot
                
  #SAME INDENT SPACE (arrows for example)              
                
#---->     @commands.command()
           #rest of your command
