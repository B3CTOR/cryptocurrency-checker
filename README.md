## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info

This is a program which scrapes data of a specific cryptocurrency from https://es.investing.com (https://es.investing.com/crypto/your_cryptocurrency) and shows a desktop notification with the data. It is programmed in Python 3.9.

The information that is scraped is the actual value of the cryptocurrency and its variation. Then it shows a desktop notification with this information. Feel free to make any changes in the code and distribute it.

Note: You should change the URL according to your country, in this case I used Investing ES (Spain). To change it go to the main.py file in the 12 line:
```
crypto_url = 'https://es.investing.com/crypto/{}'.format(args.crypto.lower())
```

## Technologies

To execute the code you'll need the following packages:

- Selenium 3.141.0

```
$ pip install selenium
```
Selenium is used in this program to go to the URL and scrape the information.

- Argparse 1.4.0

```
$ pip install argparser
```
Argparser is used to parse the cryptocurrency you want to scrape.

- Plyer 2.0.0

```
$ pip install plyer
```
Plyer is used to show the notification.

## Setup

To execute this program go to your console and type the following line:
```
$ python main.py -c your_cryptocurrency
```
You can also type the following line to show only the cryptocurrency data without any other text:
```
$ python main.py -c your_cryptocurrency -q
```

