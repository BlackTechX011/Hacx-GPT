#!/bin/bash

# HacxGPT Installer for Linux and Termux
# https://github.com/BlackTechX011/Hacx-GPT

echo "======================================"
echo "    HacxGPT Installer Script"
echo "======================================"

# Function to detect package manager
detect_pkg_manager() {
    if command -v apt-get &> /dev/null; then
        echo "apt"
    elif command -v pkg &> /dev/null; then
        echo "pkg"
    else
        echo "unknown"
    fi
}

PKG_MANAGER=$(detect_pkg_manager)

# Update and install dependencies
echo "[+] Updating package lists..."
if [ "$PKG_MANAGER" = "apt" ]; then
    sudo apt-get update -y
    echo "[+] Installing git, python, and pip..."
    sudo apt-get install git python3 python3-pip -y
elif [ "$PKG_MANAGER" = "pkg" ]; then
    pkg update -y
    echo "[+] Installing git and python..."
    pkg install git python -y
else
    echo "[!] Unsupported package manager. Please install git, python3, and pip manually."
    exit 1
fi

# Clone the repository
if [ -d "Hacx-GPT" ]; then
    echo "[!] Hacx-GPT directory already exists. Skipping clone."
else
    echo "[+] Cloning Hacx-GPT repository..."
    git clone https://github.com/BlackTechX011/Hacx-GPT.git
fi

cd Hacx-GPT

# Install Python requirements
echo "[+] Installing required python packages..."
if command -v pip3 &> /dev/null; then
    pip3 install -r requirements.txt
else
    pip install -r requirements.txt
fi

echo ""
echo "======================================"
echo "      Installation Complete!"
echo "======================================"
echo "To run HacxGPT:"
echo "1. cd Hacx-GPT"
echo "2. python3 HacxGPT.py"
echo ""
echo "Don't forget to get your API key from OpenRouter or DeepSeek!"
echo "======================================"
