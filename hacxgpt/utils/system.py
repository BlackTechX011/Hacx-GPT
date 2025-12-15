
import sys
import subprocess
import time
import os

def check_dependencies():
    """Checks and auto-installs missing dependencies."""
    required_packages = [
        ("openai", "openai"),
        ("colorama", "colorama"),
        ("pwinput", "pwinput"),
        ("dotenv", "python-dotenv"),
        ("rich", "rich"),
        ("pyperclip", "pyperclip")
    ]
    
    missing_pip_names = []
    
    for import_name, pip_name in required_packages:
        try:
            __import__(import_name)
        except ImportError:
            missing_pip_names.append(pip_name)
            
    if missing_pip_names:
        print(f"[\033[93m!\033[0m] Missing dependencies: {', '.join(missing_pip_names)}")
        print("[\033[96m*\033[0m] Installing automatically...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", *missing_pip_names])
            print("[\033[92m+\033[0m] Installation complete. Restarting script...")
            time.sleep(1)
            # Re-execute the script
            os.execv(sys.executable, ['python'] + sys.argv)
        except Exception as e:
            print(f"[\033[91m-\033[0m] Failed to install dependencies: {e}")
            print("Please manually run: pip install " + " ".join(missing_pip_names))
            sys.exit(1)
