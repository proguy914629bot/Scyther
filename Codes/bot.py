import discord
from discord.ext import commands

client = commands.Bot(command_prefix = 'PUT YOUR PREFIX HERE!')

@client.event
async def on_ready:
    print(f'{client.user} has logged in and is online!')

extensions = ['cogs.Moderation',
              'cogs.HelpCmd',
              'cogs.Music']
              
if __name__ == '__main__':
    for ext in extensions:
        client.load_extension(ext)
        
client.run('Put Your Token Here!')
