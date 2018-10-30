# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import json
import os

class Like_Serial_Ua(object):
	'''класс сериала з uaSerials.pro'''
	url = None
	html = None
	list_infa = None
	imagename = None
	def __init__(self, url):
		super(Like_Serial_Ua, self).__init__()
		self.url = url
		self.setHtml()
		self.parser()

		self.filename = "cookie/"+self.url.split("uaserials.pro/")[1].split(".html")[0]+".json"
		self.imagename = "cookie/images/"+self.list_infa["img"]["src"].split("/")[-1]
		self.list_infa["img"]["src"] = self.imagename
		if not os.path.exists(self.filename):
			self.save(self.filename)
		else:
			with open(self.filename, 'r') as f:
				data = json.loads(f.read())
				if str(data["episode"]) != str(self.list_infa["episode"]):
					self.list_infa["new_infa"] = True
					self.save(self.filename)

	def setHtml(self):
		r = requests.get(self.url)
		self.html = r.text

	def parser(self):
		soup = BeautifulSoup(self.html, 'lxml')

		title = self.formation(soup.find('h1', class_="ua-title").text)
		img = soup.find("div", class_='mov-img')
		episode = self.formation(img.find("div",class_="mov-episode").text)
		if len(episode) == 0:
			episode = "all"

		self.list_infa = {
			"title" : title,
			"orig-name": soup.find("div",class_="orig-name").text,
			"img":{
				"alt": self.formation(img.find("img").get('alt')),
				"src": img.find("img").get('src'),
			},
			"episode": episode,
			"new_infa": False
		}

	def save(self,filename):
		r = requests.get(self.list_infa["img"]["src"],stream=True)

		with open(self.imagename,"wb") as f:
			for chunk in r.iter_content(8192):
				f.write(chunk)
		

		with open(filename,"w") as f:
			json.dump(self.list_infa, f, indent=2, ensure_ascii=False)

	def clear(self,imagename):
		print(imagename)
		path = os.path.join(os.path.abspath(imagename))

		os.remove(path)
		path = os.path.join(os.path.abspath(self.filename))
		os.remove(path)

	def formation(self,text):
		return str(text.replace ("і","i").replace("І","I"))

def writeHtml(movs, filename='answer.html'):
	with open("cooki/"+filename,"w") as f:
		for mov in movs:
			f.write(str(mov) + "\n-----------------\n")
