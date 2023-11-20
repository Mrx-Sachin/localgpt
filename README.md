# localGPT

This repository contains a Python script designed to simplify querying Bard, a tool frequently used during tasks. The script allows users to effortlessly search for answers to questions by copying the text and executing the script. For improved convenience, it is recommended to set up a shortcut for running the script.

## Project Features

- **Query Automation:** Quickly search for answers to questions by copying the text and running the Python script.
- **Dependency Integration:** Utilizes Bard API, Pyperclip, Plyer, and Tkinter for an efficient and seamless user experience.
- **Installation Guide:** Step-by-step instructions on installing Python, required libraries, and setting up the environment.
- **Cookie Configuration:** Guidance on obtaining and inserting the necessary cookies (__Secure-1PSID and __Secure-1PSIDCC) from the Bard website.

## Project Demo

### GUI version

https://github.com/Mrx-Sachin/localgpt/assets/112502093/20d1b0a2-70da-48e1-b8d3-454455bc7a75

### CLI version

![Screenshot from 2023-11-20 23-13-24](https://github.com/Mrx-Sachin/localgpt/assets/112502093/033088ba-bf29-4a9d-851c-45869cf9c59b)

## How to Use

1. Install Python and required libraries.
2. Set up Tkinter (usually included with Python).
3. Obtain "__Secure-1PSID" and "__Secure-1PSIDCC" cookies from the Bard website.
4. Insert the cookies into the Python script.
5. Save and execute the script to start querying Bard effortlessly.

## Dependencies

- [Bard API](https://bard.google.com/)
- [Pyperclip](https://pypi.org/project/pyperclip/)
- [Plyer](https://pypi.org/project/plyer/)

## How to Install

### Step 1: Install Python
If Python is not installed on your system, download it from the [official Python website](https://www.python.org/downloads/).

### Step 2: Install Required Libraries
Open your command prompt or terminal and use pip to install the necessary libraries:

```bash
pip install bardapi
pip install pyperclip
pip install plyer
```
### Step 3: Set Up Tkinter
Tkinter is a standard Python library for creating graphical user interfaces and usually comes with Python, so no separate installation is needed.

### Step 4: Get Your "__Secure-1PSID" and "__Secure-1PSIDCC" from Bard Website

    Visit the Bard website and log in with your account.
    Open the developer tools (usually by pressing F12 or right-clicking and selecting "Inspect").
    Go to the "Storage" tab in the developer tools.
    Under "Cookies," find "__Secure-1PSID" and "__Secure-1PSIDCC" cookies. Copy their values.

![1](https://github.com/Mrx-Sachin/localgpt/assets/112502093/31bfdc6d-fba2-4109-85f8-85abef4561f0)
![2](https://github.com/Mrx-Sachin/localgpt/assets/112502093/b64ec8bf-1330-4a3a-aa69-39205acae17d)


### Step 5: Insert Your Cookies into the Code

Edit your Python script and replace the placeholders with the actual values of "__Secure-1PSID" and "__Secure-1PSIDCC" that you copied from the Bard website.

```
"__Secure-1PSID": "<YOUR_ACTUAL_SECURE_1PSID_VALUE>",
"__Secure-1PSIDCC": "<YOUR_ACTUAL_SECURE_1PSIDCC_VALUE>",
```

### Step 6: Save Your Code

After making these changes, save your Python script.

### Step 7: Execute Your Code

Run your Python script. If everything is set up correctly, it should interact with Bard's services and provide the described functionality.


Feel free to contribute, report issues, or suggest improvements to enhance the functionality of this local GPT.

