#!/usr/bin/python3
# -*- coding: utf-8 -*-
import wx
import wx.lib.scrolledpanel

class Baner(wx.Panel):

	def __init__(self,panel, pos, size, data):
		super(wx.Panel, self).__init__(panel, pos=pos, size=size)
		png = wx.StaticBitmap(self, -1, wx.Bitmap(data["img"]["src"], wx.BITMAP_TYPE_JPEG),pos=(0,0), size = size)
		nameButton = wx.StaticText(self, label = data["title"],style=wx.ALIGN_LEFT, pos = (0,size[1]-15-15),size = (size[0],15))
		nameButton.SetBackgroundColour('#FFFFFF')
		episodeButton = wx.StaticText(self, label=data['episode'], pos=(0, size[1]-15),style=wx.ALIGN_LEFT,size = (size[0],15))
		if data["new_infa"]:
			episodeButton.SetBackgroundColour('#ff5c33')
		else:
			episodeButton.SetBackgroundColour('#FFFFFF')


class GUI(wx.Frame):

	def __init__(self,parent,id,title):
		#First retrieve the screen size of the device
		#Create a frame
		wx.Frame.__init__(self,parent,id,title,style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER)
		self.SetSize((255, 440))
		self.Centre()

#First retrieve the screen size of the device
		screenSize = wx.DisplaySize()
		screenWidth = screenSize[0]
		screenHeight = screenSize[1]

		panel1 = wx.Panel(self,size=(250,28), pos=(0,0), style=wx.SIMPLE_BORDER)
		panel1.SetBackgroundColour('#FDDF99')
		logo = wx.StaticText(panel1, label = "UaSerials - my like serials",style=wx.ALIGN_LEFT, pos = (0,0),size = (150,15))
		update = wx.Button(panel1,id = -1,label="update",pos=(150,0),size=(50,28))
		good = wx.Button(panel1,id = -1,label="good",pos=(200,0),size=(50,28))

		self.panel = wx.lib.scrolledpanel.ScrolledPanel(self,-1, size=(250,400), pos=(0,28), style=wx.SIMPLE_BORDER)
		self.panel.SetupScrolling()
		self.panel.SetBackgroundColour('#FFFFFF')


'''
		panOne = wx.Panel(panel,pos=(0,0),size=(250,100))
		#250 345
		png = wx.StaticBitmap(panOne, -1, wx.Bitmap("1071.jpg", wx.BITMAP_TYPE_JPEG))
		nameButton = label = wx.StaticText(panOne, label = "Hello World", pos = (10,30)) 
		episodeButton = wx.StaticText(panOne, label='episode', pos=(10, 10))
'''

'''

wx.Frame.__init__(self,parent,id,title,size=screenSize, style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER)

    panel1 = wx.Panel(self,size=(screenWidth,28), pos=(0,0), style=wx.SIMPLE_BORDER)
    panel1.SetBackgroundColour('#FDDF99')
    panel2 = wx.lib.scrolledpanel.ScrolledPanel(self,-1, size=(screenWidth,400), pos=(0,28), style=wx.SIMPLE_BORDER)
    panel2.SetupScrolling()
    panel2.SetBackgroundColour('#FFFFFF')


    button1 = wx.Button(panel2,label="Button 1",pos=(0,50),size=(50,50))
    button2 = wx.Button(panel2,label="Button 2",pos=(0,100), size=(50,50))
    button3 = wx.Button(panel2,label="Button 3",pos=(0,150),size=(50,50))
    button4 = wx.Button(panel2,label="Button 4",pos=(0,200), size=(50,50))
    button5 = wx.Button(panel2,label="Button 5",pos=(0,250),size=(50,50))
    button6 = wx.Button(panel2,label="Button 6",pos=(0,300), size=(50,50))
    button7 = wx.Button(panel2,label="Button 7",pos=(0,350), size=(50,50))
    button8 = wx.Button(panel2,label="Button 8",pos=(0,400), size=(50,50))



    bSizer = wx.BoxSizer( wx.VERTICAL )
    bSizer.Add( button1, 0, wx.ALL, 5 )
    bSizer.Add( button2, 0, wx.ALL, 5 )
    bSizer.Add( button3, 0, wx.ALL, 5 )
    bSizer.Add( button4, 0, wx.ALL, 5 )
    bSizer.Add( button5, 0, wx.ALL, 5 )
    bSizer.Add( button6, 0, wx.ALL, 5 )
    bSizer.Add( button7, 0, wx.ALL, 5 )
    bSizer.Add( button8, 0, wx.ALL, 5 )
    panel2.SetSizer( bSizer )


import wx


class Example(wx.Frame):

    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw)

        self.InitUI()

    def InitUI(self):

        pnl = wx.Panel(self)

        png = wx.StaticBitmap(pnl, -1, wx.Bitmap("10png", wx.BITMAP_TYPE_ANY))
        nameButton = label = wx.StaticText(pnl, label = "Hello World", pos = (10,20)) 

        episodeButton = wx.StaticText(pnl, label='episode', pos=(10, 40))

        self.SetSize((350, 250))
        self.SetTitle('UaSerials')
        self.Centre()

    def OnClose(self, e):

        self.Close(True)


def main():

    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()  '''