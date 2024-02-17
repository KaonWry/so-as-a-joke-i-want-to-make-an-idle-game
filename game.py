import tkinter as tk
import math

score = 0
mult = 1
upg = [0]

# Reusable
def logFunc(a, b, c, upgradeType):
    global upg
    return a * math.log(upg[upgradeType - 1], b) + c

def expFunc(a, b, c, upgradeType):
    global upg
    return (a * math.pow(upg[upgradeType - 1], b) + c)

def changeState(a):
    if a['state'] == 'normal':
        a.config(state='disabled')
    else:
        a.config(state='normal')
        
# Score
def addScore():
    global score
    score += 0.01 * (1 + mult)
    
def showValue():
    global score
    addScore()
    shownScore.set(round(score, 2))
    window.after(10, showValue)
    
def showGrowth():
    global mult
    shownGrowth.set(f'{round(0.01 * (mult)*100, 2)}/s')
    window.after(1, showGrowth)
    
# Called each button click
def addMult(upgradeType, upgradeMult):
    global mult
    global upg
    mult += upgradeMult
    upg[upgradeType - 1] += 1
    if upg[upgradeType - 1] == 1:
        upg.append(0)
        
def minScore(a, b, c, upgradeType):
    global score
    cost = expFunc(a, b, c, upgradeType)
    score = score - cost

def upgButtonClick(a, b, c, upgradeType, upgradeMult):
    minScore(a, b, c, upgradeType)
    addMult(upgradeType, upgradeMult)

# Called every ms
def upgradeCost(a, b, c, upgradeType, upgradeVar):
    upgradeVar.set(round(expFunc(a, b, c, upgradeType), 2))
    
def checkUpgradeCost(a, b, c, upgradeType, button):
    global score
    cost = expFunc(a, b, c, upgradeType)
    if score <= cost:
        button.config(state='disable')
    else:
        button.config(state='normal')
    
def checkButton(a, b, c, upgradeType, button, upgradeVar):
    upgradeCost(a, b, c, upgradeType, upgradeVar)
    checkUpgradeCost(a, b, c, upgradeType, button)
    window.after(10, lambda: checkButton(a, b, c, upgradeType, button, upgradeVar))

# Debugging
def boostValue():
    global score
    score += sclAddValue.get()

# Window Management
window = tk.Tk()
window.title('CIA Black Project')
window.minsize(800, 600)

# Text Display
shownScore = tk.StringVar()
shownGrowth = tk.StringVar()
upgr1Cost = tk.StringVar()
upgr1Mult = tk.StringVar()

lblScore = tk.Label(window, textvariable=shownScore, font=('Helvetica', 30))
lblScore.grid(row=0, column=0, columnspan=5, padx = 10, pady = 10, sticky='w')

lblGrowth = tk.Label(window, textvariable=shownGrowth, font=('Helvetica', 12))
lblGrowth.grid(row=1, column=0, padx = 10, sticky='w')

# Upgrade 1
btnUpgrade1 = tk.Button(window, textvariable=upgr1Cost, font=('Helvetica', 16), command=lambda: upgButtonClick(1.5, 2.5, 2, 1, 1))
btnUpgrade1.grid(row=2, column=0, padx= 10, sticky='w')
checkButton(1.5, 2.5, 2, 1, btnUpgrade1, upgr1Cost)

lblUpgrade1 = tk.Label(window, textvariable=upgr1Mult, font=('Helvetica', 16))
lblUpgrade1.grid(row=2, column=1, padx= 10, sticky='w')

# Debugging Stuffs
btnBoostValue = tk.Button(window, text='add value', font=('Helvetica', 12), command=boostValue, state="normal")
btnBoostValue.grid(row=99, column=0, padx=10, pady=10, sticky='w')

btnChangeState = tk.Button(window, text='change state', font=('Helvetica',12), command=lambda: changeState(btnBoostValue))
btnChangeState.grid(row=99, column=1, padx=10, pady=10, sticky='w')
    
sclAddValue = tk.Scale(window, from_=0, to=1000, orient=tk.HORIZONTAL)
sclAddValue.grid(row=99, column=2, pady=10)

# Start App    
showValue()
showGrowth()
window.mainloop()