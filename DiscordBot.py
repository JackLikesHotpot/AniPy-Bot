import discord
from discord.ext import commands
from GetInfo import *
from ReverseSearch import reverseSearch as rSearch

client = commands.Bot(command_prefix = '!')
client.remove_command('help')

def removeTags(text):
    import re
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

@client.event
async def on_ready():
    print("Bot is ready.")

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please pass in all required arguments.")
    if isinstance(error, commands.CommandNotFound):
        print("Command not found.")
    else:
        print(error)

@client.command(aliases=['ANIME', 'anime', 'a'])
async def animeSearch(ctx, *, title):
    if title.isnumeric():
        query = SearchByID()
        variables = GetByID('anime', title)
    elif not title.isnumeric():
        query = SearchByTitle()
        variables = GetByTitle('anime', title)
    if variables:
        result = run_query(query, variables)
        if not result:
            await ctx.send("There does not exist an anime with a title/ID of {}.".format(title))
            return
        embed = discord.Embed(
            colour=discord.Colour.blue(),
            title=('{} ({}) {}'.format(result["data"]["Media"]["title"]["romaji"],
                                       result["data"]["Media"]["title"]["english"],
                                       result["data"]["Media"]["format"])),
            url=result["data"]["Media"]["siteUrl"],
            description=(removeTags(result["data"]["Media"]["description"])).replace("&quot;", '"')
        )
        embed.add_field(name="Status", value=result["data"]["Media"]["status"].upper(), inline=True)
        embed.add_field(name="Season",
                        value='{} {}'.format(result["data"]["Media"]["season"], result["data"]["Media"]["seasonYear"]),
                        inline=True)
        embed.add_field(name="Number of Episodes", value=result["data"]["Media"]["episodes"], inline=True)
        embed.add_field(name="Duration", value='{} minutes/episode'.format(result["data"]["Media"]["duration"], inline=True))
        embed.add_field(name="Favourites", value=result["data"]["Media"]["favourites"], inline=True)
        embed.add_field(name="Average Score", value='{}%'.format(result["data"]["Media"]["averageScore"], inline=True))
        embed.set_thumbnail(url=result["data"]["Media"]["coverImage"]["large"])
        await ctx.send(embed=embed)



@client.command(aliases=['MANGA', 'manga', 'm'])
async def mangaSearch(ctx, *, title):
    if title.isnumeric():
        query = SearchByID()
        variables = GetByID('manga', title)
    elif not title.isnumeric():
        query = SearchByTitle()
        variables = GetByTitle('manga', title)
    if variables:
        result = run_query(query, variables)
        if not result:
            await ctx.send("There does not exist a manga with a title/ID of {}.".format(title))
            return
        embed = discord.Embed(
            colour=discord.Colour.blue(),
            title=('{} ({}) {}'.format(result["data"]["Media"]["title"]["romaji"],
                                       result["data"]["Media"]["title"]["english"],
                                       result["data"]["Media"]["format"])),
            url=result["data"]["Media"]["siteUrl"],
            description=(removeTags(result["data"]["Media"]["description"])).replace("&quot;", '"')
        )
        embed.add_field(name="Status", value=result["data"]["Media"]["status"].upper(), inline=True)
        embed.add_field(name="Start Date",
                        value='{}/{}/{}'.format(result["data"]["Media"]["startDate"]["day"], result["data"]["Media"]["startDate"]["month"], result["data"]["Media"]["startDate"]["year"]),
                        inline=True)
        embed.add_field(name="Number of Chapters", value=result["data"]["Media"]["chapters"], inline=True)
        embed.add_field(name="Number of Volumes", value=result["data"]["Media"]["volumes"], inline=True)
        embed.add_field(name="Favourites", value=result["data"]["Media"]["favourites"], inline=True)
        embed.add_field(name="Average Score", value='{}%'.format(result["data"]["Media"]["averageScore"], inline=True))
        embed.set_thumbnail(url=result["data"]["Media"]["coverImage"]["large"])
        await ctx.send(embed=embed)

@client.command(aliases=['reverse', 'r'])
async def reverseSearch(ctx, *, link):
    await animeSearch(ctx=ctx,title=str(rSearch(link)))

@client.command(aliases=['h'])
async def help(ctx):
    embed = discord.Embed(
        colour = discord.Colour.orange()
    )
    embed.set_author(name='Help')
    embed.add_field(name='!anime <title>', value="Search anime by title or ID.", inline=False)
    embed.add_field(name='!manga <title>', value="Search manga by title or ID.", inline=False)
    embed.add_field(name='!user <username>', value="Search up a user by their username.", inline=False)
    embed.add_field(name='!reverse <image link>', value="Search an anime by a link to an image.", inline=False)
    await ctx.send(embed = embed)

@client.command(aliases=['user', 'u'])
async def userSearch(ctx, *, userName):
    query = SearchUser()
    variables = GetUser(userName)
    if variables:
        result = run_query(query, variables)
        if not result:
            await ctx.send("There does not exist a user with a name of {}.".format(userName))
            return

        try:
            desc = removeTags((result["data"]["User"]["about"]).replace("&quot;", '"'))
        except:
            desc = ""

        embedUser = discord.Embed(
            colour=discord.Colour.red(),
            title=result["data"]["User"]["name"],
            url=result["data"]["User"]["siteUrl"],
            description=desc
        )

        embedAni = discord.Embed(
            colour=discord.Colour.red(),
            title=("{}'s Favourite Anime".format(result["data"]["User"]["name"]))
        )

        embedMan = discord.Embed(
            colour=discord.Colour.red(),
            title=("{}'s Favourite Manga".format(result["data"]["User"]["name"]))
        )

        embedUser.add_field(name = 'Total Anime', value=result["data"]["User"]["statistics"]["anime"]["count"], inline = True)
        embedUser.add_field(name = 'Days Watched', value=round(int((result["data"]["User"]["statistics"]["anime"]["minutesWatched"])/1440), 1), inline = True)
        embedUser.add_field(name = "Mean Score", value=result["data"]["User"]["statistics"]["anime"]["meanScore"], inline = True)

        embedUser.add_field(name = "Total Manga", value=result["data"]["User"]["statistics"]["manga"]["count"], inline = True)
        embedUser.add_field(name = "Chapters Read", value=result["data"]["User"]["statistics"]["manga"]["chaptersRead"], inline = True)
        embedUser.add_field(name = "Mean Score", value=result["data"]["User"]["statistics"]["manga"]["meanScore"], inline = True)
        embedUser.set_thumbnail(url=result["data"]["User"]["avatar"]["large"])
        await ctx.send(embed=embedUser)

        animeFav = ""
        mangaFav = ""
        for fav in result["data"]["User"]["favourites"]["anime"]["nodes"]:
            animeFav += '{} ({})'.format(str(fav["title"]["romaji"]), str(fav["title"]["english"])) + "\n"
        embedAni.add_field(name = "Anime", value=animeFav)

        for fav in result["data"]["User"]["favourites"]["manga"]["nodes"]:
            mangaFav += '{} ({})'.format(str(fav["title"]["romaji"]), str(fav["title"]["english"])) + "\n"
        embedMan.add_field(name = "Manga", value=mangaFav)

        #await ctx.send(embed=embedAni)
        await ctx.send(embed=embedMan)

client.run('')