# Discord

from APISimplify import Discord

# get discord bot token --> https://discord.com/developers/applications

discord = Discord(token='BOT_TOKEN')

channel_id = 'YOUR_CHANNEL_ID'
discord.send_message(channel_id, 'Hello from APISimplify!')

# GitHub

from APISimplify import GitHub

# get github token --> https://github.com/settings/tokens get a classic token

github = GitHub(token='GITHUB_TOKEN')

user_info = github.get_user('username')
print(user_info)

# Fortnite

from APISimplify import Fortnite

# get fortnite api key --> fortniteapi.io

fortnite = Fortnite(api_key='FORTNITE_API_KEY')

stats = fortnite.get_player_stats('player_id')
print(stats)

More?
