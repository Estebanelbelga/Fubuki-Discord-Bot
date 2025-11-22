commandInfo = {
    "name": "play",
    "description": "Plays music in user's voice channel",
    "usage": "play [music]",
    "args": [
        {"name": "music", "description": "The music to play", "required": True}
    ]
}

async def run(msg, prefix, args, audioPlayer):
    if len(args) == 0: 
        return await msg.reply(f":x: Missing arguments ```{prefix}help {commandInfo.get("name")}```", delete_after = 5)
    
    #utlilisation de machin pour generer piste audio

    await audioPlayer.play(msg, "piste audio")