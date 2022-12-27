import discord
from queries.idQuery import SearchByID
from queries.titleQuery import SearchByTitle
from variables.idVar import GetByID
from variables.titleVar import GetByTitle
from queries.runQuery import run_query
from misc.clean import removeTags


def animeSearch(title):
    try:
        if title.isnumeric():
            query = SearchByID()
            variables = GetByID('anime', title)
        elif not title.isnumeric():
            query = SearchByTitle()
            variables = GetByTitle('anime', title)
    except AttributeError:
        if type(title) == int:
            query = SearchByID()
            variables = GetByID('anime', title)

    if variables:
        result = run_query(query, variables)
        if not result:
            return discord.Embed(description="There does not exist an anime with a title/ID of {}.".format(title))

        else:
            media = result['data']['Media']
            embed = discord.Embed(
                colour=discord.Colour.blue(),
                title=('{} ({}) {}'.format(media["title"]["romaji"], media["title"]["english"], media["format"])),
                url=media["siteUrl"],
                description=(removeTags(media["description"])).replace("&quot;", '"')
            )
            embed.add_field(name="Status", value=media["status"].upper(), inline=True)
            embed.add_field(name="Season", value='{} {}'.format(media["season"], media["seasonYear"]), inline=True)
            embed.add_field(name="Number of Episodes", value=media["episodes"], inline=True)
            embed.add_field(name="Duration", value='{} minutes/episode'.format(media["duration"], inline=True))
            embed.add_field(name="Favourites", value=media["favourites"], inline=True)
            embed.add_field(name="Average Score", value='{}%'.format(media["averageScore"], inline=True))
            embed.set_thumbnail(url=media["coverImage"]["large"])
            return embed