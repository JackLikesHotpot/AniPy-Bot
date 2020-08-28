import discord
from queries.idQuery import SearchByID
from queries.titleQuery import SearchByTitle
from variables.idVar import GetByID
from variables.titleVar import GetByTitle
from queries.runQuery import run_query
from misc.clean import removeTags, replaceNone


def mangaSearch(title):
    if title.isnumeric():
        query = SearchByID()
        variables = GetByID('manga', title)
    elif not title.isnumeric():
        query = SearchByTitle()
        variables = GetByTitle('manga', title)
    if variables:
        result = run_query(query, variables)
        if not result:
            return discord.Embed(description="There does not exist a manga with a title/ID of {}.".format(title))

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
                        value='{}/{}/{}'.format(result["data"]["Media"]["startDate"]["day"],
                                                result["data"]["Media"]["startDate"]["month"],
                                                result["data"]["Media"]["startDate"]["year"]),
                        inline=True)
        embed.add_field(name="Number of Chapters", value=replaceNone(result["data"]["Media"]["chapters"]), inline=True)
        embed.add_field(name="Number of Volumes", value=replaceNone(result["data"]["Media"]["volumes"]), inline=True)
        embed.add_field(name="Favourites", value=result["data"]["Media"]["favourites"], inline=True)
        embed.add_field(name="Average Score",
                        value='{}'.format(replaceNone(result["data"]["Media"]["averageScore"]), inline=True))
        embed.set_thumbnail(url=result["data"]["Media"]["coverImage"]["large"])
        return embed
