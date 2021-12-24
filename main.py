from urllib.request import *
from bs4 import *

URL = ""

class Scraper():
	def __init__(self):
		self.url_link = Request(URL, headers = {"User-Agent" : "Chrome"})
		self.url_page = urlopen(self.url_link).read()
		self.soup = BeautifulSoup(self.url_page, 'html.parser')
		self.raw = self.soup.find_all('td', 'table-light')
		self.problems = {'ALL':{}}
		self.olympiads = ['ALL', 'IOI', 'APIO', 'BOI', 'INFO(1)', 'IZHO', 'JOI', 'JOIOC', 'JOISC', 'POI', 'USACO']

	def run(self, src):
		if (src not in self.olympiads):
			print("Enter valid source")
			return

		for i in self.raw:
			if ('data-content' not in i.attrs):
				continue
			acs = i['data-content'].replace	('<b>', '').replace('</b>', '').replace('<br/>', '').split(': ')
			name = i['data-title']
			comp = i['data-title'].split(' ')[0]

			if (comp not in self.problems):
				self.problems[comp] = {}

			if (len(acs) == 1):
				self.problems['ALL'][name] = -1
				self.problems[comp][name] = -1
			else:
				self.problems['ALL'][name] = int(acs[1][:-13])
				self.problems[comp][name] = int(acs[1][:-13])

		for k, v in dict(sorted(self.problems[src].items(), key = lambda item: item[1], reverse = 1)).items():
			print(k, v)

if '__main__' == __name__:
	URL = "https://" + input("OI Checklist URL: ")
	src = input("Source: (all, IOI, APIO, BOI, InfO(1), IZHO, JOI, JOIOC, JOISC, POI, USACO): ").upper()
	app = Scraper()
	app.run(src) 