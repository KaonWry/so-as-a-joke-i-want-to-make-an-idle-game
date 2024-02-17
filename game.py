import tkinter as tk
import math

score = 0
mult = 1

# Define class
class Upgrade:
    def __init__(self, a, b, c, upgrade_mult):
        self.a = a
        self.b = b
        self.c = c
        self.upgrade_mult = upgrade_mult
        self.level = 0
        
# Classes 
upgrade1 = Upgrade(1.2, 2.3, 2, 1)

# Reusable
def logFunc(upgrade):
    return upgrade.a * math.log(upgrade.level, upgrade.b) + upgrade.c

def expFunc(upgrade):
    return upgrade.a * math.pow(upgrade.level, upgrade.b) + upgrade.c

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
    shownGrowth.set(f'{round(0.01 * (mult) * 100, 2)}/s')
    window.after(1, showGrowth)
    
# Called each button click
def minScore(upgrade):
    global score
    cost = expFunc(upgrade)
    score = score - cost

def addMult(upgrade):
    global mult
    upgrade.level += 1
    mult += upgrade.upgrade_mult

def upgButtonClick(upgrade):
    minScore(upgrade)
    addMult(upgrade)

# Called every ms
def upgradeCost(upgrade, var):
    var.set(round(expFunc(upgrade), 2))

def checkUpgradeCost(upgrade, button):
    global score
    cost = expFunc(upgrade)
    if score <= cost:
        button.config(state='disable')
    else:
        button.config(state='normal')
        
def showMult(upgrade, var):
    mult = upgrade.level * upgrade.upgrade_mult
    var.set(f'{mult + 1}x')

def checkButton(upgrade, button, varCost, varMult):
    upgradeCost(upgrade, varCost)
    checkUpgradeCost(upgrade, button)
    showMult(upgrade, varMult)
    window.after(10, lambda: checkButton(upgrade, button, varCost, varMult))

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
btnUpgrade1 = tk.Button(window, textvariable=upgr1Cost, font=('Helvetica', 16), command=lambda: upgButtonClick(upgrade1))
btnUpgrade1.grid(row=2, column=0, padx= 10, sticky='w')

lblUpgrade1 = tk.Label(window, textvariable=upgr1Mult, font=('Helvetica', 16))
lblUpgrade1.grid(row=2, column=1, padx= 10, sticky='w')

checkButton(upgrade1, btnUpgrade1, upgr1Cost, upgr1Mult)

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