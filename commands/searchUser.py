import discord
from misc.clean import *
from queries.userQuery import SearchUser
from queries.runQuery import run_query
from variables.userVar import GetUser

def userError(userName):
    return discord.Embed(description="There does not exist a user with the name of {}.".format(userName))


def generateUserInfo(userName):
    result = run_query(SearchUser(), GetUser(userName))
    return result

def userSearch(result):
    try:
        desc = removeTags(result["data"]["User"]["about"]).replace("&quot;", '"')
    except:
        desc = ""

    embedUser = discord.Embed(
        colour=discord.Colour.red(),
        title=result["data"]["User"]["name"],
        url=result["data"]["User"]["siteUrl"],
        description=desc
    )

    embedUser.add_field(name = 'Total Anime', value=result["data"]["User"]["statistics"]["anime"]["count"], inline = True)
    embedUser.add_field(name = 'Days Watched', value=round(int((result["data"]["User"]["statistics"]["anime"]["minutesWatched"])/1440), 1), inline = True)
    embedUser.add_field(name = "Mean Score", value=result["data"]["User"]["statistics"]["anime"]["meanScore"], inline = True)

    embedUser.add_field(name = "Total Manga", value=result["data"]["User"]["statistics"]["manga"]["count"], inline = True)
    embedUser.add_field(name = "Chapters Read", value=result["data"]["User"]["statistics"]["manga"]["chaptersRead"], inline = True)
    embedUser.add_field(name = "Mean Score", value=result["data"]["User"]["statistics"]["manga"]["meanScore"], inline = True)
    embedUser.set_thumbnail(url=result["data"]["User"]["avatar"]["large"])
    return embedUser


def userAnime(result):

    aniFav = result["data"]["User"]["favourites"]["anime"]["nodes"]
    embedAni = discord.Embed(
        colour=discord.Colour.red()
    )

    favs = ""
    if aniFav:
        for fav in result["data"]["User"]["favourites"]["anime"]["nodes"]:
            favs += '[{} ({})]({})'.format((fav["title"]["romaji"]), (fav["title"]["english"]), fav["siteUrl"]) + "\n\n"
        embedAni.add_field(name=("{}'s Favourite Anime".format(result["data"]["User"]["name"])), value=favs)
        embedAni.set_thumbnail(url=result["data"]["User"]["avatar"]["large"])
    return embedAni


def userManga(result):

    manFav = result["data"]["User"]["favourites"]["manga"]["nodes"]
    embedMan = discord.Embed(
        colour=discord.Colour.red()
    )

    favs = ""
    if manFav:
        for fav in result["data"]["User"]["favourites"]["manga"]["nodes"]:
            favs += '[{} ({})]({})'.format((fav["title"]["romaji"]), (fav["title"]["english"]), fav["siteUrl"]) + "\n\n"
        embedMan.add_field(name=("{}'s Favourite Manga".format(result["data"]["User"]["name"])), value=favs)
        embedMan.set_thumbnail(url=result["data"]["User"]["avatar"]["large"])
        return embedMan