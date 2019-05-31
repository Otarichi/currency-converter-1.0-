from tkinter import *
import requests
import json


class currencyConverterApp(Frame):
    def __init__(self, main_menu=None):
        super().__init__(main_menu)
        self.main_menu = main_menu
        self.createWidgets()
        self.getCurrency()
        self.firstCurr = 'USD'
        self.calculateCurrency()


    def flip(self):
        if self.firstCurr == 'USD':
            self.currencyLabel['text'] = 'GEO Lari - GEL'
            self.currencyLabel2['text'] = 'US Dollar - USD'
            self.firstCurr = 'GEL'
            self.calculateCurrency()
        elif self.firstCurr == 'GEL':
            self.currencyLabel['text'] = 'US Dollar - USD'
            self.currencyLabel2['text'] = 'GEO Lari - GEL'
            self.firstCurr = 'USD'
            self.calculateCurrency()

    def getCurrency(self):
        try:
            URL = "https://free.currconv.com/api/v7/convert?q=USD_GEL,GEL_USD&compact=ultra&apiKey=fb5f437d110d16d98ca1"
            currencyReq = requests.get(URL)
            currency = json.loads(currencyReq.content)
            self.USDtoGEL = currency['USD_GEL']
            self.GELtoUSD = currency['GEL_USD']
            self.messageLabel["text"] = 'The course has been successfully updated'
            self.messageLabel["fg"] = 'green'
        except:
            self.messageLabel["text"] = 'Error while updating the course'
            self.messageLabel["fg"] = 'red'


    def calculateCurrency(self):
        try:
            if self.firstCurr == 'USD' and self.amaunt_1_Entry.get() != '':
                answer = float(self.amaunt_1_Entry.get()) * self.USDtoGEL
                self.amaunt_2_Label2['text'] = str(answer) + ' Gel'
                self.messageLabel["text"] = 'Conversion successfully'
            elif self.firstCurr == 'GEL' and self.amaunt_1_Entry.get() != '':
                answer = round(float(self.amaunt_1_Entry.get()) * self.GELtoUSD, 1)
                self.amaunt_2_Label2['text'] = str(answer) + ' USD'
                self.messageLabel["text"] = 'Conversion successfully'
                self.messageLabel["fg"] = 'green'
        except ValueError:
            self.messageLabel["text"] = 'Please enter only the number!'
            self.messageLabel["fg"] = 'red'
        except:
            self.messageLabel["text"] = 'Something went wrong!'
            self.messageLabel["fg"] = 'red'



    def createWidgets(self):
        self.main_menu.title("Currency Converter App by Otarichi ver 1.0")
        self.currIHaveLabel = Label(self.main_menu, text='Currency I Have:', font=('Arial', 16)).place(x=10, y=10)
        self.currencyLabel = Label(self.main_menu, text='US Dollar - USD', font=('Arial', 18, 'bold'))
        self.currencyLabel.place(x=30, y=40)
        self.amaunt_1_Label = Label(self.main_menu, text='AMOUNT:', font=('Arial', 16)).place(x=10, y=75)
        self.amaunt_1_Entry = Entry(self.main_menu, width=30)
        self.amaunt_1_Entry.place(x=30, y=110)
        self.amaunt_1_Entry.insert(0, 1)
        self.flipButton = Button(self.main_menu, text='<->', command=self.flip).place(x=255, y=60)
        self.currIWantLabel = Label(self.main_menu, text='Currency I Want:', font=('Arial', 16)).place(x=320, y=10)
        self.currencyLabel2 = Label(self.main_menu, text='GEO Lari - GEL', font=('Arial', 18, 'bold'))
        self.currencyLabel2.place(x=340, y=40)
        self.amaunt_2_Label = Label(self.main_menu, text='AMOUNT:', font=('Arial', 16)).place(x=320, y=75)
        self.amaunt_2_Label2 = Label(self.main_menu, text='0', font=('Arial', 14))
        self.amaunt_2_Label2.place(x=340, y=103)
        self.calculateButton = Button(self.main_menu, text='Calculate', command=self.calculateCurrency).place(x=240, y=150)
        self.updateCurrencyButton = Button(self.main_menu, text='Update Course', command=self.getCurrency).place(x=225, y=180)
        self.messageLabel = Label(self.main_menu, text='')
        self.messageLabel.place(x=20, y=220)


main_menu = Tk()
main_menu.geometry('540x250')
currencyConverterApp_01 = currencyConverterApp(main_menu)
currencyConverterApp_01.mainloop()






