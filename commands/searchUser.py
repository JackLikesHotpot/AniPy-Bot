import discord
from misc.clean import *
from queries.userQuery import SearchUser
from queries.runQuery import run_query
from variables.userVar import GetUser


class Profile(discord.ui.View):
    def __init__(self, userResults):
        super().__init__()
        self.value = None
        self.user = userResults

    @discord.ui.button(label='User', style=discord.ButtonStyle.grey)
    async def menu1(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.edit_message(embed=userSearch(self.user))

    @discord.ui.button(label='Anime', style=discord.ButtonStyle.grey)
    async def menu2(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.edit_message(embed=userFavourites(self.user, 'anime'))

    @discord.ui.button(label='Manga', style=discord.ButtonStyle.grey)
    async def menu3(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.edit_message(embed=userFavourites(self.user, 'manga'))


def userError(userName):
    return discord.Embed(description="There does not exist a user with the name of {}.".format(userName))


def generateUserInfo(userName):
    result = run_query(SearchUser(), GetUser(userName))
    return result


def userSearch(result):
    userAnimeDetails = result["data"]["User"]["statistics"]["anime"]
    userMangaDetails = result["data"]["User"]["statistics"]["manga"]
    userDetails = result["data"]["User"]

    try:
        desc = removeTags(userDetails["about"]).replace("&quot;", '"')
    except:
        desc = ""

    embedUser = discord.Embed(
        colour=discord.Colour.red(),
        title=userDetails["name"],
        url=userDetails["siteUrl"],
        description=desc
    )

    embedUser.add_field(name='Total Anime', value=userAnimeDetails["count"], inline=True)
    embedUser.add_field(name='Days Watched', value=round(int((userAnimeDetails["minutesWatched"]) / 1440), 1),
                        inline=True)
    embedUser.add_field(name="Mean Score", value=userAnimeDetails["meanScore"], inline=True)

    embedUser.add_field(name="Total Manga", value=userMangaDetails["count"], inline=True)
    embedUser.add_field(name="Chapters Read", value=userMangaDetails["chaptersRead"], inline=True)
    embedUser.add_field(name="Mean Score", value=userMangaDetails["meanScore"], inline=True)
    embedUser.set_thumbnail(url=userDetails["avatar"]["large"])
    return embedUser


def userFavourites(result, type):
    desc = ''
    user = result['data']['User']

    favEmbed = discord.Embed(
        colour=discord.Colour.red(),
        title='''{}'s favourite {}'''.format(user['name'], type),
        url=user['siteUrl'],
    )
    favEmbed.set_thumbnail(url=user["avatar"]["large"])

    if result:
        for fav in result["data"]["User"]["favourites"][type]["nodes"]:
            desc += '[{} ({})]({}) \n'.format(fav['title']['romaji'], fav['title']['english'], fav['siteUrl'])
        favEmbed.description = desc

        if len(desc) <= 0:
            favEmbed.description = '{} has not listed any favourite {}.'.format(user['name'], type)

    return favEmbed
