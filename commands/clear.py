commandInfo = {
    "name": "clear",
    "description": "Delete messages from the channel",
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
        return await msg.reply(f":x: Missing **[x]** argument ```{prefix}help {commandInfo.get("name")}```")
    
    deletedMessages = 0
    channel = msg.channel

    try: 
        msgToDelete = int(args[0])
    except Exception as e: 
        return await msg.reply(f":x: Bad **[x]** argument ```{prefix}help {commandInfo.get("name")}```")

    if(len(args) == 1):  
        return await msg.channel.purge(limit = msgToDelete + 1)
        
    try:
        userToDeleteId = int(args[1].strip("<@!>"))
    except Exception as e: 
        return await msg.reply(f":x: Bad **[@user]** argument ```{prefix}help {commandInfo.get("name")}```")
           
    
    userToDelete = msg.guild.get_member(userToDeleteId) 

    if userToDelete == None : 
        return await msg.reply(f":x: User **'{args[1]}'** not found")   
    
    if msg.author != userToDelete:
        await msg.delete()
    else:
        msgToDelete += 1

    def is_userToDelete(m):
        return m.author == userToDelete

    return await msg.channel.purge(limit = msgToDelete, check = is_userToDelete)
