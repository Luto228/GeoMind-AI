# 🌍 GeoMind-AI

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Aiogram](https://img.shields.io/badge/Aiogram-3.x-orange.svg)](https://docs.aiogram.dev/)

**GeoMind-AI** is a high-performance Telegram bot powered by `aiogram` and `aiohttp`. It intelligently fetches and displays comprehensive data about any country on Earth, including its flag, population, capital city, and real-time weather conditions.

---

## 🚀 Features

- 📍 **Country Insight:** Instantly retrieve population and general info for any country.
- 🌡️ **Live Weather:** Get current temperature and weather descriptions for capital cities.
- ⚡ **Asynchronous:** Built with `asyncio` and `aiohttp` for lightning-fast responses.
- 🎨 **Visuals:** Displays country flags right in the chat.

---

## 🛠️ Installation

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/YourUsername/GeoMind-AI.git
    cd GeoMind-AI
    ```

2.  **Install Dependencies:**
    ```bash
    pip install aiogram aiohttp
    ```

3.  **Configure the Bot:**
    You need to set up your API keys in the configuration file.

    - Copy the example configuration:
      ```bash
      cp config.py.example config.py
      ```
    - Open `config.py` and fill in your credentials:
      ```python
      TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
      WeatherToken = 'YOUR_OPENWEATHER_API_KEY'
      ```

---

## 🔑 Obtaining API Keys

### 1. Telegram Bot Token
- Message [@BotFather](https://t.me/botfather) on Telegram.
- Use `/newbot` to create your bot and receive the `TOKEN`.

### 2. Weather API (OpenWeatherMap)
- **IMPORTANT:** GeoMind-AI requires a weather API key to function.
- Create a free account at [OpenWeatherMap](https://openweathermap.org/api).
- Generate an API key (AppID) and paste it into `WeatherToken` in your `config.py`.

---

## 🏃 Usage

Start the bot:
```bash
python bot.py
```

### Commands:
- `/start` - Get a welcoming message and instructions.
- `/info [country]` - Fetch details and weather for the specified country.
  - *Example:* `/info Japan`

---