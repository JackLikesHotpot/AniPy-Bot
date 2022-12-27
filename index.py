import discord
from discord.ext import commands
from discord import app_commands, Interaction, Embed, Intents

from commands.searchAnime import animeSearch
from commands.reverseSearch import reverseSearch
from commands.searchManga import mangaSearch
from commands.searchStudio import studioSearch
from commands.searchStaff import staffSearch
from commands.searchCharacter import charSearch
from commands.searchUser import userSearch, userError, generateUserInfo, Profile

from misc.help import helpMessage
from config import token


class Client(discord.Client):
    def __init__(self):
        super().__init__(intents=Intents.default())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync()
            self.synced = True
        print('All commands synced!')

client = Client()
tree = app_commands.CommandTree(client)


@tree.command(name='help', description='Brings up the list of commands and things you can do with the bot.')
async def help(interaction: Interaction):
    await interaction.response.send_message(embed=helpMessage())


@tree.command(name='anime', description="Search for an anime based on its title or Anilist ID.")
@app_commands.describe(anime='Search by title or Anilist ID')
async def anime(interaction: Interaction, anime: str):
    await interaction.response.send_message(embed=animeSearch(anime))


@tree.command(name='manga', description="Search for an manga based on its title or Anilist ID.")
@app_commands.describe(manga='Search by title or Anilist ID')
async def manga(interaction: Interaction, manga: str):
    await interaction.response.send_message(embed=mangaSearch(manga))


@tree.command(name='reverse', description="Reverse search an anime based on an image")
@app_commands.describe(link='Search image of an anime (PNG/JPG)')
async def manga(interaction: Interaction, link: str):
    if link.endswith(".jpg") or link.endswith(".png") or link.endswith(".jpeg"):
        await interaction.response.send_message(embed=animeSearch(title=str(reverseSearch(link))))
    else:
        await interaction.response.send_message(embed=Embed(description="Link is not a .jpg or a .png file."))


@tree.command(name='user', description="Search for a user by name")
@app_commands.describe(username='Search for a user on AniList.')
async def user(interaction: Interaction, username: str):
    result = generateUserInfo(username)
    if result:
        await interaction.response.send_message(embed=userSearch(result), view=Profile(result))
    else:
        await interaction.response.send_message(embed=userError(username))


@tree.command(name='studio', description="Search for an anime studio by name")
@app_commands.describe(studio='Search for an animation studio by name.')
async def studio(interaction: Interaction, studio: str):
    await interaction.response.send_message(embed=studioSearch(studio))


@tree.command(name='staff', description="Searches for an anime staff by name")
@app_commands.describe(staff='Search for a staff member by name.')
async def staff(interaction: Interaction, staff: str):
    await interaction.response.send_message(embed=staffSearch(staff))


@tree.command(name='character', description="Searches for a character by name")
@app_commands.describe(character='Search for a character by name.')
async def char(interaction: Interaction, character: str):
    await interaction.response.send_message(embed=charSearch(character))


client.run(token)
