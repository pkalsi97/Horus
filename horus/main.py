import sys
import os
from google import genai
from typing import Callable
from horus.menu import welcome,main_menu,sub_menu, validate_command
from colors import BOLD,BLUE,YELLOW,RESET,RED

def main() -> None:
    welcome()
    main_menu()
    
    while True:
        message: str = input(f"> ").strip().lower()
        is_valid, main_cmmd, sub_cmmd, err_msg = validate_command(message,sub_menu)
        
        if not is_valid:
            print(f"> {RED}{err_msg}{RESET}")
        else:
            sub_menu[sub_cmmd]()

    
if __name__ == "__main__":
    main()
    
    

