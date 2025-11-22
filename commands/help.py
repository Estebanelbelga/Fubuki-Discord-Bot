import discord

commandInfo = {
    "name": "help",
    "description": "Shows commands and what they do",
    "usage": "help [command]",
    "args": [
        {"name": "command",
         "description": "Shows how tu use that specific command", 
         "required": False
        }
    ]
}

async def run(msg, prefix, args, commands):
    if len(args) >= 1:
        if args[0] in commands:
            commandInfo = commands[args[0]]["info"]
            
            help = discord.Embed (
                title = f"{commandInfo["name"]}",
                description = f"{commandInfo["description"]}",
                color = discord.Color.green()
            )

            help.add_field(name = "Usage: ", value = f"{prefix}{commandInfo["usage"]}", inline = False)

            if "args" in commandInfo:
                for arg in commandInfo["args"]:
                    argName = arg["name"]
                    argDescription = arg["description"]
                    required = arg["required"]

                    if not required:
                            argName += " (optionnal)"

                    help.add_field(name = f"{argName}:", value = argDescription, inline = False)

            return await msg.reply(embed=help) 
        
        else:
            return await msg.reply(f":x: Command **{args[0]}** not found ```{prefix}help```", delete_after = 5) 

    help = discord.Embed(
         title = "List of available commands:",
         color = discord.Color.green()
    )

    for command in commands:
        help.add_field(name = f"{commands[command]["info"]["name"]}:", value = commands[command]["info"]["description"], inline = False)

    return await msg.reply(embed=help)