import requests
from tkinter import *

class NewsApp:
    def __init__(self):

        # fetch data
        self.data = requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=0d11e00d56194e87aeb5987458226557').json()
        # initial Gui load
        self.load_gui()

        # load the first news item
        self.load_news_item(1)# in data there are 20 news item but i have to fetch the 0th item


    def load_gui(self):
        self.root = Tk()
        self.root.geometry('450x700')
        # resize nahi kar rahe kyuki ham chate he ki resize ho pae
        self.root.configure(background='black')

    def clear(self):
        for i in self.root.pack_slaves(): # pack geometry manager
            # jo button aur gui item ko place karte ho geometry ke upar usko pack_slaves bolte h
            # isse hum geometry pe kitna cheez laga hua h vo nikal sakte hi aur fir pura screen clear ho jaega
            i.destroy()

    def load_news_item(self,index): # jo index value milega vahi index value ko pakad ke kaam karega

        # first we have to clear the screen so that next news load ho pae
        self.clear()

        heading = Label(self.root,text=self.data['articles'][index]['title'],bg='black',fg='white',wraplength=450,justify='center')
        heading.pack(pady=(10,20))
        heading.config(font=('verdana',15))

        details = Label(self.root, text=self.data['articles'][index]['description'], bg='black', fg='white', wraplength=450,justify='center')
        details.pack(pady=(2, 20))
        details.config(font=('verdana', 12))


        self.root.mainloop()



obj = NewsApp()