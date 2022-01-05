# AniPy Bot
A Discord bot that uses the AniList GraphQL API, coded in Python. 
You can search for anime/manga titles, users, reverse image anime pictures, and more.

# Disclaimer
Just pushed up a change (05/01/22) to fix a problem caused by tracemoepy at v4.1.
**Don't think I plan to return to this project again.** Code is somewhat poor and only reflective of my skills in Aug 2020.

# Features:
* Search anime by title/ID
* Search manga by title/ID
* Reverse image search anime by image link
* Search user by name
* Display a user's favourites
* Display the top 5 anime of a studio
* Search by character
* Search by staff
* Search by studio

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
