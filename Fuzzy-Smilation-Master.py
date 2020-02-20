# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 23:09:46 2019

@author: hbaha
"""

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import datetime
now = datetime.datetime.now()
seconds = now.second
root = tk.Tk()
frame = tk.Frame(root)
    
    
    
frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
# New Antecedent/Consequent objects hold universe variables and membership
# functions

x_Organt_Man = ctrl.Antecedent(np.arange(0, 15, 1), 'Param1')
x_Lack_Cop_Us = ctrl.Antecedent(np.arange(0, 15, 1), 'Param2')
x_Indq_Infr = ctrl.Antecedent(np.arange(0, 15, 1), 'Param3')
x_Corp_Pol_Neg = ctrl.Antecedent(np.arange(0, 15, 1), 'Param4')
x_Fail_Identi = ctrl.Antecedent(np.arange(0, 15, 1), 'Param5')
x_Tech_Complex = ctrl.Antecedent(np.arange(0, 15, 1), 'Param6')
x_Unst_Org_Env = ctrl.Antecedent(np.arange(0, 15, 1), 'Param7')
x_Mon_Close = ctrl.Antecedent(np.arange(0, 15, 1), 'Param8')
x_User_Rep = ctrl.Antecedent(np.arange(0, 15, 1), 'Param9')
x_Among_member = ctrl.Antecedent(np.arange(0, 15, 1), 'Param10')
x_Staff_Turn = ctrl.Antecedent(np.arange(0, 15, 1), 'Param11')
x_User_Resist = ctrl.Antecedent(np.arange(0, 15, 1), 'Param12')
x_Lack_Frozen_Sys = ctrl.Antecedent(np.arange(0, 15, 1), 'Param13')
x_Unfamilier_Subj = ctrl.Antecedent(np.arange(0, 15, 1), 'Param14')  
x_Unclear_Sys_Req= ctrl.Antecedent(np.arange(0, 15, 1), 'Param15')
x_Ambigu_Req = ctrl.Antecedent(np.arange(0, 15, 1), 'Param16')   
Risk = ctrl.Consequent(np.arange(0, 22, 1), 'Risk')

x_Organt_Man.automf(3)
x_Lack_Cop_Us.automf(3)
x_Indq_Infr.automf(3)
x_Corp_Pol_Neg.automf(3)
x_Fail_Identi.automf(3)
x_Tech_Complex.automf(5)
x_Unst_Org_Env.automf(5)
x_Mon_Close.automf(5)
x_User_Rep.automf(5)
x_Among_member.automf(5)
x_Staff_Turn.automf(5)
x_User_Resist.automf(7)
x_Lack_Frozen_Sys.automf(7)
x_Unfamilier_Subj.automf(7)
x_Unclear_Sys_Req.automf(7)
x_Ambigu_Req.automf(7)


Risk['low'] = fuzz.trimf(Risk.universe, [0, 0, 6])
Risk['medium'] = fuzz.trimf(Risk.universe, [2, 4, 8])
Risk['high'] = fuzz.trimf(Risk.universe, [6, 10, 10])
# Auto-membership function population is possible with .automf(3, 5, or 7)
rule1 = ctrl.Rule(x_Organt_Man['poor'] & x_Lack_Cop_Us['poor'] & x_Indq_Infr['poor'] , Risk['low'])
rule2 = ctrl.Rule(x_Corp_Pol_Neg['poor'] & x_Fail_Identi['poor'] & x_Tech_Complex['poor'], Risk['low'])
rule3 = ctrl.Rule(x_Unst_Org_Env['poor'] & x_Mon_Close['poor']&x_User_Rep['average'], Risk['low'])
rule4 = ctrl.Rule(x_Among_member['poor'] & x_Staff_Turn['poor'] & x_User_Resist['average'], Risk['low'])
rule5 = ctrl.Rule(x_Lack_Frozen_Sys['average'] & x_Unfamilier_Subj['poor']&x_Unclear_Sys_Req['poor'], Risk['low'])
rule6 = ctrl.Rule(x_Ambigu_Req['average'] & x_Fail_Identi['poor'] & x_User_Resist['poor'], Risk['low'])
rule7 = ctrl.Rule(x_Lack_Frozen_Sys['poor'] & x_User_Resist['average']&x_Unst_Org_Env['poor'], Risk['low']) 
rule8 = ctrl.Rule(x_Lack_Cop_Us['poor'] & x_Unst_Org_Env['poor'] & x_Indq_Infr['poor'], Risk['low']) 


rule9 = ctrl.Rule(x_Organt_Man['poor'] & x_Lack_Cop_Us['average'] & x_Indq_Infr['average'], Risk['medium']) 
rule10 = ctrl.Rule(x_Corp_Pol_Neg['average'] & x_Fail_Identi['poor'] & x_Tech_Complex['good'], Risk['medium']) 
rule11 = ctrl.Rule(x_Corp_Pol_Neg['poor'] & x_Fail_Identi['poor'] & x_Tech_Complex['average'], Risk['medium']) 
rule12 = ctrl.Rule(x_Unst_Org_Env['poor'] & x_Mon_Close['poor'] & x_User_Rep['good'], Risk['medium']) 
rule13 = ctrl.Rule(x_Unst_Org_Env['average'] & x_Mon_Close['poor'] & x_User_Rep['average'], Risk['medium']) 
rule14 = ctrl.Rule(x_Among_member['poor'] & x_Staff_Turn['average'] & x_User_Resist['average'], Risk['medium']) 
rule15 = ctrl.Rule(x_Lack_Frozen_Sys['average'] & x_Unfamilier_Subj['average'] & x_Unclear_Sys_Req['good'], Risk['medium']) 
rule16 = ctrl.Rule(x_Lack_Frozen_Sys['poor'] & x_Unfamilier_Subj['average'] & x_Unclear_Sys_Req['poor'], Risk['medium']) 

                 
 
rule17 = ctrl.Rule(x_Organt_Man['average'] & x_Lack_Cop_Us['average'] & x_Indq_Infr['good'], Risk['high']) 
rule18 = ctrl.Rule(x_Organt_Man['good'] & x_Lack_Cop_Us['good'] & x_Indq_Infr['average'], Risk['high']) 
rule19 = ctrl.Rule(x_Corp_Pol_Neg['average'] & x_Fail_Identi['average'] & x_Tech_Complex['good'], Risk['high']) 
rule20 = ctrl.Rule(x_Unst_Org_Env['average'] & x_Mon_Close['average'] & x_User_Rep['good'], Risk['high']) 
rule21 = ctrl.Rule(x_Among_member['good'] & x_Staff_Turn['average'] & x_User_Resist['good'], Risk['high']) 
rule22 = ctrl.Rule(x_Among_member['average'] & x_Staff_Turn['average'] & x_User_Resist['good'], Risk['high']) 
rule23 = ctrl.Rule(x_Lack_Frozen_Sys['poor'] & x_Unfamilier_Subj['good'] & x_Unclear_Sys_Req['good'], Risk['high']) 
rule24 = ctrl.Rule(x_Ambigu_Req['average'] & x_Staff_Turn['average'] & x_Tech_Complex['good'], Risk['high']) 

                 
arr=[rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9,rule10,rule11,rule12,rule13,rule14,rule15,rule16,rule17,rule18,rule19,rule20,rule21,rule22,rule23,rule24]

# Custom membership functions can be built interactively with a familiar,
# Pythonic API

risking_ctrl = ctrl.ControlSystem(arr)
RiskLevel = ctrl.ControlSystemSimulation(risking_ctrl,flush_after_run = 8  *  8  +  1)

upsampled = np.linspace(-2, 2, 16)
x, y = np.meshgrid(upsampled, upsampled)
z = np.zeros_like(x)

for i in range(16):
    for j in range(16):
        RiskLevel.input['Param1'] = x[i, j]
        RiskLevel.input['Param2'] = y[i, j]
        RiskLevel.input['Param3'] =x[i, j]
        RiskLevel.input['Param4'] =y[i, j]
        RiskLevel.input['Param5'] = x[i, j]
        RiskLevel.input['Param6'] =y[i, j]
        RiskLevel.input['Param7'] =x[i, j]
        RiskLevel.input['Param8'] =y[i, j]
        RiskLevel.input['Param9'] = x[i, j]
        RiskLevel.input['Param10'] =y[i, j]
        RiskLevel.input['Param11'] = x[i, j]
        RiskLevel.input['Param12'] = y[i, j]
        RiskLevel.input['Param13'] = x[i, j]
        RiskLevel.input['Param14'] = y[i, j]
        RiskLevel.input['Param15'] = x[i, j]
        RiskLevel.input['Param16'] = y[i, j]             
        RiskLevel.compute()
        z[i, j] = RiskLevel.output['Risk']

# Plot the result in pretty 3D with alpha blending
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # Required for 3D plotting

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap='viridis',
                       linewidth=0.4, antialiased=True)

cset = ax.contourf(x, y, z, zdir='z', offset=-2.5, cmap='viridis', alpha=0.5)
cset = ax.contourf(x, y, z, zdir='x', offset=3, cmap='viridis', alpha=0.5)
cset = ax.contourf(x, y, z, zdir='y', offset=3, cmap='viridis', alpha=0.5)

ax.view_init(30, 200)
print(RiskLevel.output['Risk'])
Risk.view(sim=RiskLevel)

canvas = FigureCanvasTkAgg(fig, frame)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH,expand=True)

toolbar = NavigationToolbar2Tk(canvas, frame)
toolbar.update()
    
def refresh():
    root.destroy()
    def execfile(filepath, globals=None, locals=None):
        import sys
        sys.setrecursionlimit(10000)
        if globals is None:
            globals = {}
               
        globals.update({
                "__file__": filepath,
                "__name__": "__main__",
                })
    
    with open(filepath, 'rb') as file:
        exec(compile(file.read(), filepath, 'exec'), globals, locals)

# execute the file
    execfile("C:\\Users\\hbaha\\OneDrive\\Masaüstü\\FuzzyLogic_Project\\SkFuzz3dRand.py")
button = tk.Button(root, text = "Click here to refresh",command = refresh)
button.pack(side=tk.BOTTOM, fill=tk.BOTH)
    

root.mainloop()
