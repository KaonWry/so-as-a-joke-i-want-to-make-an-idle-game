import tkinter
import time
import math

score = 1
totalMult = 1

def showValue():
    global score
    score += 0.01 * multiplier()
    label['text'] = round(score, 2)
    window.after(100, showValue)
    
def multiplier():
    global totalMult
    totalMult += 1
    return (totalMult)

window = tkinter.Tk()
window.title("Welcome To This Fucking Cumstain of a Programming Project")
window.minsize(800, 600)

label = tkinter.Label(window, text="", font=('Helvetica', 30))
label.pack(anchor="w", padx = 20, pady = 20)

button = tkinter.Button(window, text="Click Me", command=multiplier)
button.pack()
    
showValue()
window.mainloop()