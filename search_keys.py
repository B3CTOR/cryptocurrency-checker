import argparse

def parse_crypto(): #This function parses the cryptocurrency that I want to scrape.
	parser = argparse.ArgumentParser(description = '''
		Parse a cryptocurrency
		''')
	parser.add_argument('-c', '--crypto', type = str, metavar = '', required = True,
		help = '''
		Enter a cryptocurrency to parse
		''')
	parser.add_argument('-q', '--quiet', required = False, action = 'store_true',
		help = '''
		Print only data
		''')

	return (parser.parse_args())