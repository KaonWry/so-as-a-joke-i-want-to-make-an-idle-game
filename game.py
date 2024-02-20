import tkinter as tk
import math
import time

score = 0
mult = 1
last_time = 0

# Define class
class Upgrade:
    def __init__(self, a, b, c, upgrade_mult):
        self.a = a
        self.b = b
        self.c = c
        self.upgrade_mult = upgrade_mult
        self.level = 1

# List of upgrades
# Format: a, b, c, multiplier
upgrades = [
    Upgrade(1.2, 2.3, 2, 1),
    Upgrade(1.5, 2.5, 10, 3),
    Upgrade(2, 3.3, 50, 7),
    Upgrade(2.5, 4.3, 100, 9),
    # Add more upgrades as needed 
]

# Reusable
def logFunc(upgrade):
    return upgrade.a * math.log(upgrade.level - 1, upgrade.b) + upgrade.c

def expFunc(upgrade):
    return upgrade.a * math.pow(upgrade.level - 1, upgrade.b) + upgrade.c

def changeState(a):
    if a['state'] == 'normal':
        a.config(state='disabled')
    else:
        a.config(state='normal')
        
# Score
def addScore():
    global score
    score += 0.01 * (mult)

def showValue():
    global score
    addScore()
    shownScore.set(round(score, 2))
    window.after(10, showValue)

def showGrowth():
    global mult, last_time
    current_time = time.time()
    elapsed_time = current_time - last_time if last_time else 0
    last_time = current_time
    growth_rate = 0 if elapsed_time == 0 else 0.01 * mult / elapsed_time
    rounded_growth_rate = round(growth_rate * 100, 2)
    shownGrowth.set(f'{rounded_growth_rate}/s')
    window.after(1000, showGrowth)
    
# Called each button click
def minScore(upgrade):
    global score
    cost = expFunc(upgrade)
    score = score - cost

def addMult(upgrade):
    global mult
    upgrade.level += 1
    mult += upgrade.upgrade_mult * upgrade.level

def handleUpgrade(upgrade):
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
    var.set(f'Lvl {upgrade.level}, {upgrade.upgrade_mult + 1}x multiplier')

def checkButton(upgrade, button, varCost, varMult):
    upgradeCost(upgrade, varCost)
    checkUpgradeCost(upgrade, button)
    showMult(upgrade, varMult)
    window.after(10, lambda: checkButton(upgrade, button, varCost, varMult))

# Debugging
def boostValue():
    global score
    score += sclAddValue.get()
    
# Upgrade Button
def createUpgradeButton(row, upgrade, varCost, varMult):
    btnUpgrade = tk.Button(window, textvariable=varCost, font=('Helvetica', 14), command=lambda: handleUpgrade(upgrade))
    btnUpgrade.grid(row=row, column=0, padx=10, pady=2, sticky='w')

    lblUpgrade = tk.Label(window, textvariable=varMult, font=('Helvetica', 14))
    lblUpgrade.grid(row=row, column=1, padx=10, pady=2, columnspan=99, sticky='w')

    checkButton(upgrade, btnUpgrade, varCost, varMult)
    
# Window Management
window = tk.Tk()
window.title('CIA Black Project')
window.minsize(800, 600)

# Text Display
shownScore = tk.StringVar()
shownGrowth = tk.StringVar()

lblScore = tk.Label(window, textvariable=shownScore, font=('Helvetica', 30))
lblScore.grid(row=0, column=0, columnspan=99, padx = 10, pady = 10, sticky='w')

lblGrowth = tk.Label(window, textvariable=shownGrowth, font=('Helvetica', 12))
lblGrowth.grid(row=1, column=0, padx = 10, sticky='w')

# Create upgrade buttons in a loop
for i, upgrade in enumerate(upgrades, start=2):  # Starting from row 2
    varCost = tk.StringVar()
    varMult = tk.StringVar()
    createUpgradeButton(i, upgrade, varCost, varMult)

# Debugging Stuffs
btnBoostValue = tk.Button(window, text='add value', font=('Helvetica', 12), command=boostValue, state="normal")
btnBoostValue.grid(row=99, column=0, padx=10, pady=10, sticky='w')

# btnChangeState = tk.Button(window, text='change state', font=('Helvetica',12), command=lambda: changeState(btnBoostValue))
# btnChangeState.grid(row=99, column=1, padx=10, pady=10, sticky='w')
    
sclAddValue = tk.Scale(window, from_=0, to=1000, orient=tk.HORIZONTAL)
sclAddValue.grid(row=99, column=1, pady=10)

# Start App    
showValue()
showGrowth()
window.mainloop()