commandInfo = {
    "name": "ping",
    "description": "Indicates the bot's latency",
    "usage": "ping"
}

async def run(msg, bot):
    return await msg.reply(f"Pong :ping_pong: ! Latency: {round(bot.latency * 1000)}ms")