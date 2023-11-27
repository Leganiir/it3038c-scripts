#Modules needed are pip install tkinter and requests. Note that tkinter may already be installed, so if pip cannot find the library you're good to go.
#Note: the API has 1,500 monthly calls allowed.
import tkinter
from tkinter import *
import tkinter.messagebox
import requests

#Creates the size of the application screen and gives the process a title.
root = tkinter.Tk()
root.title("Isaac Leganik Currency Convert")
root.geometry("700x700")

#Creates the variables to store which currency we are starting with and converting to.
Money1 = tkinter.StringVar(root)
Money2 = tkinter.StringVar(root)

def Convert():
    #This code grabs which currency we are converting to from the tkinter OptionMenu
    From_Currency = Money1.get()
    To_Currency = Money2.get()
    #This code formats the inputs such that I can send them to the API, which needs just the first 3 letters. From currency is the starting, to is what we are converting to.
    From_Currency = From_Currency.split("-")[0].strip()
    To_Currency = To_Currency.split("-")[0].strip()
    
    #This code takes the base url for the API and adds the currency code (USD) that we just got. It will finish with a api_call looking like "https://v6.exchangerate-api.com/v6/48c489d56e65fc732ac98e21/latest/USD"
    base_api = "https://v6.exchangerate-api.com/v6/48c489d56e65fc732ac98e21/latest/"
    api_call = base_api + From_Currency
    
    #If Statement to ensure there's a starting amount of currency.
    if (StartingAmount.get() == ""):
        tkinter.messagebox.showerror("Error", "Please enter a starting amount")
        
    #This ensures there are two currencies selected
    elif (From_Currency == "" or To_Currency == ""):
        tkinter.messagebox.showerror("Error", "Please select two currencies")
        
    else:
        #Otherwise, we move on and call the API, ensuring we get a good status code of 200
        response = requests.get(api_call)
        if response.status_code == 200:
            #This code takes the API reponse and looks for the conversion rate for the currency we are converting to.
            api_data = response.json()
            conversion_rates = api_data.get("conversion_rates")
            exchange_rate = conversion_rates[To_Currency]
            
            try: 
                #Trys to convert. This is so that if someone enters "ABC" into the 'Starting Amount' box, it gives an error rather than crashing.
                #The final conversion is also trimmed to 2 decimal places. The result is inserted into the 'EndingAmount' tkinter entry field.
                FinalConversion = float(StartingAmount.get()) * exchange_rate
                FinalConversionFormat = "{:.2f}".format(FinalConversion)
                EndingAmount.insert(0, str(FinalConversionFormat))
            except ValueError:
                tkinter.messagebox.showerror("Error", "Your 'Starting Amount' entry has extra spaces and or letters, enter only number and decimals")
                
        else:
            tkinter.messagebox.showerror("Error", "API returning error")
            
#This chunck of code makes the header "Isaac Leganik's Currency Project" text.
label = tkinter.Label(root, text="Isaac Leganik's Currency Project", font=('Times New Roman', 18))
label.grid(row=0, column=1, sticky='nsew', ipady=10)

#This set of code makes the "Starting Amount" text along with the box to enter the amount of currency to convert.
label = tkinter.Label(root, text="Starting Amount: ", font=('Times New Roman', 14))
label.grid(row=1, column=0, sticky=E, ipady=10)
StartingAmount = tkinter.Entry(root)
StartingAmount.grid(row=1, column=1, sticky=W)

#Creates the "From" label
label = tkinter.Label(root, text="From: ", font=('Times New Roman', 14))
label.grid(row=2, column=0, sticky=E, pady=2)

#Creates the "To" label
label = tkinter.Label(root, text="To: ", font=('Times New Roman', 14))
label.grid(row=3, column=0, sticky=E)

#A list of currencies that the program can convert
Currency_List = ["EUR - Euro - €", "USD - US Dollar - $", "JPY - Japanese Yen - ¥", "GBP - Great British Pound - £", "CAD - Canadian Dollar - $",
                 "KRW - South Korean Won - ₩", "CNY - Chinese Yuan - ¥", "RUB - Russian Ruble - ₽", "INR - Indian Rupee - ₹", "MXN - Mexican Peso - $"]

#This code creates the entry boxes for the currency list, pulling from the array made above, allowing the user to choose.
FromCurrency = tkinter.OptionMenu(root, Money1, *Currency_List)
ToCurrency = tkinter.OptionMenu(root, Money2, *Currency_List)
FromCurrency.grid(row=2, column=1, sticky=W)
ToCurrency.grid(row=3, column=1, sticky=W)

#Creates the clickable button to call the Convert function
label = Button(root, text="Convert", font=(18), command=Convert, padx=5, pady=5)
label.grid(row=5, column=1, pady=20, sticky=W)

#Creates the output field
label = tkinter.Label(root, text="Converted: ", font=('Times New Roman', 14))
label.grid(row=7, column=0, sticky=E)
EndingAmount = tkinter.Entry(root)
EndingAmount.grid(row=7, column=1, sticky=W)

root.mainloop()
