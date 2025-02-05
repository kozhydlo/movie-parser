# Telegram Movie Bot

This repository contains a Telegram bot that interacts with users and retrieves movie information from a database and a website. It also includes a script for scraping movie data and storing it in an SQLite database.

## Repository Structure

### `bot.py`
This file contains the code for the Telegram bot, handling user interactions and executing queries to retrieve movie information.

#### Telegram Bot Features:
- Initializes and configures the Telegram bot.
- Handles the `/start` command and user messages.
- Provides options for movie search and processes user queries.
- Uses Selenium to fetch additional movie details.

#### Database Interaction:
- Connects to an SQLite database (`KINO3.db`) to retrieve movie data.
- Supports random movie selection and search by title or description.
- Uses `text.txt` to store and display search results.

### `main.py`
This script scrapes movie information from a website and stores it in an SQLite database.

#### Data Collection:
- Uses BeautifulSoup to parse HTML from [uakino.club](https://uakino.club) and extract movie titles, quality, links, and descriptions.
- Randomly selects a User-Agent to prevent bot detection.
- Stores the retrieved data in an SQLite database (`Triangle_kino.db`).
- Iterates through pages to collect movie data continuously.

#### Database Structure:
- Creates and updates the `Triangle_kino` table with the collected movie data.

## Requirements

### Python:
- The code is written in Python and requires version 3.x.

### Dependencies:
Ensure all required libraries are installed using:
```bash
pip install -r requirements.txt
```

### SQLite:
- SQLite must be installed for database operations.

## Usage

### Running the Telegram Bot:
Start the bot with:
```bash
python bot.py
```
- Use the `/start` command to initialize the bot and choose search options.

### Running the Scraper:
Execute the scraper with:
```bash
python main.py
```
- The script collects movie information and stores it in the database.
- Request intervals and other parameters can be adjusted in the script.

### Additional Configuration:
- Ensure you have the necessary API tokens configured for the Telegram bot.

---
Developed for automating movie search and data collection from online sources.
