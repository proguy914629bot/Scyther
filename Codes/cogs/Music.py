import discord
from discord.ext import commands
import youtube_dl
import DiscordUtils

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    music = DiscordUtils.Music()
        
    @commands.command(aliases = ['p'])
    async def play(self, ctx, *, url):
        try:
            await ctx.send(f'Joined `{ctx.author.voice.channel.name}`.')
            player = music.get_player(guild_id=ctx.guild.id)
            if not player:
                player = music.create_player(ctx, ffmpeg_error_betterfix=True)
            if not ctx.voice_bot.is_playing():
                await ctx.send(f'Searching for `{url}` in YouTube.. Please Wait')
                await player.queue(url, bettersearch=True)
                song = await self.player.play()
                await ctx.send(f"Playing `{self.song.name}`")
            else:
                await ctx.send(f'Searching for `{url}` in YouTube.. Please Wait')
                song = await self.player.queue(url, bettersearch=True)
                await ctx.send(f"Queued `{self.song.name}`")
        except:
            await ctx.send('Please do the `sc!j` or `sc!join` command first. Thanks!')
            return
            
    @commands.command(aliases = ['j'])
    async def join(self, ctx):
        try:
            await ctx.author.voice.channel.connect() #Joins author's voice channel
        except:
            await ctx.send('You are not in a Voice Channel! Please join a voice channel and try again!')
            return
        await ctx.send(f'Joined `{ctx.author.voice.channel.name}`.')
    
    @commands.command(aliases = ['disconnect'])
    async def leave(self, ctx):
        try:
            await ctx.voice_bot.disconnect()
        except:
            await ctx.send(f'I am not in a Voice Channel {ctx.author.mention}!')
            return
        await ctx.send('📭 Left/Disconnected from the Voice Channel.')
        
    @commands.command()
    async def pause(self, ctx):
        try:
            player = music.get_player(guild_id=ctx.guild.id)
            song = await self.player.pause()
            await ctx.send(f"Paused `{self.song.name}`")
        except:
            await ctx.send('Nothing is currently playing right now.')
            
    @commands.command()
    async def resume(self, ctx):
        try:
            player = music.get_player(guild_id=ctx.guild.id)
            song = await self.player.resume()
            await ctx.send(f"Resumed `{self.song.name}``")
        except:
            await ctx.send('Nothing is currently playing right now.')
            
    @commands.command()
    async def stop(self, ctx):
        player = music.get_player(guild_id=ctx.guild.id)
        await self.player.stop()
        await ctx.send("Stopped playing music!")
        
    @commands.command(aliases = ['l'])
    async def loop(self, ctx):
        try:
            player = music.get_player(guild_id=ctx.guild.id)
            song = await self.player.toggle_song_loop()
            if song.is_looping:
                await ctx.send(f"🔂 Enabled loop for `{self.song.name}`")
            else:
                await ctx.send(f"🔂 Disabled loop for `{self.song.name}`")
        except:
            await ctx.send('Nothing is currently playing right now.')
            
    @commands.command(aliases = ['q'])
    async def queue(self, ctx):
        player = music.get_player(guild_id=ctx.guild.id)
        embed = discord.Embed(
            color = discord.Color.gold(),
            title = f'Queue: ',
            description = f"{', '.join([song.name for song in player.current_queue()])}"
        )
        await ctx.send(embed=embed)
        
    @commands.command(aliases = ['np'])
    async def nowplaying(self, ctx):
        try:
            player = music.get_player(guild_id=ctx.guild.id)
            song = self.player.now_playing()
            embed = discord.Embed(
                color = discord.Color.gold(),
                title = '⏯️ Now/Currently Playing:',
                description = f'{self.song.name}'
            )
            await ctx.send(embed=embed)
        except:
            embed = discord.Embed(
                color = discord.Color.gold(),
                title = '⏯️ Now/Currently Playing:',
                description = f'Nothing is currently playing right now!'
            )
            await ctx.send(embed=embed)
            
    @commands.command(aliases = ['s', 'fs'])
    async def skip(self, ctx):
        player = music.get_player(guild_id=ctx.guild.id)
        data = await self.player.skip(force=True)
        if len(data) == 2:
            await ctx.send(f"Skipped from {data[0].name} to {data[1].name}")
        else:
            await ctx.send(f"Skipped {data[0].name}")
    
def setup(bot):
    bot.add_cog(BotRelated(bot))
    print('Music Commands Cog Is Ready!')
