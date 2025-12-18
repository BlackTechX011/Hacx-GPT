from setuptools import setup, find_packages

setup(
    name="hacxgpt",
    version="2.0.0",
    description="Advanced Uncensored AI Terminal Interface",
    author="BlackTechX",
    packages=find_packages(),
    install_requires=[
        "openai",
        "rich",
        "python-dotenv",
        "pwinput",
        "pyperclip",
        "colorama",
        "prompt_toolkit"
    ],
    entry_points={
        "console_scripts": [
            "hacxgpt=hacxgpt.main:main",
        ],
    },
    python_requires=">=3.8",
)

