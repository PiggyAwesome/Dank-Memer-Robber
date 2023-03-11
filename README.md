# Dank-Memer-Robber
An easy GUI for Dank Memer robbers!

This application is against the Discord AND Dank Memer TOS. I only created this program as a proof of concept. I advise you to not use this program, even if the chances of you getting banned are really slim.

It is advised to read through the entire Readme before running this program. If you post an issue, but you have not followed all of these steps - it will instantly be closed.

![image](https://user-images.githubusercontent.com/48888771/224500616-d5a6fd97-5e48-4c8a-b6aa-fe1dc7cd2d3d.png)

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
2. Run the program with Python, while making sure that you are executing the command in the same folder as `funcs.py`, `servers.json` and `visuals`

## Functions:


## Select command location
#### Select a server you have added in `servers.json` using the dropdown menu before sending any commands. <br>

![image](https://user-images.githubusercontent.com/48888771/224495194-3cebb24d-da98-42ae-964b-cddeb0164cac.png)<br>
![image](https://user-images.githubusercontent.com/48888771/224492962-c37fca33-9898-4e9d-b7e8-4099c0ca6b1c.png)


## Log Robber's wishlist
#### If you click the Wishlist button, and then the Update button, the wishlist will be pasted in Window 2. If this does not work, you need to manually copy the wishlist.  <br>

![image](https://user-images.githubusercontent.com/48888771/224492562-8e2628cd-9f99-421d-9d90-5f6bac464df5.png)

## Add users to roblist
#### To add users to the roblist you can either copy and paste your wishlist into Window 1, or add a User ID manually. After you have added the users, click the `Update Roblist` button.<br>

![image](https://user-images.githubusercontent.com/48888771/224492898-18f99142-977e-40a8-9ec3-40b145731a71.png)


## Rob a user
#### You can select a user in the rob selector and press the rob button to rob the user.

![image](https://user-images.githubusercontent.com/48888771/224495120-d933f02e-2af3-4e5b-8b7f-482343b3dbd9.png)



## Check balance
#### You can check a user's balance by selecting them in the rob dropdown. You can then press the update button and the balance will be pasted in Window 2<br>

![image](https://user-images.githubusercontent.com/48888771/224494964-d4eee448-bbd6-48a1-82d3-9c12bc0a4ce2.png)


## Misc
#### This application makes it easy to quickly do the following:
1. Use a horseshoe
2. Use Whiskey
3. Use Alcohol
4. Hunt
5. Fish
6. Dig
7. Search
8. Crime
9. Scratch
10. Work
11. Use Padlock
12. Use Landmine

![image](https://user-images.githubusercontent.com/48888771/224493189-efb86fa6-9356-4bdf-af1b-18f1a61a41dd.png)


## Deposit, Withdraw, Use, Market
1. Fail: Withdraws 10% of your withdraw amount
2. Dep & With: Deposits and Withdraws directly after each other
3. Withdraw: Withdraws the specified amount of money
4. Deposit: Deposits the specified amount of money
5. Use: Uses the specified item with no arguments
6. Market: Views current market offers for the specified item

![image](https://user-images.githubusercontent.com/48888771/224493849-2b156561-b552-40b1-ad53-4f3b9bd3243b.png)


## Reactions
#### You can easily send random short replies based on your mood (changeable in `main.py`):
- 👍 Happy = ["yey", "whoohoo", "woo", "epic", "noice"]
- 👎 Sad = ["bruh", "wth", "wtf", "bro wtf", "bro wtf", "breh", "<a:rock_sus:1010570711414341683>"]
- 😐 Neutral = ["bruh", "breh", "sure", "lol", "rip"] <br>

![image](https://user-images.githubusercontent.com/48888771/224494160-e635c408-4dea-4d5f-955e-a390cf3cbae3.png)

## Record and play
#### You can record a script and let it run while you are afk
1. Click the red circle to enter the command recorder
2. Enter your command sequence (see below for reference) and click done when finished
3. Click the play button to execute the commands

### Valid command recorder commands:
```
rob(USERID)
dep(AMOUNT)
with(AMOUNT)
horseshoe
alcohol
whiskey
use(ITEM)
market(ITEM)
hunt
fish
dig
search
crime
scratch
sleep(SECONDS)
```


![image](https://user-images.githubusercontent.com/48888771/224494242-2ab4800d-19c8-446c-b857-a4e012096c8e.png)<br>
![image](https://user-images.githubusercontent.com/48888771/224494763-a9b6a0f8-bee0-4ab9-8f2f-0e6d29b28705.png)
