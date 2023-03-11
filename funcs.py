import time, re

class Funcs:
    def __init__(self, info, bot, s):
        self.info = info
        self.bot = bot
        self.s = s

    def update_roblist(self, string, server, extra=[]):
        # string = string.replace("\n", "\n")


        channelID = self.info[server]["channelID"]
        guildID = self.info[server]["guildID"]
        cooldown = self.info[server]["cooldown"]

        mixed = []  
        # print(string)
        ids = re.findall(r'<@[0-9]*>', string)
        names = re.findall(r'\(.*\)', string)

        for id in extra:
            ids.append(id)
            names.append("Unknown")

        for i in range(len(ids)):
            mixed.append([names[i].replace(")", "").replace("(", ""), ids[i].replace("<@", "").replace(">", "")])

        return mixed, ids, names

    def do(self, channelID, guildID, data):
        self.bot.triggerSlashCommand(270904126974590976, channelID=channelID, guildID=guildID, data=data)

    def rob(self, user, server):
        channelID = self.info[server]["channelID"]
        guildID = self.info[server]["guildID"]
        cooldown = self.info[server]["cooldown"]

        rob_dat = self.s.get(["rob"], inputs={"user":user[1]})
        Funcs.do(self, channelID, guildID, data=rob_dat)

    def dep(self, amount, server):
        channelID = self.info[server]["channelID"]
        guildID = self.info[server]["guildID"]
        cooldown = self.info[server]["cooldown"]

        dep_dat = self.s.get(["deposit"], inputs={"amount":amount})
        Funcs.do(self, channelID, guildID, data=dep_dat)

    def wit(self, amount, server):
        channelID = self.info[server]["channelID"]
        guildID = self.info[server]["guildID"]
        cooldown = self.info[server]["cooldown"]

        with_data = self.s.get(["withdraw"], inputs={"amount":amount})
        Funcs.do(self, channelID, guildID, data=with_data)

    def horseshoe(self, server):
        channelID = self.info[server]["channelID"]
        guildID = self.info[server]["guildID"]
        cooldown = self.info[server]["cooldown"]

        use_data = self.s.get(["use"], inputs={"item": "shoe"})
        Funcs.do(self, channelID, guildID, data=use_data)

    def whiskey(self, server):
        channelID = self.info[server]["channelID"]
        guildID = self.info[server]["guildID"]
        cooldown = self.info[server]["cooldown"]

        use_data = self.s.get(["use"], inputs={"item": "whiskey"})
        Funcs.do(self, channelID, guildID, data=use_data)

    def alcohol(self, server):
        channelID = self.info[server]["channelID"]
        guildID = self.info[server]["guildID"]
        cooldown = self.info[server]["cooldown"]

        use_data = self.s.get(["use"], inputs={"item": "alcohol"})
        Funcs.do(self, channelID, guildID, data=use_data)


    def use(self, item, server):
        channelID = self.info[server]["channelID"]
        guildID = self.info[server]["guildID"]
        cooldown = self.info[server]["cooldown"]

        use_data = self.s.get(["use"], inputs={"item": item})
        Funcs.do(self, channelID, guildID, data=use_data)


    def wishlist(self, server):
        channelID = self.info[server]["channelID"]
        guildID = self.info[server]["guildID"]
        cooldown = self.info[server]["cooldown"]

        with open("server.txt", "w") as srvr:
            server = srvr.write(str(server))

        use_data = self.s.get(["use"], inputs={"item": "wishlist"})
        Funcs.do(self, channelID, guildID, data=use_data)


    def balance(self, user, server):
        channelID = self.info["private"]["channelID"]
        guildID = self.info["private"]["guildID"]
        cooldown = self.info["private"]["cooldown"]
        # print(user)
        with open("server.txt", "w") as srvr:
            server = srvr.write(str(server))

        use_data = self.s.get(["balance"], inputs={"user": str(user)})
        Funcs.do(self, channelID, guildID, data=use_data)


    def market(self, item, server):
        channelID = self.info[server]["channelID"]
        guildID = self.info[server]["guildID"]
        cooldown = self.info[server]["cooldown"]

        use_data = self.s.get(["market", "view"], inputs={"item_filter": item})
        Funcs.do(self, channelID, guildID, data=use_data)

    def work(self, server):
        channelID = self.info[server]["channelID"]
        guildID = self.info[server]["guildID"]
        cooldown = self.info[server]["cooldown"]

        use_data = self.s.get(["work", "shift"], inputs={})
        Funcs.do(self, channelID, guildID, data=use_data)


    def run_any(self, command, server, inputs={}):
        channelID = self.info[server]["channelID"]
        guildID = self.info[server]["guildID"]
        cooldown = self.info[server]["cooldown"]

        use_data = self.s.get(command.split(" "), inputs=inputs)
        Funcs.do(self, channelID, guildID, data=use_data)


    def run_seq(self, seq, name):
        for event in seq:
            # print(event)
            if 'rob' in event.lower():
                print(event.lower()[4:-1])
                Funcs.rob(self, event.lower()[4:-1], name)
            if 'dep' in event.lower():
                print(event.lower()[4:-1])
                Funcs.dep(self, event.lower()[4:-1], name)
            if 'with' in event.lower():
                Funcs.wit(self, event.lower()[5:-1], name)
            if 'horseshoe' in event.lower():
                Funcs.horseshoe(self, name)
            if 'alcohol' in event.lower():
                Funcs.alcohol(self, name)
            if 'whiskey' in event.lower():
                Funcs.whiskey(self, name)
            if 'use' in event.lower():
                Funcs.use(self, event.lower()[4:-1], name)
            if 'market' in event.lower():
                Funcs.market(self, event.lower()[7:-1], name)
            if event.lower() in ['hunt', "fish", "dig", "search", "crime", "scratch"]:
                Funcs.run_any(self, event.lower(), name)
            if 'sleep' in event.lower():
                print(int(event.lower()[6:-1]))
                time.sleep(int(event.lower()[6:-1]))
    
    def depnwith(self, dep_amount, with_amount, name):
        Funcs.dep(self, dep_amount, name)
        time.sleep(1)
        Funcs.wit(self, with_amount, name)
