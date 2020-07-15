# Searcher Bot
This bot help you to **search** things in **wikis of games** like Stardew Valley, Terraria or in Google directly from your Discord server.

## 🧾 - Table of Contents
1. [Searchers Working](#---searchers-working)
1. [Prerequisites](#---prerequisites)
1. [Setup](#---setup)
1. [Deployment](#---deployment)

## 🔥 - Searchers Working
- **Google** \[_google]
- **Stardew Valley** \[_stardew, _valley, _stardewv, _stardewvalley]
- **Terraria** \[_terraria]

## 🛠 - Prerequisites
- [Python 3.5](https://www.python.org/downloads/) or newer version.
- [pip](https://pip.pypa.io/en/stable/) package manager.
- [Google Chrome](https://www.google.com/intl/es_mx/chrome/) installed.
- [Chrome Webdriver](https://chromedriver.chromium.org/downloads) file.
- Discord Application bot [token](https://discord.com/developers/applications/)
    ![Token](https://user-images.githubusercontent.com/38699812/87493279-0e4f2400-c612-11ea-8a63-f19f867f8810.png)

## ⚙ - Setup
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
## 🌟 - Deployment
To start the Discord bot run:
```cmd
python3 main.py
```
