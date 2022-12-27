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

        else:
            media = result['data']['Media']
        embed = discord.Embed(
            colour=discord.Colour.blue(),
            title=('{} ({}) {}'.format(media["title"]["romaji"], media["title"]["english"], media["format"])),
            url=media["siteUrl"],
            description=(removeTags(media["description"])).replace("&quot;", '"')
        )

        embed.add_field(name="Status", value=media["status"].upper(), inline=True)
        embed.add_field(name="Start Date", value='{}/{}/{}'.format(media["startDate"]["day"], media["startDate"]["month"], media["startDate"]["year"]), inline=True)
        embed.add_field(name="Number of Chapters", value=replaceNone(media["chapters"]), inline=True)
        embed.add_field(name="Number of Volumes", value=replaceNone(media["volumes"]), inline=True)
        embed.add_field(name="Favourites", value=media["favourites"], inline=True)
        embed.add_field(name="Average Score", value='{}'.format(replaceNone(media["averageScore"]), inline=True))
        embed.set_thumbnail(url=media["coverImage"]["large"])
        return embed
