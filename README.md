# Searcher Bot
This bot help you to **search** things in **wikis of games** like Stardew Valley, Terraria or in Google directly from your Discord server.

## 🧾 Table of Contents 🧾

1. [Usage](#-usage-)
1. [Example](#-example-)
1. [Searchers](#-example-)
1. [Deployment](#-deployment-)
1. [Setup](#-setup-)
1. [Prerequisites](#-prerequisites-)

## 🔥 Usage 🔥
- **Google** 
    - \_google (what you want to search)
- **Stardew Valley** 
    - \_stardew (what you want to search) [show 1-5 result] 
- **Terraria** 
    - \_terraria (what you want to search)
## 🎈 Example 🎈
Example **discord message**:

```
_google discord bot
```

Example **response**:
    
![image](https://user-images.githubusercontent.com/38699812/87507451-0784d900-c633-11ea-89fa-0def9a651c0b.PNG)

## 🔎 Searchers 🔎
- **Google** 
  - \_google
- **Stardew Valley** 
  - \_stardew
  - \_valley
  - \_stardewv
  - \_stardewvalley
- **Terraria** 
  - \_terraria


## 🌟 Deployment 🌟
To start the Discord bot run:
```cmd
python3 main.py
```

## 🔨 Setup 🔨
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

## 💡 Prerequisites 💡
- [Python 3.5](https://www.python.org/downloads/) or newer version.
- [pip](https://pip.pypa.io/en/stable/) package manager.
- [Google Chrome](https://www.google.com/intl/es_mx/chrome/) installed.
- [Chrome Webdriver](https://chromedriver.chromium.org/downloads) file.
- Discord Application bot [token](https://discord.com/developers/applications/)

![Token](https://user-images.githubusercontent.com/38699812/87493279-0e4f2400-c612-11ea-8a63-f19f867f8810.png)

