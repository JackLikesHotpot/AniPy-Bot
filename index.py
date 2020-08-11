from discord.ext import commands
from commands.searchAnime import animeSearch
from commands.reverseSearch import reverseSearch
from commands.searchManga import mangaSearch
from commands.searchStudio import studioSearch
from misc.help import helpMessage
from misc.checkUser import checkUser
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
    await ctx.send(embed=animeSearch(title))


@client.command(aliases=["MANGA", "m"])
async def manga(ctx, *, title):
    await ctx.send(embed=mangaSearch(title))


@client.command(aliases=['REVERSE', 'r'])
async def reverse(ctx, *, link):
    await ctx.send(embed=animeSearch(title=str(reverseSearch(link))))


@client.command(aliases=['USER', 'u'])
async def user(ctx, *, userName):
    if checkUser(userName):
        result = generateUserInfo(userName)
        await ctx.send(embed=userSearch(result))
        await ctx.send(embed=userAnime(result))
        await ctx.send(embed=userManga(result))

@client.command(aliases=['STUDIO', 's'])
async def studio(ctx, *, studioName):
    await ctx.send(embed=studioSearch(studioName))

client.run('')
