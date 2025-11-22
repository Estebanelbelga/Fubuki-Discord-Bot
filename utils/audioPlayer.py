class audioPlayer:
    def __init__(self):
        self.voiceClient = None
        self.isPlaying = False
        self.currentMusic = None
        self.queue = []
          
    async def connect(self, targetChannel):
        if self.voiceClient == None or not self.voiceClient.is_connected():
            self.voiceClient = await targetChannel.connect()
            return self.voiceClient

        if self.voiceClient.channel != targetChannel:
            await self.voiceClient.move_to(targetChannel)
            return self.voiceClient
        
        return self.voiceClient

    async def disconnect(self):
        if not self.voiceClient == None:
            await self.voiceClient.disconnect()
            return True
        
        return False
    
    async def play(self, msg, music):
        if not msg.author.voice: 
            return await msg.reply(":x: You must be in a voice channel to play music", delete_after = 5)
        
        if self.voiceClient == None or not self.voiceClient.is_connected():
            self.voiceClient = await self.connect(msg.author.voice.channel)
            self.isPlaying = False
            self.currentMusic = None
            self.queue = []

        if msg.author.voice.channel != self.voiceClient.channel: 
            return await msg.reply(f":x: Already playing music in <#{self.voiceClient.channel.id}>", delete_after = 5)
        
        if self.isPlaying:
            #ajouter musique à la queue
            return
        
        #jouer la musique afou