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
        args = userCmd[1:]

        if userCmd[0] in commands:
                command = commands[userCmd[0]]["function"]

                inspection = inspect.signature(command)
                kwargs = {}

                for item in inspection.parameters.items():
                        if item[0] in locals():
                                kwargs[item[0]] = locals()[item[0]]
                        elif item[0] in globals():
                                kwargs[item[0]] = globals()[item[0]]

                return await command(**kwargs)
                
bot.run(discordToken, log_level=logging.WARNING)