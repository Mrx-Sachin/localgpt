#!/usr/bin/env python
import argparse
from bardapi import Bard
import re
from bardapi import BardCookies

cookie_dict = {
    "__Secure-1PSID": "<YOUR_ACTUAL_SECURE_1PSID_VALUE>",
"__Secure-1PSIDCC": "<YOUR_ACTUAL_SECURE_1PSIDCC_VALUE>"
}
import subprocess

def check_and_install_dependencies():
    required_modules = ['argparse', 'bardapi', 're']

    missing_modules = [module for module in required_modules if not module_installed(module)]

    if missing_modules:
        print(f"Installing missing modules: {', '.join(missing_modules)}")
        install_modules(missing_modules)
    else:
        print("All required modules are already installed.")

def module_installed(module):
    try:
        __import__(module)
        return True
    except ImportError:
        return False

def install_modules(modules):
    for module in modules:
        subprocess.run(['pip', 'install', module])
def get_answer(question):
    bard = BardCookies(cookie_dict=cookie_dict)

    # question = take all the things after file name  eg : cli.py  make zip of 10 txt file

    # Construct the input text
    input_text = "answer for linux cli in single line ,  " + question
    # Get the answer using Bard API
    # print(input_text)
    answer = bard.get_answer(input_text)
    # # Print the answer content
    print(answer['content'])
    return answer['content']

def main():
    check_and_install_dependencies()
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="CLI for interacting with Bard API")
    parser.add_argument("question", type=str, help="The question for Bard API")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Get the answer for the provided question
    ans=get_answer(args.question)
    # print (args.question)
    # Ask the user for further action
    action = input("Do you want to (r)egenerate, or take (N)o action on the command? (r/N): ")

    if action.lower() == 'r':
        print("Regenerating the command...")
        get_answer(ans+"above code not working \n"+args.question)
        # Add your regeneration logic here
    else:
        print("No action taken. Exiting...")

if __name__ == "__main__":
    main()
'''
pip install bardapi
pip install pyperclip
sudo apt-get install libxapp-gtk3-module

'''
