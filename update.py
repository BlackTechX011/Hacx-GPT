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
def fetch_latest_main():
    url = "https://raw.githubusercontent.com/BlackTechX011/Hacx-GPT/main/main.py"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print("Failed to fetch the latest version of main.py")
        return None

def update_main(content):
    with open("main.py", "w") as file:
        file.write(content)
    print("main.py updated successfully.")

if __name__ == "__main__":
    latest_main_content = fetch_latest_main()
    if latest_main_content:
        update_main(latest_main_content)
    else:
        print("Exiting due to failure in fetching the latest version of main.py")
    # Exit after updating
    exit()
