commandInfo = {
    "name": "disco",
    "description": "Disconnect the bot from its voice channel", 
    "usage": "disconnect"
}

async def run(msg, audioPlayer):
    if await audioPlayer.disconnect():
        return await msg.reply(":white_check_mark: **Disconnected** from voice channel !")
    else:
        return await msg.reply(":x: Not in a voice channel")