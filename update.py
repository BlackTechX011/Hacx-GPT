import os
import requests

def fetch_latest_file(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, "w") as file:
            file.write(response.text)
        print(f"{filename} updated successfully.")
    else:
        print(f"Failed to fetch the latest version of {filename}")

if __name__ == "__main__":
 
    main_url = "https://raw.githubusercontent.com/BlackTechX011/Hacx-GPT/main/main.py"
    fetch_latest_file(main_url, "main_updated.py")

    os.replace("Hacx GPT V3", "main.py")
