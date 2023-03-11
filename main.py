import random, discum, json, requests, threading, queue
from discum.utils.slash import SlashCommander
from discum.utils.button import Buttoner
import PySimpleGUI as sg
from funcs import Funcs


bot = discum.Client(token="YOUR_TOKEN_HERE", log=False)

slashCmds = bot.getSlashCommands("270904126974590976").json()
s = SlashCommander(slashCmds) 


with open("servers.json", "r") as file:
    file = file.read()
info = json.loads(file)


happy = ["yey", "whoohoo", "woo", "epic", "noice"]
angry = ["bruh", "wth", "wtf", "bro wtf", "bro wtf", "breh", "<a:rock_sus:1010570711414341683>"]
neutral = ["bruh", "breh", "sure", "lol", "rip"]
Funcs = Funcs(info, bot, s)


sg.LOOK_AND_FEEL_TABLE['RobbersTheme'] = {'BACKGROUND': '#000000',
                                        'TEXT': '#00FF00',
                                        'INPUT': '#000000',
                                        'TEXT_INPUT': '#FFD700',
                                        'SCROLL': '#00FF00',
                                        'BUTTON': ('#000000', '#FFD700'),
                                        'PROGRESS': ('#D1826B', '#CC8019'),
                                        'BORDER': 1, 'SLIDER_DEPTH': 0, 
'PROGRESS_DEPTH': 0, }


sg.theme('RobbersTheme')
cmd_sequence = ""

servers = []
for item in info:
    servers.append(item)

