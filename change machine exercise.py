from tkinter import *

window = Tk()
window.title = ("Changer")
window.configure(bg = "lightgreen")
window.geometry("500x500")

def showResult():
    try:
        amount = int(input1.get())
        if amount >=0:
            numQuarters = amount//25
            amount = amount%25
            numDimes = amount//10
            amount = amount%10
            numNickels = amount//5
            amount = amount%5
            numPennies = amount//1
            amount = amount%1
            resultArea.config(text = str(numQuarters) + " quarter(s) \n" + \
                              str(numDimes) + " dime(s) \n" + \
                              str(numNickels) + " Nickel(s) \n" + \
                              str(numPennies) + " Pennie(s) \n")
        else:
            displayArea.config( text = "invalid input, try again")
    except:
         resultArea.config( text = "invalid input, try again")
label1 = Label(window, text = "Please enter the amount in terms of cents")
label1.pack()

input1 = Entry(window)
input1.pack()

button1 = Button(window, text = "Show Result", command = showResult)
button1.pack(pady = 20)

resultArea = Label(window, text = "Result will show here")
resultArea.pack()
