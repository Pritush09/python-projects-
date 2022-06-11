import io
import webbrowser
import requests
from tkinter import *
from urllib.request import urlopen  # to get the image of the news
from PIL import ImageTk,Image

class NewsApp:
    def __init__(self):

        # fetch data
        self.data = requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=0d11e00d56194e87aeb5987458226557').json()
        #print(self.data)
        # initial Gui load
        self.load_gui()

        # load the first news item
        self.load_news_item(0)# in data there are 20 news item but i have to fetch the 0th item


    def load_gui(self):
        self.root = Tk()
        self.root.geometry('550x700')
        # resize nahi kar rahe kyuki ham chate he ki resize ho pae
        #self.root.resizable(0,0)
        self.root.configure(background='black')
        # tk jo title araha he browser tk usko change kar rahe
        self.root.title('MY NEWS APP')

    def clear(self):
        for i in self.root.pack_slaves(): # pack geometry manager
            # jo button aur gui item ko place karte ho geometry ke upar usko pack_slaves bolte h
            # isse hum geometry pe kitna cheez laga hua h vo nikal sakte hi aur fir pura screen clear ho jaega
            i.destroy()

    def load_news_item(self,index): # jo index value milega vahi index value ko pakad ke kaam karega

        # first we have to clear the screen so that next news load ho pae
        self.clear()

        # image sabse pehle place hoga
        # agar image nahi load hota h toh uske liye try use karlo
        try:
            img_url = self.data['articles'][index]['urlToImage']
            raw_data = urlopen(img_url).read() # jo data aega uss data ko read karenge data vo binary format me hoga toh variable me store kardiye
            im = Image.open(io.BytesIO(raw_data)).resize((540,350)) # ye code basically read karta h imiage ko binary format se
            photo = ImageTk.PhotoImage(im) # basically load karta h image ko photo ke format me
        except:
            img_url = 'https://bitsofco.de/content/images/2018/12/broken-1.png'
            raw_data = urlopen(img_url).read()  # jo data aega uss data ko read karenge data vo binary format me hoga toh variable me store kardiye
            im = Image.open(io.BytesIO(raw_data)).resize((540, 350))  # ye code basically read karta h imiage ko binary format se
            photo = ImageTk.PhotoImage(im)  # basically load karta h image ko photo ke format me


        Labe = Label(self.root,image=photo) # vo image ko label ke format me display karva diye
        Labe.pack(pady=(2,3))#  ab pack karna hoga

        heading = Label(self.root,text=self.data['articles'][index]['title'],bg='black',fg='white',wraplength=450,justify='center')
        heading.pack(pady=(10,20))
        heading.config(font=('verdana',15))

        details = Label(self.root, text=self.data['articles'][index]['description'], bg='black', fg='white', wraplength=450,justify='center')
        details.pack(pady=(2, 20))
        details.config(font=('verdana', 12))

        # button place karne ke liye pehle hame ek frame banana padega
        frame = Frame(self.root,bg='black') # self.root ko dale kyuki ye jo frame he vo root ke upar hi create hoga

        # now ab gui object ko pack karna padta he toh fame ko bhi pack kardiye
        frame.pack(expand=True,fill=BOTH)

        read = Button(frame, text='Read More', width=30, height=3, command=lambda :self.open_link(self.data['articles'][index]['url']))
        read.pack(side=LEFT)


        if index != 0:
            prev = Button(frame,text='Prev',width=23,height=3,command= lambda :self.load_news_item(index-1))
            prev.pack(side=LEFT)


        if index != len(self.data['articles'])-1:
            Next = Button(frame, text='Next', width=23, height=3,command= lambda :self.load_news_item(index+1))
            Next.pack(side=RIGHT)



        self.root.mainloop()

    def open_link(self,url):
        webbrowser.open(url)



obj = NewsApp()