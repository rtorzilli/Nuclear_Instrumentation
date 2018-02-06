# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 20:28:30 2018

@author: Robert
"""
# place this code in same directory as excel book
import pandas as pd # for excel
import os # for generalization call
import numpy as np #for math

# Windows path for calls
currentDir = os.path.abspath(os.path.dirname(__file__))

dataLoc = currentDir+"\\300N.xlsx"

FourB_data = pd.read_excel(dataLoc, sheetname='4B')
FourC_data = pd.read_excel(dataLoc, sheetname='4C')
FourD_data = pd.read_excel(dataLoc, sheetname='4D')
BG_data = pd.read_excel(dataLoc, sheetname='4D_BackGround')

# Analysis for data from Procedure 4 B

# N Measurements
N=len(FourB_data)

# Experimental Mean X

X = (FourB_data['Counts'].sum())/N


#Sample Variance s^2 = VarSam
# =============================================================================
# How to get single value
# print(FourB_data['Counts'][1])
# =============================================================================
VarSam_Top = 0
for i in range(N):
    VarSam_Top += (FourB_data['Counts'][i] -X)**2
VarSam=VarSam_Top/N

print('Experimental Mean: '+str(X))    
print('Sample Variance: '+str(VarSam))

