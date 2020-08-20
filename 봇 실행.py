import asyncio,discord
from discord.ext import commands

token = "NzQ1MjcwNzI3MzQ3MDExNjQ1.XzvVcw.Llov7BPsGheaiY8W5Nu9wxMbBsQ"
game = discord.Game("테스트")
bot = commands.Bot(command_prefix='>',status=discord.Status.online,activity=game)

@bot.event
async def on_ready():
        print("Start")

bot.run(token)
