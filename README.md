
***

<div align="center">

  <a href="https://github.com/BlackTechX011/Hacx-GPT">
    <img src="https://github.com/BlackTechX011/Hacx-GPT/blob/main/img/HacxGPT.png" alt="Hacx GPT Logo" width="250" />
  </a>

  # HacxGPT

  <p>
    <strong>An advanced AI framework inspired by WormGPT, engineered to explore the frontiers of language model interactions.</strong>
  </p>
  
  <!-- Badges -->
  <p>
    <a href="https://github.com/BlackTechX011/Hacx-GPT" title="View on GitHub"><img src="https://img.shields.io/static/v1?label=BlackTechX&message=Hacx-GPT&color=blue&logo=github" alt="BlackTechX - Hacx-GPT"></a>
    <a href="https://github.com/BlackTechX011/Hacx-GPT/stargazers"><img src="https://img.shields.io/github/stars/BlackTechX011/Hacx-GPT?style=social" alt="GitHub Stars"></a>
    <a href="https://github.com/BlackTechX011/Hacx-GPT/network/members"><img src="https://img.shields.io/github/forks/BlackTechX011/Hacx-GPT?style=social" alt="GitHub Forks"></a>
    <br>
    <img src="https://img.shields.io/github/last-commit/BlackTechX011/Hacx-GPT?color=green&logo=github" alt="Last Commit">
    <img src="https://img.shields.io/github/license/BlackTechX011/Hacx-GPT?color=red" alt="License">
  </p>
   
  <h4>
    <a href="https://github.com/BlackTechX011/">GitHub</a>
    <span> · </span>
    <a href="https://www.instagram.com/BlackTechX011/">Instagram</a>
    <span> · </span>
    <a href="https://x.com/BlackTechX011">X (Twitter)</a>
    <span> · </span>
    <a href="https://www.youtube.com/@BlackTechX_">YouTube</a>
  </h4>
</div>

---

## 🚀 Showcase

Here is a glimpse of the HacxGPT framework in action.

![HacxGPT Demo Screenshot](https://github.com/BlackTechX011/Hacx-GPT/blob/main/img/home.png)



---

## :notebook_with_decorative_cover: Table of Contents

- [About The Project](#star2-about-the-project)
  - [What is this Repository?](#grey_question-what-is-this-repository)
  - [The Real HacxGPT: Our Private Model](#gem-the-real-hacxgpt-our-private-model)
- [Features](#dart-features)
- [Getting Started](#electric_plug-getting-started)
  - [Prerequisites: API Key](#key-prerequisites-api-key)
  - [Installation](#gear-installation)
- [Configuration](#wrench-configuration)
- [Usage](#eyes-usage)
- [Contributing](#wave-contributing)
- [License](#warning-license)

---

## :star2: About The Project

HacxGPT is designed to provide powerful, unrestricted, and seamless AI-driven conversations, pushing the boundaries of what is possible with natural language processing.

### :grey_question: What is this Repository?

This repository contains an open-source framework that demonstrates the *concept* of HacxGPT. It utilizes external, third-party APIs from providers like **OpenRouter** or **DeepSeek** and combines them with a specialized system prompt. This allows a standard Large Language Model (LLM) to behave in a manner similar to our private HacxGPT, offering a preview of its capabilities.

**It is important to understand:** This code is a wrapper and a proof-of-concept, not the core, fine-tuned HacxGPT model itself.

### :gem: The Real HacxGPT: Our Private Model

While this repository offers a glimpse into HacxGPT's potential, our flagship offering is a **privately-developed, fine-tuned Large Language Model.**

Why choose our private model?
- **Ground-Up Development:** We've trained our model using advanced techniques similar to the DeepSeek methodology, focusing on pre-training, Supervised Fine-Tuning (SFT), and Reinforcement Learning (RL).
- **Superior Performance:** The private model is significantly more intelligent, coherent, and capable than what can be achieved with a simple system prompt on a public API.
- **Enhanced Security & Privacy:** Offered as a private, managed service to ensure security and prevent misuse.
- **True Unrestricted Power:** Built from the core to handle a wider and more complex range of tasks without the limitations of public models.

#### How to Access the Private Model

Access to our private model is exclusive. To inquire about services and pricing, please contact our team via Telegram.

➡️ **Join our Telegram Channel for more info:** [https://t.me/HacxGPT](https://t.me/HacxGPT)

---

## :dart: Features

- **Powerful AI Conversations:** Get intelligent and context-aware answers to your queries.
- **Unrestricted Framework:** A system prompt designed to bypass conventional AI limitations.
- **Easy-to-Use CLI:** A clean and simple command-line interface for smooth interaction.
- **Cross-Platform:** Tested and working on Kali Linux, Ubuntu, and Termux.

---

## :electric_plug: Getting Started

Follow these steps to get the HacxGPT framework running on your system.

### :key: Prerequisites: API Key

To use this framework, you **must** obtain an API key from a supported provider. These services offer free tiers that are perfect for getting started.

1.  **Choose a provider:**
    *   **OpenRouter:** Visit [OpenRouter.ai](https://openrouter.ai/keys) to get a free API key. They provide access to a variety of models.
    *   **DeepSeek:** Visit the [DeepSeek Platform](https://platform.deepseek.com/api_keys) for a free API key to use their powerful models.

2.  **Copy your API key.** You will need to paste it into the script when prompted during the first run.

### :gear: Installation

We provide simple, one-command installation scripts for your convenience.

#### **Windows**
1. Download the `install.bat` script from this repository.
2. Double-click the file to run it. It will automatically clone the repository and install all dependencies.

#### **Linux / Termux**
1. Open your terminal.
2. Run the following command. It will download the installer, make it executable, and run it for you.
   ```bash
   bash <(curl -s https://raw.githubusercontent.com/BlackTechX011/Hacx-GPT/main/install.sh)
   ```

<details>
<summary>Manual Installation (Alternative)</summary>

If you prefer to install manually, follow these steps.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/BlackTechX011/Hacx-GPT.git
    ```
2.  **Navigate to the directory:**
    ```bash
    cd Hacx-GPT
    ```
3.  **Install Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
</details>

---

## :wrench: Configuration

You can easily switch between API providers.

1.  Open the `HacxGPT.py` file in a text editor.
2.  Locate the `API_PROVIDER` variable at the top of the file.
3.  Change the value to either `"openrouter"` or `"deepseek"`.

    ```python
    # HacxGPT.py

    # Change this value to "deepseek" or "openrouter"
    API_PROVIDER = "openrouter" 
    ```
4. Save the file. The script will now use the selected provider's API.

---

## :eyes: Usage

Once installation and configuration are complete, run the application with this simple command:

```bash
python3 HacxGPT.py
```

The first time you run it, you will be prompted to enter your API key. It will be saved locally for future sessions.

---

## :star: Star History

[![Star History Chart](https://api.star-history.com/svg?repos=BlackTechX011/Hacx-GPT&type=Date)](https://star-history.com/#BlackTechX011/Hacx-GPT&Date)


---

## :wave: Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

<a href="https://github.com/BlackTechX011/Hacx-GPT/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=BlackTechX011/Hacx-GPT" />
</a>

---

## :warning: License

Distributed under the Personal-Use Only License (PUOL) 1.0. See `LICENSE.txt` for more information.

***