layout = [
        [sg.Text('Rob list:'), sg.Text(size=(25,1), key='Name')],

        [sg.Text('Wishlist output:', size=(20, 1), font='Lucida', justification='left'), sg.Button('Update')],
        [sg.Multiline(size=(60, 10), key='textbox'), sg.Multiline("sus", size=(60, 10), key='messagebox')],

        [   sg.Button(key='Horseshoe', image_filename="visuals/horseshoe.png"), sg.Button(key='Whiskey', image_filename="visuals/whiskey.png"), sg.Button(key='Alcohol', image_filename="visuals/alcohol.png"),
            sg.Button(key='Hunt', image_filename="visuals/Hunting_Rifle.png"), sg.Button(key='Fish', image_filename="visuals/Fishing_Pole.png"), sg.Button(key='Dig', image_filename="visuals/Shovel.png")
        ],
        [   sg.Button(key='Search', image_filename="visuals/search.png"), sg.Button(key='Crime', image_filename="visuals/knife.png"), sg.Button(key='Scratch', image_filename="visuals/lottery.png"),
            sg.Button(key='Work', image_filename="visuals/briefcase.png"), sg.Button(key='Padlock', image_filename="visuals/padlock.png"), sg.Button(key='Landmine', image_filename="visuals/landmine.png")
        ],
        [sg.Button(key='Wishlist', image_filename="visuals/Robberswishlist.png"), sg.Button("Check Balance", key="Check Balance"),

        [sg.Text('Server name:',size=(20, 1), font='Lucida', justification='left')],
        [sg.Combo(servers, key='name', size=(20, 1), default_value="2d")],

        [
            sg.Text('\n\n💰 Choose user to rob:', size=(20, 3), font='Lucida', justification='left')
        ],
        [
            sg.Combo(["                                                 "], key='board'), sg.Button(key="Rob", image_filename="visuals/robber.gif", size=(1,1),), sg.Button('Update Roblist')
        ],
        [
            sg.Text('Add user to roblist:', size=(20, 1), font='Lucida', justification='left'), sg.Input(key='new_id', default_text="", size=(15, 1)), sg.Button('Add')
        ],
        [
            sg.Text("")
        ],
        [
            sg.Button("Fail", key='Fail'), sg.Button("Dep & With", key='Dep & With')
        ],
        [
            sg.Text("")
        ],
        [
            sg.Input(key='wit_amount', default_text="100k", size=(10, 1)), sg.Button(key='With', image_filename="visuals/up.png"),
            sg.Input(key='dep_amount', default_text="all", size=(10, 1)), sg.Button(key='Dep', image_filename="visuals/down.png"),
        ],
        [
            sg.Input(key='use_item', default_text="wishlist", size=(10, 1)), sg.Button('Use'),
            sg.Input(key='market', default_text="wishlist", size=(10, 1)), sg.Button(key='Market View', image_filename="visuals/market.png")
        ],
        [
            sg.Text("")
        ],
        [sg.Button(key='happy', image_filename="visuals/thumbsup.png"), sg.Button(key="angry", image_filename="visuals/thumbsdown.png"), sg.Button(key="neutral", image_filename="visuals/neutral.png")],
        [
            sg.Text("")
        ],

        [sg.Button('Exit'), sg.Button(key='Record', image_filename="visuals/record.png"), sg.Button(key='Run Sequence', image_filename="visuals/play.png")]
    ]

def gui(q):
    window = sg.Window('Dank Memer', layout, keep_on_top=True, resizable=True)
    while True:
        event, values = window.read()
        # print(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            bot.gateway.close()
            break
        if event == 'Rob':
            if values["board"] == "":
                continue
            Funcs.rob(values["board"], values["name"])

        if event == 'Dep':
            Funcs.dep(values["dep_amount"], values["name"])

        if event == 'With':
            Funcs.wit(values["wit_amount"], values["name"])

        if event == 'Update Roblist':
            mixed, ids, names = Funcs.update_roblist(values["textbox"], values["name"])
            window['board'].Update(values=mixed)

        if event == 'Horseshoe':
            Funcs.horseshoe(values["name"])
        if event == 'Alcohol':
            Funcs.alcohol(values["name"])
        if event == 'Work':
            Funcs.work(values["name"])
        if event == 'Whiskey':
            Funcs.whiskey(values["name"])
        if event == 'i':
            sg.popup_no_wait(info)
        if event == 'Use':
            Funcs.use(values["use_item"], values["name"])
        if event == 'Padlock':
            Funcs.use("padlock", values["name"])

        if event == 'Landmine':
            Funcs.use("mine", values["name"])

        if event == 'Wishlist':
            Funcs.wishlist(values["name"])

        if event == 'Market View':
            Funcs.market(values["market"], values["name"])

        if event == 'Fail':
            Funcs.wit(values["wit_amount"]+"/10", values["name"])

        if event == 'Dep & With':
            threading.Thread(target=Funcs.depnwith, args=[values["dep_amount"], values["wit_amount"], values["name"]]).start()

        if event == 'angry':
            bot.sendMessage(str(info[values["name"]]["channelID"]), random.choice(angry))

        if event == 'neutral':
            bot.sendMessage(str(info[values["name"]]["channelID"]), random.choice(neutral))

        if event == 'happy':
            bot.sendMessage(str(info[values["name"]]["channelID"]), random.choice(happy))


        if event in ['Hunt', "Fish", "Dig", "Search", "Crime", "Scratch"]:
            Funcs.run_any(event.lower(), values["name"])

        if event == 'Add':
            tag = requests.get(f"https://discordlookup.mesavirep.xyz/v1/user/{values['new_id']}").json()["tag"]
            window['textbox'].Update(values["textbox"] + f"\n⏣ 000,000  <@{values['new_id']}> ({tag})")

        if event == 'Check Balance':
            Funcs.balance(values["board"][1], values["name"])

        if event == "Update":
            if not q.empty():
                item = q.get()
                window['messagebox'].Update(item)
                # print("updated")


        if event == "Record":
            layout2 = [[sg.Multiline(size=(60, 10), key='seq')], [sg.Button('Done')]]
            rec_window = sg.Window('Command Recorder', layout2)
            while True:
                event2, values2 = rec_window.read()
                if event2 == "Done":
                    cmd_sequence = values2["seq"]
                    rec_window.close()
                    break
        if event == "Run Sequence":
            sequence = cmd_sequence.splitlines()
            threading.Thread(target=Funcs.run_seq, args=[sequence, values["name"]]).start()


    window.close()




q = queue.Queue()

threading.Thread(target=gui, args=(q, )).start()

priv_channel_id = info["private"]["channelID"]

with open("servers.json", "r") as file:
    file = file.read()
info = json.loads(file)

priv_channel_id = info["private"]["channelID"]



@staticmethod
def click(message, guildID):
    try:
        message = bot.getMessage(message["channel_id"], message["id"])
        data = message.json()[0]
        buts = Buttoner(data["components"])
        bot.click(
            data["author"]["id"],
            channelID=data["channel_id"],
            guildID = guildID,
            messageID=data["id"],
            messageFlags=data["flags"],
            data=buts.getButton("Read Pocket Wishlist"),
        )
    except: pass

@bot.gateway.command
def recieve_message(message):
    if message.event.ready_supplemental:
        bot.gateway.subscribeToGuildEvents(wait=1)
    if message.event.message:
        m = message.parsed.auto()

        if int(m["author"]["id"]) == 270904126974590976:
            with open("server.txt", "r") as srvr:
                server = srvr.read()
            if int(m["channel_id"]) == info[server]["channelID"]:
                # print(server)
                try:
                    with open("server.txt", "r") as srvr:
                        server = srvr.read()
                    x = click(m, info[server]["guildID"])
                except IndexError:
                    pass


@bot.gateway.command
def get_balance(message):
    if message.event.ready_supplemental:
        bot.gateway.subscribeToGuildEvents(wait=1)
    if message.event.message:
        m = message.parsed.auto()
        if int(m["author"]["id"]) == 270904126974590976:
            if int(m["channel_id"]) == priv_channel_id:
                try:
                    if "Balance" in m["embeds"][0]["title"]:
                        title = m["embeds"][0]["title"]
                        description = m["embeds"][0]["description"]
                        wallet = description.split("\n")[0]
                        bank = description.split("\n")[1]
                        inv = description.split("\n")[3]
                        market_net = description.split("\n")[4]

                        q.put(f"{title}\nWallet: {wallet}\nBank: {bank}\nInventory Worth: {inv}\nMarket Net: {market_net}")
                except KeyError:
                    pass



@bot.gateway.command
def get_wish(message):
    if message.event.ready_supplemental:
        bot.gateway.subscribeToGuildEvents(wait=1)
    if message.event.message:
        m = message.parsed.auto()
        if int(m["author"]["id"]) == 270904126974590976:
            with open("server.txt", "r") as srvr:
                server = srvr.read()
            if int(m["channel_id"]) == info[server]["channelID"]:
                try:
                    if "Robbable Users in" in m["embeds"][0]["title"]:
                        title = m["embeds"][0]["title"]
                        description = m["embeds"][0]["description"]
                        q.put(f"{title}\n{description}")
                except KeyError:
                    pass
                    

bot.gateway.run()
