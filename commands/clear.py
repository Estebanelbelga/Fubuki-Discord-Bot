commandInfo = {
    "name": "clear",
    "description": "Deletes messages from the channel",
    "usage": "clear [x] [@user]",
    "args": [
        {"name": "x",
         "description": "Number of messages to delete", 
         "required": True
        },
        {"name": "@user",
         "description": "Deletes messages only from that user", 
         "required": False
        }
    ]
}

async def run(msg, prefix, args):
    if not len(args) >= 1: 
        return await msg.reply(f":x: Missing arguments ```{prefix}help {commandInfo.get("name")}```", delete_after = 5)
    
    deletedMessages = 0
    channel = msg.channel

    try: 
        msgToDelete = int(args[0])
    except Exception as e: 
        return await msg.reply(f":x: Bad arguments ```{prefix}help {commandInfo.get("name")}```", delete_after = 5)

    if(len(args) == 1):  
        deletedMessages = len(await msg.channel.purge(limit = msgToDelete + 1))
        return await channel.send(f":white_check_mark: {deletedMessages - 1} messages got deleted !", delete_after = 5)
    
    try:
        userToDeleteId = int(args[1].strip("<@!>"))
    except Exception as e: 
        return await msg.reply(f":x: Bad arguments ```{prefix}help {commandInfo.get("name")}```", delete_after = 5)
           
    
    userToDelete = msg.guild.get_member(userToDeleteId) 

    if userToDelete == None : 
        return await msg.reply(f":x: User **{args[1]}** not found", delete_after = 5)   
    
    if msg.author != userToDelete:
        await msg.delete()
    else:
        msgToDelete += 1
        deletedMessages = -1

    def is_userToDelete(m):
        return m.author == userToDelete

    deletedMessages += len(await msg.channel.purge(limit = msgToDelete, check = is_userToDelete))

    if deletedMessages == -1:    
        deletedMessages = 0

    return await channel.send(f":white_check_mark: {deletedMessages} messages got deleted !", delete_after = 5)
