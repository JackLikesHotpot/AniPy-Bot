from discord import HTTPException
from discord.ext import commands
from commands.searchAnime import animeSearch
from commands.reverseSearch import reverseSearch
from commands.searchManga import mangaSearch
from commands.searchStudio import studioSearch
from commands.searchStaff import staffSearch
from commands.searchCharacter import charSearch
from misc.help import helpMessage
from commands.searchUser import *

client = commands.Bot(command_prefix='!')
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


@client.command(aliases=['h'])
async def help(ctx):
    await ctx.send(embed=helpMessage())


@client.command(aliases=["ANIME", "a"])
async def anime(ctx, *, title):
    embed = animeSearch(title)
    await ctx.send(embed=embed)


@client.command(aliases=["MANGA", "m"])
async def manga(ctx, *, title):
    embed = mangaSearch(title)
    await ctx.send(embed=embed)


@client.command(aliases=['REVERSE', 'r'])
async def reverse(ctx, *, link):
    title = str(reverseSearch(link))
    if not title:
        await ctx.send(discord.Embed(description="Image is malformed or something went wrong."))        ##########################################
    else:
        await ctx.send(embed=animeSearch(title=str(reverseSearch(link))))


@client.command(aliases=['USER', 'u'])
async def user(ctx, *, userName):
    result = generateUserInfo(userName)
    if result:
        try:
            userEmbed = userSearch(result)
            await ctx.send(embed=userEmbed)

            userAnimeEmbed = userAnime(result)
            await ctx.send(embed=userAnimeEmbed)

            userMangaEmbed = userManga(result)
            await ctx.send(embed=userMangaEmbed)
        except HTTPException:
            pass
    else:
        await ctx.send(embed=userError(userName))


@client.command(aliases=['STUDIO', 's'])
async def studio(ctx, *, studioName):
    embed = studioSearch(studioName)
    await ctx.send(embed=embed)


@client.command(aliases=['STAFF', 'st'])
async def staff(ctx, *, staffName):
    embed = staffSearch(staffName)
    await ctx.send(embed=embed)


@client.command(aliases=["CHARACTER", 'ch', 'char'])
async def character(ctx, *, charName):
    embed = charSearch(charName)
    await ctx.send(embed=embed)


client.run('')
