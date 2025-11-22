class audioPlayer:
    def __init__(self):
        self.voiceClient = None
        self.currentMusic = None
        self.queue = []
          
    async def connect(self, targetChannel):
        if self.voiceClient == None or not self.voiceClient.is_connected():
            return await targetChannel.connect()

        if self.voiceClient.channel != targetChannel:
            return await self.voiceClient.move_to(targetChannel)
        
        return self.voiceClient

    async def disconnect(self):
        if not self.voiceClient == None:
            if self.voiceClient.is_connected():
                await self.voiceClient.disconnect()
                return True
        return False
    
    async def play(self, msg, music):        
        if self.voiceClient == None or not self.voiceClient.is_connected():
            self.voiceClient = await self.connect(msg.author.voice.channel)
            self.currentMusic = None
            self.queue = []

        if msg.author.voice.channel != self.voiceClient.channel: 
            return await msg.reply(f":x: Already playing music in <#{self.voiceClient.channel.id}>")
        
        await msg.reply(music["title"])

        if self.currentMusic != None:
            #ajouter musique à la queue
            return
        
        