import sys
from google import genai
from typing import Callable
from chat_utility import validate_api_key, available_llms, ChatUtility

YELLOW="\033[093m"
RED ="\033[091m"
RESET="\033[0m"
BOLD = "\033[1m"

EXIT = "$EXIT$"

def ploop(validation_fn: Callable[[str], bool], message:str, err: str) -> str:
    while True:
        value = input(f"{message}")
        if value == EXIT:
            sys.exit(0)
        elif not validation_fn(value):
            print(f"{BOLD}{RED}-> {err}{RESET}")
        else:
            return value
            

# Welcome, Name, LLM, API-KEY (with Validation)
def welcome() -> tuple[str,str,str]:
    print(f"""{BOLD}{YELLOW}
████████╗██╗  ██╗███████╗██████╗ ███████╗███████╗
╚══██╔══╝██║  ██║██╔════╝██╔══██╗██╔════╝██╔════╝
   ██║   ███████║█████╗  ██████╔╝█████╗  ███████╗
   ██║   ██╔══██║██╔══╝  ██╔══██╗██╔══╝  ╚════██║
   ██║   ██║  ██║███████╗██████╔╝███████╗███████║
   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═════╝ ╚══════╝╚══════╝
          {RESET}""")
    name: str = ploop(lambda name: len(name.strip()) != 0 and name.isalnum(),f"Name: ",f"Please enter name correctly!")
    llm_provider = ploop(lambda llm: len(llm.strip()) and llm.strip().upper() in available_llms, f"LLM-PROVIDER [{", ".join(available_llms)}]: ", f"Please enter LLM-PROVIDER correctly!")
    api_key: str = ploop(lambda api_key: len(api_key.strip()) != 0 and validate_api_key(api_key,llm_provider.upper()),f"API-KEY: ",f"Invalid API-KEY!")
    return (name,api_key,llm_provider)

    
def main() -> None:
    name, api_key, llm_provider = welcome()
    chat_util = ChatUtility(name,llm_provider,api_key)
    print("Enter -> $EXIT$ to exit")
    while True:
        message = input(f"{name} :")
        if message == EXIT:
            sys.exit(0)
        else:
            chat_util.chat(message)
        
    
if __name__ == "__main__":
    main()
    
    

