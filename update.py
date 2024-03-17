import os
import sys
import requests
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

def fetch_latest_file(url, filename):
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(filename, "w") as file:
            file.write(response.text)
        logging.info(f"\033[92mSuccessfully updated {filename}\033[0m")
    except requests.RequestException as e:
        logging.error(f"\033[91mFailed to update {filename}: {e}\033[0m")
        sys.exit(1)

def update_main():
    main_url = "https://raw.githubusercontent.com/BlackTechX011/Hacx-GPT/main/main.py"
    fetch_latest_file(main_url, "main_updated.py")
    os.replace("main_updated.py", "main.py")

if __name__ == "__main__":
    print("\033[0m")
    print("\033[92m")
    print("""\033[0m

__________.__                 __   ___________           .__    ____  ___
\______   \  | _____    ____ |  | _\__    ___/___   ____ |  |__ \   \/  /
 |    |  _/  | \__  \ _/ ___\|  |/ / |    |_/ __ \_/ ___\|  |  \ \     / 
 |    |   \  |__/ __ \\  \___|    <  |    |\  ___/\  \___|   Y  \/     \ 
 |______  /____(____  /\___  >__|_ \ |____| \___  >\___  >___|  /___/\  \ 
        \/          \/     \/     \/            \/     \/     \/      \_/
                                                                                                                                                    

    """)
    logging.info("Starting update process...")
    update_main()
    logging.info("Update process completed successfully.")
