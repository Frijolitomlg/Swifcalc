# _   __                       _       
#| | / /                      | |      
#| |/ /_      ____ _  ___ __ _| |_ ___ 
#|    \ \ /\ / / _` |/ __/ _` | __/ _ \
#| |\  \ V  V / (_| | (_| (_| | ||  __/
#\_| \_/\_/\_/ \__,_|\___\__,_|\__\___|
#
# This is just a simulation on the price of the swift against other crypto and USD, 
# The price is based on the ETH price from the Token Sale that was 105,568 SFT 
                                      

''' Libraries to import all native to python3 '''
import tkinter
from tkinter import *
from tkinter import messagebox
import json
import urllib.request
import urllib.error


#constants and initial values
myswf = 0
ETH = 1
SWFT = 105568
rate = ETH/SWFT

X_ETH_BTC = 0
X_ETH_USD = 0

EUSD = 0
ESWFT = 0
BETH = 0


''' initial connection function '''
url = "https://api.binance.com/api/v1/ticker/price?symbol="+"ETHBTC"
url2 = "https://api.binance.com/api/v1/ticker/price?symbol="+"ETHUSDT"

ethmarketdata = json.load(urllib.request.urlopen(url2))
btcmarketdata = json.load(urllib.request.urlopen(url))

X_ETH_USD = float(ethmarketdata['price'])
X_ETH_BTC = float(btcmarketdata['price'])

def exconnection():
    ''' reconection function '''
    url = "https://api.binance.com/api/v1/ticker/price?symbol="+"ETHBTC"
    url2 = "https://api.binance.com/api/v1/ticker/price?symbol="+"ETHUSDT"

    ethmarketdata = json.load(urllib.request.urlopen(url2))
    btcmarketdata = json.load(urllib.request.urlopen(url))

    X_ETH_USD = float(ethmarketdata['price'])
    X_ETH_BTC = float(btcmarketdata['price'])
    
# GUI in tkinter


class App():
    
    def __init__(self):
        self.master = Tk()
        self.master.title("Swift Sim Price Alpha")
        self.master.iconbitmap('scalc.ico')
        self.master.resizable(width=False, height=False)
        self.master.config(bg='#ffffff')
      

        self.menubar = Menu(self.master, bg=None, fg=None)
        

        self.filemenu = Menu(self.menubar, tearoff=0,)
        self.filemenu.add_command(label="Re-connect", command=exconnection)
        self.filemenu.add_command(label="Clear values", command=self.Clearall)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.master.quit)
        self.menubar.add_cascade(label="File", menu=self.filemenu)

        
        
        self.helpmenu = Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label="About", command=self.About)
        self.helpmenu.add_command(label="Credit", command=self.Credit)
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)

        self.master.config(menu=self.menubar)
        
        self.disclamer = Label(self.master, text="Calculate the aproximate value of your swift", bg='#ffffff')
        self.disclamer.grid(row=0, column=0, columnspan=4)
       

        self.ETH = Label(self.master, text="ETH value:", bg='#ffffff')
        self.ETH.grid(row=1, column=0, )
        self.yETH = Label(self.master, text=ESWFT, bg='#ffffff')
        self.yETH.grid(row=1, column=1, sticky=W)

        self.BTC = Label(self.master, text="BTC value:", bg='#ffffff')
        self.BTC.grid(row=2, column=0, )
        self.yBTC = Label(self.master, text=BETH, bg='#ffffff')
        self.yBTC.grid(row=2, column=1, sticky=W)

        
        self.USD = Label(self.master, text="USD value:", bg='#ffffff')
        self.USD.grid(row=3, column=0, )
        self.yUSD = Label(self.master, text=EUSD, bg='#ffffff')
        self.yUSD.grid(row=3, column=1, sticky=W)

        self.LB1 = Label(self.master, text="Enter your SFT ammount here:", bg='#ffffff')
        self.LB1.grid(row=4, column=0, sticky=W, columnspan=4)


        self.user_input = StringVar()


        self.ammount = Entry(self.master, textvariable=self.user_input, takefocus=True)
        self.ammount.grid(row=5, column=1, )

        self.btprocess = Button(self.master, text="Calculate", command=self.process, bg='#ffffff')
        self.btprocess.grid(row=5, column=2, sticky=W)
        
        

    def About(self):

        self.Aboutinf = messagebox.showinfo("About","This Software calculate an aproximate value according to the result of the token sale.\nThis aproximation do not represent the real value on the market.")

    def Credit(self):

        self.Creditinf = messagebox.showinfo("Credit","Created by Kwacate")
    
    def Clearall(self):

        myswf = 0
        EUSD = 0
        ESWFT = 0
        BETH = 0
        self.yETH.configure(text=ESWFT)
        self.yBTC.configure(text=BETH)
        self.yUSD.configure(text=EUSD)
        self.ammount.delete(0, END)


    def process(self):
        

        u_input = self.user_input.get()

        if u_input.isdecimal() == True:

            myswf = float(u_input)



            ## calculating stuff ##
            ESWFT = rate * myswf / 4
            '''Swift to ETH ratio'''
            EUSD = X_ETH_USD * ESWFT / 4
            '''ETH to USD ratio'''
            BETH = X_ETH_BTC * ESWFT / 4
            '''ETH to BTC ratio'''

            ESWFT = format(ESWFT, '.7f')
            BETH = format(BETH, '.7f')
            EUSD = format(EUSD, '.7f')

            ## updating the sheit ##
            self.yETH.configure(text=ESWFT)
            self.yBTC.configure(text=BETH)
            self.yUSD.configure(text=EUSD)
            self.ammount.delete(0, END)

        else:
            self.ammount.delete(0, END) 
            self.notnumber = messagebox.showwarning("Warning","Insert a valid number")



   

   
App()

mainloop()