#Pet project Movie Telegram Bot

- [ABOUT THE PROJECT](#about-the-project)
- [INSTALLATION](#installation)
- [SUPPORT RESOURCES](#support-resources)
- [RUN](#run)

## ABOUT THE PROJECT
___
Telegram bot designed to parse a popular resource with online movies.

At a given time interval, the bot checks for new movies. If a new movie is published on the resource, the bot gets a link to the movie and publishes it in the telegram channel

## INSTALLATION
___

The bot can be deployed on the server in the usual way and also through Docker(the manual is under development)

## SUPPORT RESOURCES
___
* Selenium
* Beautiful Soup
* Requests

Requires [chromedriver](https://chromedriver.storage.googleapis.com/index.html)

The versions of the driver and the installed browser must match.
The path to the driver must be written in the Movie class (models.movie_link)

## RUN
___
* The .env.dist file needs to be renamed to .env
* In the .env file, you must specify your Telegram ID, Bot Token and database access
* In the config.py file, you must specify the channel ID where posts will be sent
* The bot is launched through the launch of the app.py file
