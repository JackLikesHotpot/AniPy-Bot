import discord


def helpMessage():
    embed = discord.Embed(
        colour=discord.Colour.orange()
    )
    embed.set_author(name='Help')
    embed.add_field(name='!anime <title>', value="Search anime by title or ID.", inline=False)
    embed.add_field(name='!manga <title>', value="Search manga by title or ID.", inline=False)
    embed.add_field(name='!user <username>', value="Search up a user by their username.", inline=False)
    embed.add_field(name='!reverse <image link>', value="Search an anime by a link to an image.", inline=False)
    return embed