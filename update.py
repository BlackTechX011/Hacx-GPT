import os
import requests

print(f"""\033[0m

__________.__                 __   ___________           .__    ____  ___
\______   \  | _____    ____ |  | _\__    ___/___   ____ |  |__ \   \/  /
 |    |  _/  | \__  \ _/ ___\|  |/ / |    |_/ __ \_/ ___\|  |  \ \     / 
 |    |   \  |__/ __ \\  \___|    <  |    |\  ___/\  \___|   Y  \/     \ 
 |______  /____(____  /\___  >__|_ \ |____| \___  >\___  >___|  /___/\  \ 
        \/          \/     \/     \/            \/     \/     \/      \_/
                                                                                                                                                    

    """)

def fetch_latest_file(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, "w") as file:
            file.write(response.text)
        print(f"{filename} updated successfully.")
    else:
        print(f"Failed to fetch the latest version of {filename}")

if __name__ == "__main__":
    # Update main.py
    main_url = "https://raw.githubusercontent.com/BlackTechX011/Hacx-GPT/main/main.py"
    fetch_latest_file(main_url, "main.py")

    # Update setup.py
    setup_url = "https://raw.githubusercontent.com/BlackTechX011/Hacx-GPT/main/setup.py"
    fetch_latest_file(setup_url, "setup.py")

    # Exit after updating
    exit()
