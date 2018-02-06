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

X4B = (FourB_data['Counts'].sum())/N

# Gauss Standard Deviation
sigma = np.sqrt(X4B)

#Sample Variance s^2 = VarSam
# =============================================================================
# How to get single value
# print(FourB_data['Counts'][1])
# =============================================================================

def VarSam (givenDF,meanExp):
    N=len(givenDF)
    VarSam_Top = 0
    for i in range(N):
        VarSam_Top += (givenDF -meanExp)**2
    VarSam=VarSam_Top/N    
    return VarSam
# =============================================================================
# VarSam_Top = 0
# for i in range(N):
#     VarSam_Top += (FourB_data['Counts'][i] -X)**2
# VarSam=VarSam_Top/N
# =============================================================================
varSam4B = VarSam(FourB_data,X4B)
print('Experimental Mean: '+str(X4B))    
print('Sample Variance: '+str(varSam4B))
print('Standard Deviation s ~ ' +str(np.sqrt(varSam4B)) + ' Sigma ~ ' +str(sigma))

# Refine data with 3sigma test
# Define bounds
lowBound=X4B-3*sigma
upBound = X4B+3*sigma

# Compare only keep if within bounds
refined4B = []
for i in range(N):
    if FourB_data['Counts'][i]<upBound and FourB_data['Counts'][i] > lowBound:
        refined4B.append(FourB_data['Counts'][i])
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    