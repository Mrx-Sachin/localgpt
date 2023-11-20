from bardapi import Bard
import os
import pyperclip
import tkinter as tk
from plyer import notification
from tkinter import scrolledtext

# Set your API key
from bardapi import BardCookies
cookie_dict = {
    "__Secure-1PSID": "<YOUR_ACTUAL_SECURE_1PSID_VALUE>",
"__Secure-1PSIDCC": "<YOUR_ACTUAL_SECURE_1PSIDCC_VALUE>"
}

bard = BardCookies(cookie_dict=cookie_dict)
# Get the question from the clipboard
question = pyperclip.paste()

# Construct the input text
input_text =  question
# Get the answer using Bard API
answer = bard.get_answer(input_text)

# Check if the answer is short enough for a notification
if len(answer['content']) <= 100:
    # Display notification
    notification_title = "Answer"
    notification_message = answer['content']
    notification.notify(title=notification_title, message=notification_message)
else:
    # Create a GUI window
    root = tk.Tk()
    root.title("Answer Display")

    # Create a scrolled text widget
    scroll_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20)
    scroll_text.insert(tk.END, answer['content'])
    scroll_text.pack()

    # Start the GUI event loop
    root.mainloop()






