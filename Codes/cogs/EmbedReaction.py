import discord
from discord.ext import commands
import DiscordUtils

class EmbedWithReactions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def AutoEmbedWithReaction(self, ctx):
        embed1 = discord.Embed(color=ctx.author.color).add_field(name="Example", value="Page 1")
        embed2 = discord.Embed(color=ctx.author.color).add_field(name="Example", value="Page 2")
        embed3 = discord.Embed(color=ctx.author.color).add_field(name="Example", value="Page 3")
        paginator = DiscordUtils.Pagination.AutoEmbedPaginator(ctx)
        embeds = [embed1, embed2, embed3]
        await paginator.run(embeds)
        
    @commands.command()
    async def ManualEmbedWithReaction(self, ctx):
        embed1 = discord.Embed(color=ctx.author.color).add_field(name="Example1", value="Page 1").add_field(name = 'Example2', value = 'Page 1')
        embed2 = discord.Embed(color=ctx.author.color).add_field(name="Example1", value="Page 2").add_field(name = 'Example2', value = 'Page 2').add_field(name = 'Example3', value = 'Page 1')
        embed3 = discord.Embed(color=ctx.author.color).add_field(name="Example1", value="Page 3")
        paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx)
        paginator.add_reaction('⏮️', "first")
        paginator.add_reaction('⏪', "back")
        paginator.add_reaction('🔐', "lock")
        paginator.add_reaction('⏩', "next")
        paginator.add_reaction('⏭️', "last")
        embeds = [embed1, embed2, embed3]
        await paginator.run(embeds)
        
def setup(bot):
    bot.add_cog(EmbedWithReactions(bot))
    print('EmbedWithReaction Command Cog is Ready!')
