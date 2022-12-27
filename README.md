# AniPy Bot
A Discord bot that uses the AniList GraphQL API, coded in Python. 
You can search for anime/manga titles, users, reverse image anime pictures, and more.

# Features:
* /anime <anime name>- Search anime by title/ID
* /manga <manga name> - Search manga by title/ID
* /reverse <link> Reverse image search anime by image link
* /user <anilist username> Search user by name
* /character <character name> Search by character
* /staff <staff name> Search by staff
* /studio <studio name> Search by studio

# Example Use
![Example](https://i.imgur.com/PIDSrAg.png)

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
* You can edit the bot's token in `config.py`.

# License:
MIT © JackLikesHotpot 
