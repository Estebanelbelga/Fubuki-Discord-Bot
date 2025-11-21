import importlib
import os 

def loadCommands(commandsFoler = "commands"): 
        commands = {}

        for file in os.listdir(commandsFoler): 
                if file.startswith("_") or not file.endswith(".py") : continue

                moduleName = f"{commandsFoler}.{file[:-3]}"

                try:
                        module = importlib.import_module(moduleName)
                except Exception as e: 
                        print(f"Error while loading {moduleName}: {e}")
                        continue 
                
                if not hasattr(module, "commandInfo") or not hasattr(module, "run"): continue

                commands[module.commandInfo.get("name")] = {
                        "function": module.run,
                        "info": module.commandInfo
                }
                
        return commands