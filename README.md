# Dank-Memer-Robber
An easy GUI for Dank Memer robbers!


Coming this week

### How to set up:

1. Go into main.py and add your discord user token:
```py
bot = discum.Client(token="YOUR_TOKEN_HERE", log=False)
```
2. Add your own server info in servers.json
```json
    "private": {                       // You must have a private server. This is where balance checks and non interactive commands get executed
        "channelID": 69696969,         // Channel ID where the commands will be sent
        "guildID": 69696969,           // Guild ID of your private server
        "cooldown": 20                 // Cooldown in seconds for the /rob command
    },
    
    "johnnys server": {                // You can add rob servers like this and name them anything you want
        "channelID": 69696969,         // Channel ID where the commands will be sent
        "guildID": 69696969,           // Guild ID of server 
        "cooldown": 20                 // Cooldown in seconds for the /rob command
    },
    
    ...
```
