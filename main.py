import discord
import logging 
import json 
import inspect
from utils import commandsLoader, audioPlayer

with open("config.json") as c:
        config = json.load(c)
discordToken = config["discordToken"]
prefix = config["prefix"]

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.voice_states = True
bot = discord.Client(intents=intents)

commands = commandsLoader.loadCommands()
audioPlayer = audioPlayer.audioPlayer()

@bot.event
async def on_ready():
        await bot.change_presence(activity=discord.Game(name=f"{prefix}help for available commands"))
        print(f"{bot.user}: Bot is up")

@bot.event
async def on_message(msg):
        if msg.author.bot: return 
        if not msg.content.startswith(prefix): return
        userCmd = msg.content[len(prefix):].split()

        if userCmd[0] in commands:
                command = commands[userCmd[0]]["function"]

                inspection = inspect.signature(command)
                kwargs = {}

                for item in inspection.parameters.items():
                        if item[0] == "msg": 
                                kwargs["msg"] = msg
                        if item[0] == "prefix": 
                                kwargs["prefix"] = prefix
                        if item[0] == "args":
                                kwargs["args"] = userCmd[1:]
                        if item[0] == "bot":
                                kwargs["bot"] = bot
                        if item[0] == "commands":
                                kwargs["commands"] = commands
                        if item[0] == "audioPlayer":
                                kwargs["audioPlayer"] = audioPlayer
                
                return await command(**kwargs)
                
bot.run(discordToken, log_level=logging.WARNING)