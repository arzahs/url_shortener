# coding: utf-8

DATA_FILE = 'data.txt'
DATA_ENCODING = 'utf-8'


def load_data_():
	with open(DATA_FILE, 'r', encoding=DATA_ENCODING) as data_file:
		return eval(data_file.read())

def save_data():
	with open(DATA_FILE, 'w', encoding=DATA_ENCODING) as data_file:
		print(repr(urls_), file=data_file)

urls_ = load_data_()

def get_url(short_url):
	for url in urls_:
		if url.get('Short') == short_url:
			return str(url.get('Long'))


def add_url(url):
	urls_.append(url)
	save_data()