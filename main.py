from search_keys import parse_crypto
from scraper import scrape_data
import time
from selenium import webdriver
import sys
from plyer import notification
import datetime


if __name__ == '__main__': #Here I get the cryptocurrency whit 'parse_crypto()' and then I initialize the webdriver.
	args = parse_crypto()
	crypto_url = 'https://es.investing.com/crypto/{}'.format(args.crypto.lower())
	driver = webdriver.Chrome(r'C:\chromedriver.exe')
	driver.get(crypto_url)
	driver.minimize_window()


	try:
		price_crypto, indecrease_crypto = scrape_data(driver) #Here I get the scraped data.
	except:
		print('An error has occurred, please introduce a valid cryptocurrency.')
		sys.exit()

	if args.quiet: #Here I show the notification with all the scraped information and the actual date.
		notification.notify(
			title = 'Cryptocurrency checker on {}'.format(datetime.date.today()),
			message = '{}, {}$, {}'.format(args.crypto.capitalize(), price_crypto, indecrease_crypto),
			app_icon = 'favicon.ico')

	else:
		notification.notify(
			title = 'Cryptocurrency checker.',
			message = 'The price of {} is {}$.\nWith a variation of {}.'.format(args.crypto.capitalize(), price_crypto, indecrease_crypto),
			app_icon = 'favicon.ico')



	time.sleep(10)
	driver.close()