from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver


def scrape_data(driver): #This function scrapes the cryptocurrency information.


	WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')))
	act_cookies = driver.find_element_by_xpath('//*[@id="onetrust-accept-btn-handler"]').click()

	WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'last_last')))
	price = driver.find_element_by_id('last_last')

	WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="fullColumn"]/div[6]/div[1]/div[1]/div[2]/span[4]')))
	indecrease = driver.find_element_by_xpath('//*[@id="fullColumn"]/div[6]/div[1]/div[1]/div[2]/span[4]')

	return price.text, indecrease.text