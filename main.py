# -*- coding: utf-8 -*-
from uaserials import *
from appWindow import *
import wx
import os
import json

def read_urls_like():
	with open("urls.txt","r") as f:
		urls = f.read().split("\n")
	return urls

def read_data():
	directory = 'cookie' 
	files = os.listdir(directory) 
	del(files[-1])
	data = []
	for f in files:
		with open("cookie/"+f,"r") as f:
			data.append(json.loads(f.read()))

	data2 = []
	for i in range(len(data)-1):
		if data[i]["new_infa"]:
			data2.append(data[i])
			del(data[i])

	for d in data:
		data2.append(d)

	return data2

def update(Serials,urls):
	for s in Serials:
		s.clear(s.imagename)
	Serials = []
	for url in urls:
		Serial = Like_Serial_Ua(url)
		Serials.append(Serial)

	return Serials

def main():
	Serials = []
	urls = read_urls_like()
	Like_Serials_Ua = []

	app = wx.App()
	frame = GUI(parent=None, id=-1, title="UaSerials")
	
	for url in urls:
		Serial = Like_Serial_Ua(url)
		Serials.append(Serial)

	#Serials = update(Serials,urls)
	data = []
	for s in Serials:
		data.append(s.list_infa);
		
	bSizer = wx.BoxSizer( wx.VERTICAL )

	i = 0
	for d in data:
		pan = Baner(frame.panel,pos=(0,i*100),size=(250,100),data=d)
		bSizer.Add( pan)
		i = i + 1
	frame.panel.SetSizer( bSizer )
	frame.Show()
	app.MainLoop()


'''
	panOne = Baner(frame.panel,pos=(0,0),size=(250,130),data=data)

	bSizer = wx.BoxSizer( wx.VERTICAL )
	bSizer.Add( panOne)
	frame.panel.SetSizer( bSizer )
	app.MainLoop()
'''
if __name__ == '__main__':
	main()