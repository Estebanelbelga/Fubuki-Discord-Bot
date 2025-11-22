import asyncio
import yt_dlp

commandInfo = {
    "name": "play",
    "description": "Play a song in your voice channel",
    "usage": "play [music]",
    "args": [
        {"name": "music", "description": "Song name or YouTube URL (song or playlist)", "required": True}
    ]
}

class ytDlpSilentLogger:
    def debug(self, msg): pass
    def warning(self, msg): pass
    def error(self, msg): print(f"Error while searching on youtube: {msg}")

async def searchQuery(query):
    def searching():
        with yt_dlp.YoutubeDL({
            "logger": ytDlpSilentLogger(), 
            "noplaylist": True, 
            "format": "bestaudio/best",
            "quiet": True,
            "default_search": "ytsearch1"}) as ydl: # type: ignore
                return ydl.extract_info(query, download = False)
    return await asyncio.to_thread(searching)

async def run(msg, prefix, args, audioPlayer):
    if not msg.author.voice: return await msg.reply(":x: You must be in a **voice channel** to play music")
    if len(args) == 0: return await msg.reply(f":x: Missing **[music]** argument ```{prefix}help {commandInfo.get("name")}```")

    query = " ".join(args)
    results = await searchQuery(query)

    print(f"results: {results}")

    if 1 < len(results["entries"]): # type: ignore
        for entry in results["entries"]: # type: ignore
            print("playlist send")
            await audioPlayer.play(msg, entry)
        return
    
    print("music send")
    return await audioPlayer.play(msg, results["entries"][0]) # type: ignore
