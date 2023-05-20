from tkinter import*


signs = ["Mouse","Ox","Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Sheep",  "Monkey", "Rooster", "Dog", "Pig"]

personalities = ["quick-witted and resourceful", "diligent and dependable" , 
			"ambitious and charming", "compassionate and elegant" , 
			"energetic and charismatic", "enigmatic and intelligent", 
			"self-reliant and active" , "calm and creative, ", 
			"sharp and curious",  "observant and practical", 
			"lovely and honest",  "compassionate and generous"]

def showSign(event):
    birthYear = (int)(inputbox.get())
    years = birthYear - 1900
    index = years%12
    label2.config(text="Your zodiac sign is: " +signs[index]+ ". You are not " +personalities[index])

window = Tk()
window.geometry("1000x500")

label1 = Label(window, text = "Please enter your birth year(chinese calender):",
               font = ("Arial", 20)) 
label1.pack()

inputbox = Entry(window)
inputbox.pack()

label2 = Label(window, text = "Result will show here",
               font = ("Arial", 20)) 
label2.pack()

window.bind('<Return>', showSign)
#for i in range((int)(1900, 2021)):

    
