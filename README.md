# The Mungbean Assistant

## Idea
Build text bot that when you text it it will return specific material. It will also send automated texts to you!

## User Text Commands
1. Weather
   * WEATHER 
   * WEATHER 10DAY
   * WEATHER TODAY
   * WEATHER TOMORROW
2. Poems
   * POEM
3. Words of Affirmation
   * AFFIRMATION
4. Top news headlines with links to NY Times
   * NEWS
5. Phish (sends random jam as audio or link to phish.in)
   * PHISH
   * PHISH YEAR
   * PHISH PHOTO
6. Reminders
   * SET REMINDER
7. Scraping
   1. COVID TIMES (messages you when new rapid test times are available)

## Technology
* Server - Raspberry Pi
* Automation - Jenkins
* Github actions (Black and MyPy) for code reinforcement
* Docker
* Orchestration - Airflow
* Telegram (API)
  * [Link to bots info](https://core.telegram.org/bots)


## To use the bot
1. Download [Telegram](https://telegram.org/)
2. Under chats, search for `@mungbean_bot` and hit Start