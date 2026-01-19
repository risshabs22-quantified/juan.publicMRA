# juan.publicMRA
# 🏆 Microsoft Rewards Automation Bot

An automated Python bot that earns Microsoft Rewards points by performing Bing searches, completing daily sets, quizzes, polls, and other activities.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Selenium](https://img.shields.io/badge/Selenium-4.10+-green.svg)
![Edge](https://img.shields.io/badge/Browser-Edge-blue.svg)

---

## ⚠️ Disclaimer

> **Use at your own risk!** This bot may violate Microsoft's Terms of Service. Automated reward earning could result in account suspension or banning.

---

## ✨ Features

- 🔍 **Automated Bing Searches** - PC (34) and Mobile (24) searches
- 📋 **Daily Set Completion** - Auto-completes daily activities
- 🎯 **More Activities** - Processes additional reward tasks
- 🎫 **Punch Cards** - Completes bonus punch card tasks
- 🧠 **Quiz & Poll Handling** - Answers quizzes and polls automatically
- 🛡️ **Anti-Detection** - Human-like typing, random delays, stealth mode

---

## 📁 Project Structure

```
MSRewardsBot/
├── main.py                 # Entry point - run this!
├── config.example.json     # Template config (copy to config.json)
├── requirements.txt        # Python dependencies
├── .gitignore              # Git ignore rules
├── README.md               # This file
└── src/                    # Source modules
    ├── __init__.py
    ├── auth.py             # Microsoft login
    ├── browser.py          # Edge browser setup
    ├── searches.py         # Bing search automation
    ├── rewards.py          # Dashboard task automation
    └── utils.py            # Utilities & logging
```

---

## 🚀 Quick Start

### Prerequisites

- **Python 3.8+**
- **Microsoft Edge** browser
- **Microsoft account** enrolled in [Microsoft Rewards](https://rewards.bing.com/)

### Installation

```bash
# 1. Clone/download the project
cd MSRewardsBot

# 2. Install dependencies
pip install -r requirements.txt

# 3. Create your config file
copy config.example.json config.json    # Windows
# cp config.example.json config.json    # Mac/Linux

# 4. Edit config.json with your credentials
# (see Configuration section below)

# 5. Run the bot
python main.py
```

---

## ⚙️ Configuration

Edit `config.json` with your settings:

```json
{
    "email": "your-email@outlook.com",
    "password": "your-password",
    "headless": false,
    "pc_searches": 34,
    "mobile_searches": 24,
    "min_delay": 3,
    "max_delay": 8
}
```

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `email` | string | - | Your Microsoft account email |
| `password` | string | - | Your Microsoft account password |
| `headless` | boolean | `false` | Run browser invisibly |
| `pc_searches` | integer | `34` | Desktop searches to perform |
| `mobile_searches` | integer | `24` | Mobile searches to perform |
| `min_delay` | float | `3` | Min delay between searches (sec) |
| `max_delay` | float | `8` | Max delay between searches (sec) |

---

## 🔄 What It Does

```
1. 🖥️  DESKTOP SESSION
   ├── Login to Microsoft account
   ├── Record starting points
   ├── Perform 34 PC Bing searches
   ├── Complete Daily Set activities
   ├── Complete More Activities
   └── Complete Punch Cards

2. 📱 MOBILE SESSION
   ├── Login (mobile emulation)
   └── Perform 24 mobile Bing searches

3. 📊 SUMMARY
   └── Display points earned
```

---

## 🔧 Troubleshooting

| Issue | Solution |
|-------|----------|
| Login fails | Check credentials in config.json |
| 2FA required | Complete 2FA manually in browser window |
| Edge not found | Install Microsoft Edge browser |
| Points not earned | Account may be flagged; increase delays |

---

## 📈 Expected Points

| Activity | Points | Frequency |
|----------|--------|-----------|
| PC Searches | ~150 | Daily |
| Mobile Searches | ~100 | Daily |
| Daily Set | ~30-60 | Daily |
| More Activities | Varies | Daily |

**Total potential:** ~250-350+ points/day

---

## 🔒 Security

- ⚠️ **Never share your `config.json`** - it contains your credentials
- ✅ `config.json` is automatically excluded from git via `.gitignore`
- 💡 Consider using a secondary account

---

## 📋 Requirements

- `selenium>=4.10.0` - Browser automation
- `webdriver-manager>=4.0.0` - Auto driver management
- `fake-useragent>=1.4.0` - User agent generation

---

## 📄 License

Educational purposes only. Use responsibly and at your own risk.

---

<div align="center">

**⭐ Star this repo if it helped you! ⭐**

Made with ❤️ for the Microsoft Rewards community

</div>
