# AniPy Bot
A Discord bot that uses the AniList GraphQL API, coded in Python. 
You can search for anime/manga titles, users, reverse image anime pictures, and more.

# Disclaimer

**Currently incompatible with Slash Commands, and will probably just rewrite this project in JS instead.*

Code is somewhat poor and only reflective of my skills in Aug 2020.

# Features:
* !a <anime_name> - Search anime by title/ID
* !m <manga_name> - Search manga by title/ID
* !r <link> Reverse image search anime by image link
* !u <user_name> Search user by name
* Display a user's favourites
* Display the top 5 anime of a studio
* !ch <character_name> Search by character
* !st <staff_name> Search by staff
* !s <studio_name> Search by studio

# Example Use
![Example](https://i.imgur.com/S9Wjm4p.png)

# Requirements:
* Python 3.6.5+
* A Discord Developer Account

# Setup:
1. Clone this repo.
2. Create a new application in your [Discord Developer Account](https://discord.com/developers/applications).
3. In that application, go to the Bot page and add a bot.
4. Copy your bot's token and input it into `config.py`.
5. In your preferred command line, go into the AniPy-Bot folder and execute the command `pip install -r requirements.txt`.
6. Execute the bot with `python index.py`.

# Configuration:
* You can edit the command prefix in `config.py`.

# License:
MIT © xjl98 
