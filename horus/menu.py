import os
import sys
import json
import textwrap
from google import genai
from typing import Callable
from dotenv import load_dotenv
from colors import BOLD,BLUE,YELLOW,RESET,RED
from chat_util import validate_api_key


load_dotenv()
MAIN_COMMAND = "horus"

DATA_FILE = os.getenv("DATA_FILE")

def welcome() -> None:
    print(f"""{BOLD}{YELLOW}
  ██╗  ██╗ ██████╗ ██████╗ ██╗   ██╗███████╗
  ██║  ██║██╔═══██╗██╔══██╗██║   ██║██╔════╝
  ███████║██║   ██║██████╔╝██║   ██║███████╗
  ██╔══██║██║   ██║██╔══██╗██║   ██║╚════██║
  ██║  ██║╚██████╔╝██║  ██║╚██████╔╝███████║
  ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝                              
    {RESET}""")
    print(f"{BLUE}  Welcome! Here are some basic commands{RESET}")
    

def validate_command(message: str, menu: dict) -> tuple[bool,str,str,str]:
    response = (False,'N.A','N.A')
    
    if len(message) == 0:
        return (False,'','',f"Invalid Command! Empty input.")
    
    command: list[str] = message.split() 
    if len(command) != 2:
        return (False,'','',f"Invalid Command! Expected two words.")
    
    main_cmmd, sub_cmmd = command
    
    if main_cmmd != MAIN_COMMAND or not sub_cmmd in menu:
        return (False,'','',f"Unknown command '{message}'")
    
    return (True,main_cmmd,sub_cmmd,'')

def main_menu() -> None:
    print(f"{BLUE}  Main-Menu{RESET}")
    print(f"{BLUE}  --------------------------{RESET}")
    print(f"  ► LLM Setup  -  horus setup")
    print(f"  ► Chat       -  horus chat")
    print(f"  ► Clear      -  horus clear")
    print(f"  ► Exit       -  horus exit")
    print(f"{BLUE}  --------------------------{RESET}")

sub_menu = {
    "setup": lambda : setup(),
    "chat": lambda : chat(),
    "exit": lambda : exit_horus(),
    "clear": lambda :clear(),
}

def ploop(message: str, err_mssg: str, validation_fn: Callable[[str],bool])-> str:
    while True:
        value = input(f"{message}")
        if validation_fn(value):
            return value
        else:
            print(f"{BOLD}{RED}> {err_mssg}{RESET}")

def setup():
    config: dict[str,str] = {}
    name: str
    api_key: str
    
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE,"r") as file:
            config = json.load(file)
        name = config.get("name")
        api_key = config.get("api_key")
        
        print(f"{BLUE}  -INFORMATION--------------{RESET}")
        print(f"{BLUE}  -NAME: {name} {RESET}")
        print(f"{BLUE}  -API KEY: {api_key} {RESET}")
        print(f"{BLUE}  --------------------------{RESET}")
    
    intent = ploop("> Do You Want to Update? [Y/N]: ","Please Enter Y or N",lambda input: input in ["Y","N","y","n"])
    if intent.lower() == "y":
        name: str = ploop(f"> Name: ",f"Please enter name correctly!",lambda name: len(name.strip()) != 0 and name.isalnum())
        api_key: str = ploop(f"> API-KEY: ",f"Invalid API-KEY!",lambda api_key: len(api_key.strip()) != 0 and validate_api_key(api_key))

        config = {"name": name.strip(), "api_key": api_key.strip()}
        
        with open(DATA_FILE,"w") as file:
            json.dump(config,file,indent=4)
            
        print("> SETUP COMPLETE")
    
    clear()
        
            
def chat():
    if not os.path.exists(DATA_FILE): 
        print(f"{RED}> Complete setup! 'horus setup'{RESET}")
        return
    else:
        with open(DATA_FILE,"r") as file:
            config = json.load(file)
        name = config.get("name")
        api_key = config.get("api_key")
        
    print(f"""{BLUE}
  ██████╗██╗  ██╗ █████╗ ████████╗
  ██╔════╝██║  ██║██╔══██╗╚══██╔══╝
  ██║     ███████║███████║   ██║   
  ██║     ██╔══██║██╔══██║   ██║   
  ╚██████╗██║  ██║██║  ██║   ██║   
   ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝                       
          {RESET}""")
    
    print(f"To end the chat -> $END$")
    
    client = genai.Client(api_key = api_key)
    chat = client.chats.create(model="gemini-2.0-flash")
    
    while True:
        prompt = input(f"{YELLOW}> {name}: {RESET}")
        if prompt == "$END$":
            break
        
        response = chat.send_message(prompt)
        formatted_response = textwrap.fill(response.text, width=80)
        print(f"{BLUE}> HORUS: {formatted_response}")

    clear()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    main_menu()

def exit_horus():
    print("""
  ██████╗ ██╗   ██╗███████╗██╗
  ██╔══██╗╚██╗ ██╔╝██╔════╝██║
  ██████╔╝ ╚████╔╝ █████╗  ██║
  ██╔══██╗  ╚██╔╝  ██╔══╝  ╚═╝
  ██████╔╝   ██║   ███████╗██╗
  ╚═════╝    ╚═╝   ╚══════╝╚═╝                          
          """)
    raise sys.exit(0)
    