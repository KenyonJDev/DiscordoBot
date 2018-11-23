import discord
from discord.ext import commands
import lavalink

time_rx = re.compile('[0-9]+')
url_rx = re.compile('https?:\/\/(?:www\.)?.+')

class music:
    def __init__(self, client):
        self.client = client


    @commands.command(aliases=['p','P'])
    @commands.guild_only()
    async def play(self, ctx, *, query: str):
        """searches and plays a song"""
        player = self.client.lavalink.players.get(ctx.guild.id)

        query = query.strip('<>')

        if not url_rx.match(query):
            query = f'ytsearch:{query}'

        results = await self.client.lavalink.get_tracks(query)

        if not results or not results['tracks']:
            return await ctx.send('Nothing found!')

        embed = discord.Embed(color=discord.Color.blurple())

        if results['loadType'] == 'PLAYLIST_LOADED':
            tracks = results['tracks']

            for track in tracks:
                player.add(requester=ctx.author.id, track=track)

            embed.title = 'Playlist Enqueued!'
            embed.description = f'{results["playlistInfo"]["name"]} - {len(tracks)} tracks'
            await ctx.send(embed=embed)
        else:
            track = results['tracks'][0]
            embed.title = 'Track Enqueued'
            embed.description = f'[{track["info"]["title"]}]({track["info"]["uri"]})'
            await ctx.send(embed=embed)
            player.add(requester=ctx.author.id, track=track)

        if not player.is_playing:
            await player.play()


def setup(bot):
    bot.add_cog(music(bot))
    print("music loaded")