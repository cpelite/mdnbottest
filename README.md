A simple bot for usage in the german virtual nations / micronations.

Required Packages:

    discord.py
    os
    dotenv

Step 1 - Installation of Python (for Ubuntu, Debian, and Derivates)

    sudo apt update
    sudo apt install software-properties-common
    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt install python3.9

Step 2 - Install Pip

    sudo apt install python3-pip

Step 3 - Create a VENV (Virtual Environment)

    sudo apt install python3-venv
    python3 -m venv my-project-env
    source my-project-env/bin/activate

Step 4 - Install required libraries (from within the venv)

    pip install -r requirements.txt

Step 5 - create a .env-file

    nano .env
Step 6 - Add your Token to the .env file in nano

    DISCORD_TOKEN=YOUR_TOKEN_HERE

Step 7 - Start the bot

    python3 mdnbot.py

Additional: Step 8 - Use Nohup to keep bot running
    
    nohup python3 mdnbot.py