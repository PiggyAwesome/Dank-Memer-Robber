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

### How to run:

1. Run `pip install -r requirements.txt` to install the required libraries
2. Run the program with Python, while making sure that you are executing the command in the same folder as `funcs.py` and `visuals`

### Functions:

## 1. Log Robber's wishlist
#### If you click the Wishlist button, and then the Update button, the wishlist will be pasted in Window 2. If this does not work, you need to manually copy the wishlist.  <br>

![image](https://user-images.githubusercontent.com/48888771/224492562-8e2628cd-9f99-421d-9d90-5f6bac464df5.png)

## 2. Add users to roblist
#### To add users to the roblist you can either copy and paste your wishlist into Window 1, or add a User ID manually. After you have added the users click the `Update Roblist` button.<br>
![image](https://user-images.githubusercontent.com/48888771/224492898-18f99142-977e-40a8-9ec3-40b145731a71.png)

## 3. Select command location
#### Select a server you have added in `servers.json` using the dropdown menu before sending any commands. <br>

![image](https://user-images.githubusercontent.com/48888771/224492962-c37fca33-9898-4e9d-b7e8-4099c0ca6b1c.png)
