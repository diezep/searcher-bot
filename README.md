# Searcher Bot
This bot help you to **search** things in **wikis of games** like Stardew Valley, Terraria or in Google directly from your Discord server.

<!--
## 🧾 - Table of Contents
1. [Prerequisites](#prerequisites)
1. [General expectations of a README file](#general-expectations-of-a-README)
1. [Usual Sections and Inspirations](#usual-sections-and-inspirations)
1. [References and other resources](#references-and-other-resources)
1. [Useful Tools](#useful-tools)
1. [Credits](#credits)
1. [Contribute](#contribute)
-->

## 🛠 - Prerequisites
- [Python 3.5](https://www.python.org/downloads/) or newer version.
- [pip](https://pip.pypa.io/en/stable/) package manager.
- [Google Chrome](https://www.google.com/intl/es_mx/chrome/) installed.
- [Chrome Webdriver](https://chromedriver.chromium.org/downloads) file.
- Discord Application bot [token](https://discord.com/developers/applications/)
    ![Token](https://user-images.githubusercontent.com/38699812/87493279-0e4f2400-c612-11ea-8a63-f19f867f8810.png)

## ⚙ Setup
- Using the package manager [pip](https://pip.pypa.io/en/stable/), install necessary packages running the following command:
    ```cmd
    pip install -r requirements.txt
    ```

- Create .env file with the following variables:
  ```python
  DISCORD_TOKEN = "(Bot token registered in Discord App.)"
  CHROMEDRIVER_PATH = "(PATH of 'webdriver.exe' downloaded)"
  GOOGLE_CHROME_BIN = "(PATH of Google Chrome ['chrome.exe' file])"
    ```
## Deployment
To start the Discord bot run:
```cmd
python3 main.py
```
## Searchers In Development
- Google [_google]
- Stardew Valley [_stardew, _valley, _stardewv, _stardewvalley]
- Terraria [_terraria]
