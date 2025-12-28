
# HacxGPT Internal API

This directory contains the resources and documentation needed to access our specialized, fine-tuned AI models developed exclusively by the HacxGPT team.

> [!NOTE] 
> This API operates differently than standard web APIs. It is hosted on the **I2P (Invisible Internet Project)** network for privacy and security. Follow the setup instructions carefully.

---

## Table of Contents
1. [Prerequisites](#-prerequisites)
2. [Step 1: Setting up the Network (i2a)](#-step-1-setting-up-the-network-i2a)
3. [Step 2: Getting Keys & Model Names](#-step-2-getting-keys--model-names)
4. [Step 3: Usage & Code Examples](#-step-3-usage--code-examples)
5. [Troubleshooting](#-troubleshooting)

---

## 🛠 Prerequisites

Before you begin, make sure you have the following:
*   **Python 3.7+** installed.
*   A **Telegram account** (Required to retrieve keys and model names).
*   **Basic knowledge** of running commands in a terminal.

---

## 🚀 Step 1: Setting up the Network (i2a)

Because our API is hosted on the hidden web (I2P), you cannot connect to it directly over the standard internet. You need a "bridge" or proxy tool called `i2a`.

1.  **Download i2a:**
    Go to the official repository and clone/download the tool:
    [👉 GitHub: BlackTechX011/i2a](https://github.com/BlackTechX011/i2a)

2.  **Run i2a:**
    Open a generic terminal window (Command Prompt, PowerShell, or Bash). Navigate to the folder where you installed `i2a` and run it.

3.  **Wait for Connection:**
    *   Once `i2a` starts, **do not close the window!**
    *   **Important:** Wait a few minutes (usually 2-5 minutes). The tool needs time to find peers and build "tunnels" into the I2P network.
    *   Once it indicates it is connected/ready, leave this terminal running in the background.

---

## 🔑 Step 2: Getting Keys & Model Names

We use a unique authentication system and frequent model updates. You must join our community to get the necessary credentials.

1.  Join the official **HacxGPT Telegram Channel**:
    [👉 t.me/HacxGPT](https://t.me/HacxGPT)
2.  Look for the pinned post. You will find:
    *   The current **Internal Key** (used in the URL).
    *   The list of **Available Model Names** (IDs) to use in your code.

> **⚠️ Security Warning:** Treat your Internal Key like a password. Do not share it publicly. It grants full access to our internal neural links.

---

## 💻 Step 3: Usage & Code Examples

The internal API is compatible with the standard **OpenAI Python SDK**. However, you must configure the `base_url` specifically to route through your local `i2a` proxy.

### Configuration Details
*   **Proxy Address:** `http://127.0.0.1:8790`
*   **Authentication:** The real key goes in the URL.
*   **Header Key:** The standard `api_key` field can be set to any placeholder string (e.g., `"HacxGPT"`).

### Python Example

```python
from openai import OpenAI

# ---------------------------------------------------------
# CONFIGURATION
# ---------------------------------------------------------
# Get these details from the Telegram Channel (t.me/HacxGPT)
INTERNAL_KEY = "PASTE_KEY_FROM_TELEGRAM_HERE"
MODEL_NAME = "PASTE_MODEL_NAME_FROM_TELEGRAM_HERE" 
# ---------------------------------------------------------

# INITIALIZE CLIENT
client = OpenAI(
    # The magic happens here: The key is part of the URL
    base_url=f"http://127.0.0.1:8790/{INTERNAL_KEY}/v1/",
    
    # This is just a placeholder, but it is required by the library
    api_key="HacxGPT"
)

# MAKE A REQUEST
try:
    print(f"Connecting to internal network using model: {MODEL_NAME}...")
    
    response = client.chat.completions.create(
        model=MODEL_NAME,  # Must match a valid ID from Telegram
        messages=[
            {"role": "user", "content": "Hello, are you online?"}
        ]
    )
    print("Response received:")
    print(response.choices[0].message.content)

except Exception as e:
    print(f"Error: {e}")
    print("Tip: Make sure i2a is running in a separate terminal and your Key/Model Name is correct!")
```

---

## ❓ Troubleshooting

**"Connection Refused" or "Target Machine actively refused it"**
*   Is `i2a` running?
*   Did you close the terminal running `i2a`? It must stay open while you run your Python script.

**"Timeout" or Slow Responses**
*   I2P is a decentralized network. It is naturally slower than the normal internet.
*   If `i2a` was just started, wait 5 more minutes for the tunnels to stabilize and try again.

**"Model not found" or Authentication Error**
*   Check the **Telegram Channel** for the most recent Key and Model ID. These may change periodically for security or updates.

---

**Happy Hacking!** 🕵️‍♂️
*The HacxGPT Team*