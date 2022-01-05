import discord
from queries.idQuery import SearchByID
from queries.titleQuery import SearchByTitle
from variables.idVar import GetByID
from variables.titleVar import GetByTitle
from queries.runQuery import run_query
from misc.clean import removeTags


def animeSearch(title):
    if title.isnumeric():
        query = SearchByID()
        variables = GetByID('anime', title)

    elif not title.isnumeric():
        query = SearchByTitle()
        variables = GetByTitle('anime', title)

    if variables:
        result = run_query(query, variables)
        if not result:
            return discord.Embed(description="There does not exist an anime with a title/ID of {}.".format(title))

        data = result['data']['Media']

        embed_string = '{}'.format(data['title']['romaji'])
        if data['title']['english'] is None:
            embed_string += ' {}'.format(data['format'])
        else:
            embed_string += ' ({}) {}'.format(data['title']['english'], data['format'])

        embed = discord.Embed(
            colour=discord.Colour.blue(),
            title=(embed_string),
            url=data["siteUrl"],
            description=(removeTags(data["description"])).replace("&quot;", '"')
        )
        embed.add_field(name="Status", value=data["status"].upper(), inline=True)
        embed.add_field(name="Season",
                        value='{} {}'.format(data["season"], data["seasonYear"]),
                        inline=True)
        embed.add_field(name="Number of Episodes", value=data["episodes"], inline=True)
        embed.add_field(name="Duration",
                        value='{} minutes/episode'.format(data["duration"], inline=True))
        embed.add_field(name="Favourites", value=data["favourites"], inline=True)
        embed.add_field(name="Average Score", value='{}%'.format(data["averageScore"], inline=True))
        embed.set_thumbnail(url=data["coverImage"]["large"])
        return embed