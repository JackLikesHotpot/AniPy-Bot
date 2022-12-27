import discord
from queries.staffQuery import searchStaff
from queries.runQuery import run_query
from variables.staffVar import GetByStaff

def staffSearch(staffName):
    query = searchStaff()
    variables = GetByStaff(staffName)
    if variables:
        result = run_query(query, variables)
        if not result:
            return discord.Embed(description="There does not exist a person with the name {}.".format(staffName))

        embed = discord.Embed(
            colour=discord.Colour.dark_orange(),
            title=result["data"]["Staff"]["name"]["full"],
            url=result["data"]["Staff"]["siteUrl"]
        )

        characters = ""

        for char in result["data"]["Staff"]["characters"]["edges"]:
            characters += '[{}]({})'.format(char["node"]['name']['full'], char["node"]["siteUrl"]) + '\n'
        embed.add_field(name="Character List", value=characters)
        embed.set_thumbnail(url=result["data"]["Staff"]["image"]["large"])
        return embed