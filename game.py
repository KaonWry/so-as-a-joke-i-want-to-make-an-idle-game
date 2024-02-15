import tkinter as tk
import time
import math

score = 1
mult = 0

def baseAddValue():
    global score
    score += 0.01 * (1 + mult)
    
def multiplier():
    global mult
    mult += 0.25
    
def showValue():
    global score
    baseAddValue()
    shownScore = score
    lblScore['text'] = round(shownScore, 2)
    window.after(100, showValue)
    
def showgGrowth():
    global mult
    shownGrowth = str(round((0.01 * (1 + mult)*10), 3))
    lblGrowth['text'] = f'{shownGrowth}/s'
    window.after(1, showgGrowth)
    
def showMult():
    global mult
    shownMult = f'{int(mult*100)}%'
    lblMult['text'] = shownMult
    window.after(1, showMult)
    
def boostValue():
    global score
    score += sclAddValue.get()
    
def changeState():
    if btnBoostValue['state'] == 'normal':
        btnBoostValue.config(state='disabled')
    else:
        btnBoostValue.config(state='normal')

window = tk.Tk()
window.title('CIA Black Project')
window.minsize(800, 600)

lblScore = tk.Label(window, text='', font=('Helvetica', 30))
lblScore.grid(row=0, column=0, columnspan=5, padx = 10, pady = 10, sticky='w')

lblGrowth = tk.Label(window, text='', font=('Helvetica', 12))
lblGrowth.grid(row=1, column=0, padx = 10, pady = 0, sticky='w')

btnMult = tk.Button(window, text='Pound me dady UwU', command=multiplier, font=('Helvetica', 9))
btnMult.grid(row=2, column=0, padx=10, pady=10, sticky='w')

lblMult = tk.Label(window, text='', font=('Helvetica', 12))
lblMult.grid(row=2, column=1, padx=10, pady=10, sticky='w')

btnBoostValue = tk.Button(window, text='add value', font=('Helvetica', 12), command=boostValue, state="normal")
btnBoostValue.grid(row=3, column=0, padx=10, pady=10, sticky='w')

btnChangeState = tk.Button(window, text='change state', font=('Helvetica',12), command=changeState)
btnChangeState.grid(row=3, column=1, padx=10, pady=10, sticky='w')
    
sclAddValue = tk.Scale(window, from_=0, to=1000, orient=tk.HORIZONTAL)
sclAddValue.grid(row=3, column=2, pady=10)

showValue()
showMult()
showgGrowth()
window.mainloop()